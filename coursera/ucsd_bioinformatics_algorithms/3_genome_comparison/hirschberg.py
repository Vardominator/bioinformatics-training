from collections import OrderedDict
import re

def middle_column_score(v, w, scoring_matrix, sigma):
    '''Returns the score of the middle column for the alignment of v and w.'''

    # Initialize the score columns.
    S = [[i*j*sigma for j in xrange(-1, 1)] for i in xrange(len(v)+1)]
    S[0][1] = -sigma
    backtrack = [0]*(len(v)+1)

    # Fill in the Score and Backtrack matrices.
    for j in xrange(1, len(w)/2+1):
        for i in xrange(0, len(v)+1):
            if i == 0:
                S[i][1] = -j*sigma
            else:
                scores = [S[i-1][0] + scoring_matrix[v[i-1], w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])

        if j != len(w)/2:
            S = [[row[1]]*2 for row in S]

    return [row[1] for row in S], backtrack


def middle_edge(v, w, scoring_matrix, sigma):
    '''Returns the middle edge in the alignment graph of v and w.'''

    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    source_to_middle = middle_column_score(v, w, scoring_matrix, sigma)[0]

    # Get the score of the middle column from the middle to sink.  Reverse the order as the computations are done in the opposite orientation.
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], scoring_matrix, sigma))

    # Get the componentwise sum of the middle column scores.
    scores = map(sum, zip(source_to_middle, middle_to_sink))

    # Get the position of the maximum score and the next node.
    max_middle = max(xrange(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)/2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)/2 + 1), (max_middle, len(w)/2 + 1), (max_middle + 1, len(w)/2),][backtrack[max_middle]]

    return (max_middle, len(w)/2), next_node

def global_alignment(v, w, scoring_matrix, sigma):

    # Initialize the matrices.
    S = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]
    backtrack = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]

    # Initialize the edges with the given penalties.
    for i in xrange(1, len(v)+1):
        S[i][0] = -i*sigma
    for j in xrange(1, len(w)+1):
        S[0][j] = -j*sigma

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    v_aligned, w_aligned = v, w

    # Get the position of the highest scoring cell in the matrix and the high score.
    i, j = len(v), len(w)
    max_score = str(S[i][j])

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    # Prepend the necessary preceeding indels to get to (0,0).
    for repeat in xrange(i):
        w_aligned = insert_indel(w_aligned, 0)
    for repeat in xrange(j):
        v_aligned = insert_indel(v_aligned, 0)

    return max_score, v_aligned, w_aligned

def space_efficient_global_alignment(v, w, scoring_matrix, sigma):
    '''Return the global alignment of v and w using a linear space algorithm.'''

    def linear_space_alignment2(top, bottom, left, right):
        '''Constructs the global alignment path using linear space.'''

        if left == right:
            return [v[top:bottom], '-'*(bottom - top)]

        elif top == bottom:
            return ['-'*(right - left), w[left:right]]

        elif bottom - top == 1 or right - left == 1:
            return global_alignment(v[top:bottom], w[left:right], scoring_matrix, sigma)[1:]

        else:
            # Get the middle edge and the corresponding nodes.
            mid_node, next_node = middle_edge(v[top:bottom], w[left:right], scoring_matrix, sigma)

            # Shift the nodes appropriately, as they currently don't alighn with the top/left starting points.
            mid_node = tuple(map(sum, zip(mid_node, [top, left])))
            next_node = tuple(map(sum, zip(next_node, [top, left])))

            # Get the character in each alignment corresponding to the current middle edge.
            # (Take the index modulo the string length to avoid IndexErrors if we reach the end of a string but still have -'s to append.)
            current = [['-', v[mid_node[0] % len(v)]][next_node[0] - mid_node[0]], ['-', w[mid_node[1] % len(w)]][next_node[1] - mid_node[1]]]

            # Recursively divide and conquer to generate the alignment.
            A = linear_space_alignment2(top, mid_node[0], left, mid_node[1])
            B = linear_space_alignment2(next_node[0], bottom, next_node[1], right)
            return [A[i] + current[i] + B[i] for i in xrange(2)]

    # Get the alignment and alignment score.
    v_aligned, w_aligned = linear_space_alignment2(0, len(v), 0, len(w))
    score = sum([-sigma if '-' in pair else scoring_matrix[pair] for pair in zip(v_aligned, w_aligned)])

    return str(score), v_aligned, w_aligned


SCORES = {}
with open('data/blosum62.txt', 'r') as stream:
    SCORES = OrderedDict({k:{} for k in re.split('\s+', stream.readline().strip())})
    for row in stream.readlines():
        vals = re.split('\s+', row.strip())
        i = 1
        for letter in SCORES.keys():
            SCORES[vals[0]][letter] = int(vals[i])
            i += 1

# indel penalty
SIGMA = 5

# Read the input data.
with open('data/week3problem2.txt') as input_data:
    word1, word2 = [line.strip() for line in input_data.readlines()]

# Get the alignment.
alignment = space_efficient_global_alignment(word1, word2, SCORES, 5)

# Print and save the answer.
print '\n'.join(alignment)
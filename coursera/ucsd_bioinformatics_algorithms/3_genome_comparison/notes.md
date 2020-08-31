# How do we compare biological sequences?
## Introduction
* Bacteria and fungi produce antibiotics and other non-ribosomal peptides (NRPs) without and reliance on the ribosome and the genetic code.
* Instead, these oganisms manufacture NRPs by employing a giant protein called NRP synthetase.
  - DNA -> RNA -> NRP synthetase -> NRP
* The NRP synthetase that encodes the 10 amino acid-long antibiotic Tyrocidine B1 includes 10 segments called adenylation domains (A-domains).

## Sequence Alignment
* Good alignment: one that matches as many symbols as possible
* Alignment of sequences v and w: two-row matrix such that the first row contains the symbols v (in order) and the second contains symbols of w (in order), and space symbols (gap symbols)
* An alignment presents one possible scenario by which v could have evolved into w
* matches: columns with the same letter in all rows
* mismatches: columns containing different letters
* indels: column containing a space symbol
* insertion: column containing a space symbol in the top row
* deletion: column containing a space symbol in the bottom row of the alignment
* common subsequence: matches in an alignment of two strings, or a sequence of symbols appearing in the same order, though not necessarily consecutively
* longest common subsequence (LCS): alignment of two strings maximizing the number of matches

## The Manhattan Tourist Problem
* The challenge of finding a legal path through the city that visits the most sights
* Find a maximum-weight path connecting the source to the sink (longest path).
* problem: longest path in a directed graph
  - input: an edge-weighted directed graph with source and sink nodes
  - output: a longest path from source to sink in the directed graph
* problem: longest path in a directed acyclic graph (DAG)
  - input: an edge-weighted DAG with source and sink nodes
  - output: a longest path from source to sink in the DAG

## sequence alignment and the manhattan tourist
* the alignmnt graph of strings v and w, represents the path from source to sink

# How do we compare biological indices II
## shortcomings of LCS scoring model
* more matches at the expense of introducing more indels. the more indels added, the less biologically relevant the alignment becomes
* we need some way of penalizing indels
* scoring matrices
  - +1 for matches
  - penalize mismatches by some positive constant u (mismatch penalty)
  - penalize indels by some positive constant s (indel penalty)
  - \# matches - u*\#mismatches - s*\#indels
* biologists have further refined this cost function to allow for the fact that some mutations may be more likely than others
  - mismatche/indel penalties differ depending on symbols involved
  - this leads to using a *scoring matrix* that holds the score of aligning every pair of symbols

## Limitations of global alignment
* An important question is how to find a conserved segment within much longer genes and ignore the flanking areas, which exhibit little similarity.
* How can we rule out biologically irrelevant alignments when local similarities are present?

## Local alignment problem
* When biologically significant similarities are present in some parts of sequences and absent from others, biologists attempt to ignore global alignment and instead alignt substrings. This results in a *local alignment*. 
* Local Alignment Problem: find the highest-scoring local alignment between two strings
  - input: strings v and w as a matrix score
  - output: substrings of v and w whose global alignment score (as defined by score) is maximized among all substrings of v and w

# How do we compare biological indices III
* Introducing mismatch and indel penalties can produce more biologically adequate global alignments. However, even with this more robust model, the A-domain alignment is still not perfect.
* Increasing the indel penalty would result in more mismatches instead of indels, rather than providing a more accurate result.
* The previously defined *linear scoring model* does not account for DNA replication errors that insert or delete entire interval of nucleotides as a single event instead of as k independent insertions or deletions. 
* A *gap* is a contiguous sequence of spaces in a row of an alignment. 
* One can score gaps more appropriately by defining an *affine penalty* for a gap of length k as sigma + epsilon * (k - 1)
  - sigma: gap opening penalty
  - epsilon: gap extension penalty
* Select epsilon to be smaller than sigma so that the affine penalty for a gap of length k is smaller than the penalty for k independent single-nucleotide indels (sigma * k)
* Alignment with affine gap penalties problem: construct a highest-scoring global alignment between strings (with affine gap penalties)
  - input: two strings, a matrix score, and numbers sigma and epsilon
  - output: highest scoring global alignment between strings, as defined by the scoring matrix score and by the gap opening and extension penalties sigma and epsilon
* Since we do not know in advance where gaps should be located, we need to add edges accounting for every possible gap.
* Naive approach: add edges connecting (i, j) to both (i + k, j) and (i, j + k) with weights sigma + epsilon * (k-1) for all possible gap sizes k. This increases the number of edges from P(n^2) to O(n^3)

## 3-level Manhattan
* Trick to decreasing the number of edges in the DAG is to increase the number of nodes.
* We will build an alignment graph on three levels. For each node (i, j) we will construct 3 different nodes:
  - (i,j) lower: vertical edges with weight -epsilon to represent gap extensions in v
  - (i,j) middle: diagonal edges of weight score(v_i, w_j) representing matches and mismatches
  - (i,j) upper: horizontal edges with weight -epsilon to represent gap extensions in w
* We add edges responsible for opening and closing gaps. To model gap opening, we connect each node (i,j) middle to both (i+1) lower and (i, j+1) upper. Each edges is weighted with -sigma. 
* Closing a gap does not carry a penalty, so zero-weight edges are introduced to connect (i,j) lower and (i,j) upper with (i,j) middle. 
* A gap of length k starts and ends at the middle level, charged -sigma for the first symbol, -epsilon for each subsequent symbol, and 0 to close the gap => sigma + epsilon * (k - 1)
* O(n * m) edges for sequences of length n and m.
* A longest path in this graph constructs and optimal alignment with affine gap penalties. 

## Implementation of 3-level Manhattan
* Bottleneck: NRP synthesases are long (~20000 amino acids)
  - alignment runtime: proportional to #edges (quadratic)
  - alignment memory: proportional to #nodes (quadratic)
* Memory is often a bottleneck when comparing long sequences.
* Middle Node of the alignment: a node where an optimal alignment path crosses the middle column. How can we find this middle node in linear time?
* Computing alignment score in linear space
  - Finding the longest path in the alignment graph requires storing all backtracking pointers - O(nm) memory
  - Computing the length of the longest path does not require storing any backtracking pointers - O(n) memory
* Calculating the scores of the nth column does not require values of the (n-2)th column, just the (n-1)th column.
* i-path: a longest path among ALL paths that visit the i-th node in the middle column.
  - length(i) = fromSource(i) + toSink(i)
* O(nm) time; O(nm) space

## Multiple Sequence Alignment
* Scoring function should score alignments with conserved columns higher.
* Alignments of 3 sequences are 3-D paths in a 3-D Manhattan grid.
* There will need be a maximum of 7 values, one for each neighbor.
* Multiple alignment: running time
  - For 3 sequences of length n, the run time is proportional to the number of edges in the 3-D grid, i.e. 7n^3
  - For a k-way alignment, build a k-dimensional Manhattan graph with:
    * n^k nodes
    * most nodes have 2^k - 1 incoming edges
    * runtime: O(2^k n^k)
* Biologists usually use heuristics that do not guarantee an optimal solution. 
* Multiple alignments from pairwise alignments? Generally not possible. 
* Profile representation of multiple alignment. Can we align sequences against a profile or a profile against a profiles? 
* Greedy multiple alignment
  - Choose the most similar sequences and combine them into a profile, thereby reducing k-way alignment to (k-1)-way alignment of (k-2) sequences and 1 profile
  - iterate...

## Space-Efficient Sequence Alignment
* If we only wish to compute the score of an alignment rather than the alignment itself, then the space required can easily be reduced to just twice the number of nodes in a single column of the alignment graph, or O(n).

### The Middle Node Problem
* middle node: the node where the longest path crosses the middle column
* i-path: passes through the middle column at row i
* Length(i) = FromSource(i) + ToSink(i)
  - FromSource(i) is s[i][middle

### Middle Edge in Linear Space Problem: Find a middle edge in the alignment graph in linear space
* input: two strings and a matrix score
* output: a middle edge in the alignment graph of these strings
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

# Genome rearrangmenets and fragility
## Introduction: Random Breakage Model
* Mice and men look different, but genetically they are very similar. The genes are just arranged differently.
* Genome rearrangement: mouse x chromosome to human x chromosome
  - What are the similarity blocks and how to find them?
  - What is the evolutionary scenario for transforming one genome into the other?
* Reversal: reversing ordering of genes as an evolutionary process
* Are there any rearrangement hotspots in mammalian genomes?
* Random Breakage Model (RBM) of Chromosome Evolution
  - Nadeau & Taylor (1984): the first statistical arguments in favor of the RBM
* Does RBM have predictive power, despite the fact that breakage happens at random places?
  - Apply N random reversals to a chromosome consisting of M "genes". Can we predict how many blocks of length k will be generated?
  - Furthermore, if we can predict it, will these predictions fit what we observe in real genomes?
  - Despite the fact that reversals occur at random positions, we can predict (roughly) how many blocks of each length will be generated. This follows an exponential distribution.

## Reversal
* Reversal introduced two breakpoints: diseruptions in gene order.
* Reversal distance: the minimum number of reversals required to transform one permutation into another.
* Greedy Sorting by Reversal

## Breakpoint Theorem
* Adjacencies and Breakpoints
* adjacencies(P) + breakpoints(P) = |P| + 1
  - What is the number of breakpoints in the identity permutation? 1, 2, 3, ... + n
* sorting by reversal => breakpoint elimination
  - How many breakpoints can be eliminated by a single reversal? Reversal has two ends and nothing happens outside of these ends. Only the ends themselves can be breakpoints. Thus, at every step the number of breakpoints can be decreased by at most 2.
* Breakpoint Theorem: Reversal distance >= breakpoints(P)/2

## Rearrangements in Tumor Genomes
* Philadelphia Chromosome
  - abl and bcr genes
* fusions and fissions

## 2-breaks
* Want to think of human genome as cyclic because the problem becomes easier without changing the results.
* Linear to Circular chromosomes
* 2-break: a reversal that deletes two red edges and replaces them by two other red edges (on the same 4 nodes)
* 2-break distance d(P, Q): minimum number of 2-breaks transforming genome P into genome Q

## Greedy sorting
* Element k in permutation P = (p_1..p_n) is sorted if p_k = +k and usorted otherwise
* P is k-sorted if its first k elements are sorted, but if element k is unsorted.
* For every k-sorted permutation P, there exists a single reversal, called the k-sorting revrsal, that fixes the first k - 1 elements of P and moves element k to the k-th position. If k is already in the k-th position of P, the k-sorting reversal merely flips -k around. 

# Applying genome rearrangment analysis to find genome fragility
## Breakpoint graphs
* Red and blue edges form alternating red-blue cycles
* cycle(P, Q): number of red-blue alternating cycles
* Given P, what Genome Q maximizes cycle(P, Q)?
* Genome rerrangements affect red-blue cycles
  - Each transformation P -> Q corresponds to a transformation

## 2-break distance theorem
* We don't know how many breakpoints transform P into Q, but we do now that the breakpoint of P and Q transforms into the breakpoint of Q and Q. Thus, the cycle number changes into the cycle number between Q and Q, which in turn is the number of blocks in Q. 
* Therefore, the number of red-blue cycles increases by blocks(P,Q) - cycle(P,Q)
* A 2-break adds 2 new edge edges and therefore creates at most 2 new cycles with 2 new red edges. It removes 2 red edges and therefore destroys at least 1 old cycle with two old edges. Thus, the change in the number of cycles <= 2-1 = 1
* 2-break distance theorem
  - a 2-break increases the number of cycles by at most 1
  - there exists a 2-break increasing the number of cycles by 1
  - every sorting by 2-breaks must increase the number of cycle by blocks(p,q) - cycle(p,q)
  - 2-break distance between genomes P and Q: d(p,q) = blocks(p,q) - cycle(p,q)
* 2-break distance between human and mouse genomes
  - human and mouse genomes can be decomposed into 280 synteny blocks (at least 0.5 million nucleotides in length)
  - the breakpoint graph on these blocks as 35 cycles
  - the 2-break distance between human and mouse:
    * d(H,M) = blocks(H,M) - cycle(H,M) = 280 - 35 = 245
  - there are numerous 245-step scenarios
  - the true scenario may have more than 245 steps

## Rearrangment hotspots in the genome
* Are there any? yes
* Is there a model that complies with both the "exponential distribution" and the "breakpoint reuse" tests? yes it is the Fragile Breakage Model
* Fragile Breakage Model
  - The genome is a mosaic of:
    * fragile regions with high propensity for rearrangements and
    * solid regions with low propensity for rearrangments
  - fragile regions (regions between consecutive synteny blocks) are small, accounting for less than ~5% of the genome.
* Does FBM explain both exponential distribution and rearragnment hotspots?
  - A small number of short fragile regions explain rearrangement hotspots.
  - If the fragile regions are somewhat randomly distributed throughout the genome, the synteny blocks follow the exponential distribution.
* Multiply Breakpoint Reuse Test
* Birth and Death of Fragile Regions
  - Recent studies revealed evidence for the "birth and death" of the fragile regions, implying that they move to different locations in different lineages.
  - This led to discovery of the Turnover Fragile Breakage Model (TFBM) that complies with a new Multiple Breakpoint Reuse (MBR) test
  - TFBM points to locations of the currently fragile regions

## Synteny block construction
* identitcal and reverse complementary k-mers
* amounts to constructing diagonals
* Finding Synteny Blocks Problem: find diagonals in the genomic dot-polot
  - input: a set of points DotPlot in 2-D
  - output: a set of diagonals in DotPlot representing synteny blocks
* Nodes: points in 2-D
* Edges: connect close points (distance below maxDistance)
* Synteny Block Generation Algorithm

* Simple
```
Synteny(DotPlot, maxDistance, minSize)
  maxDistance: gap size
  minSize: minimum synteny block size
  1. form a graph whose node set is the set of points in DotPlot
  2. connect two nodes by an edge if the 2-D distance between them is < maxDistance. The connected components in the resulting graph define synteny blocks
  3. delete small synteny blocks (length < minSize)
```

## Stepik week 5
* Solving the 2-break distance problem for genomes P and Q is equivalent to finding a shortest series of 2-breaks transformaing BreakpointGraph(P,Q) into the trivial brekapoint graph. 
* Since every transformation of P into Q transforms BreakPointGraph(P, Q) into the trivial brekapoint graph BreakpointGraph(Q,Q), any sorting of 2-breaks increases the number of red-blue cycles by: Cycles(Q,Q) - Cycles(P,Q)
* Cycle Theorem: given genomes P and Q, and 2-break applied to P can increase Cycles(P,Q) by at most 1.
* There are permutations for which no reversal reduces the number of breakpoints, which means that a greedy algorithm for sorting reversals that reduces the number of breakpoints at each step cannot work. 
* 2-break distance theorem: the 2-break distance between genomes P and Q is equal to Blocks(P,Q) - Cycles(P,Q)

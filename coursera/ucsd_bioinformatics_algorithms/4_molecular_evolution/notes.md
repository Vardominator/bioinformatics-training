# Which animal gave us SARS?
* In a matter of a few weeks, biologists identified a virus that had caused the epidemic and sequenced its genome. 
* SARS: severe acute respiratory syndrome
* SARS belongs to a family of viruses called coronaviruses
* RNA viruses
  - coronaviruses, influenza viruses, and HIV
  - they possess RNA instead of DNA
  - RNA replication has a higher error rate than DNA replication. Thus, RNA viruses are capable of mutating more quickly into divergent strains.
* When researchers sequenced the 29,751 nucleotide-long SARS-CoV genome, it was clear that it did not come from birds.
* Questions remained:
  - How did sars-cov cross the species barrier to humans
  - When and where did it happen
  - How did sars spread around the world, and who infected whom
* Each of these questions are somehow related to constructing evolutionary trees (phylogenies). 

## Constructing distance matrix from coronavirus genomes
* To determin how SARS jumped from animals to humans, scientist began sequencing coronviruses from various species in order to determine which one is the most similar to SARS-CoV.
* Due to the complex and dynamic nature of viral genomes, scientists focused on one of six genes in SARS-CoV. This gene encodes the *spike protein* which identifies and binds to receptor sites on the host's cell membrane.
* Spike protein is 1,255 amino acids long and has weak similarity with spike proteins in other coronaviruses.
* Distance matrix: an entry represents the number of differing symbols between the genes representing rows i and j of the alignment.
  - The distance function can vary. 
  - The distance function must satisfy three properties:
    * symmetric
    * non-negative
    * triangle inequality: for all i,j, and k, D_i_j + D_j_k >= D_i_k
* Scientists used these matrices to construct a coronavirus phylogeny and understand the origin and spread of SARS
* Graphs used to model phylogenies share two properties:
  - connected: possible to reach any node from any other node
  - contain no cycles
* In a rooted tree, one node is designated as a special node called the root. Trees without a designated root are called unrooted.

## Distance matrix to evolutionary tree
* Distance-based phylogeny problem: reconstruct an evolutionary tree fitting a distance matrix
  - input: a distance matrix
  - output: a tree fitting this matrix
* Not every distance matrix has a tree fitting
  - A distance matrix is additive if there exists a tree, non-additive otherwise
* A tree is non-branching if every node other than the beginning and ending node of the path has a degree equal to 2.
* A non-branching path is maximal if it is not a subpath of an even longer non-branching path
* A matrix is additive, then there exists a simple tree fitting this matrix.
* Simple tree: no edges of degree two

## Algorithm for distance-based phlyogeny construction
* Ensure that the two closest species with respect to the distance matrix D correspond to neighbors in Tree(D). The minimum value D_i_j should correspond to leaves i and j having the same parent.
* Thereom: every simple tree with at least four nodes has a pair of neighboring leaves
* Limb length: length of the limb connecting j with its parent
* Limb length problem: compute the length of a limb in a tree defined by an additive distance matrix
  - input: an additive distance matrix D and an integer j
  - output: LimbLength(j), the length of the limb connecting leaf j to its parent in Tree(D)

# What animal gave us SARS? part 2
## Sum of squared errors
* We can construct a tree that is the best approximate solution for a given (potentially) non-additive matrix
* Least-squares distances-based phlogeny problem

## Ultrametric trees
* Researchers often assume that all internal nodes correspond to speciations, where one species splits into two.
* Unrooted binary tree: every node has degree 1 or 3
* Rooting the tree results in a rooted binary tree: an unrooted binary tree with a root (of degree 2) on one of its edges
* Heuristic that models a molecular clock: assigns ages to each node in the tree (age of leaves = 0)
* Once we assign ages to each node, we get the edge weights by subtracted ages between nodes.
* If we assign ages, then the tree becomes ultrametric: all paths from leaf to root are equal in lenght
* UPGMA: a clustering heuristic
  1. form a cluster for each present-day species, each containing a single leaf
  2. find the two closest clusters C1 and C2 according to the average distance
  3. Merge C1 and C2 into a single cluster C
  4. Form a new node for C and connect to C1 and C2 by an edge. Set age of C as D_avg(C1, C2) / 2
  5. Update the distance matrix by computing the average distance between each pair of clusters. 
  6. Iterate until a single cluster contains all species.

## Neighbor-joining Algorithm
* Theorem: If D is additive, then the smallest element of D\* corresponds to neighboring leaves in Tree(D)
* Steps
  - Construct matrix D*
  - Find a minimum element D\*_i,j of D\*
  - Compute delta_i_j = ()
  ...
* Weakness of distance-based methods
  - distance-based algorithms for evolutionary tree reconstruction say nothing about ancestral states at internal nodes
  - we lost information when we converted a multiple alignment to a distance matrix

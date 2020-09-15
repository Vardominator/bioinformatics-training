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

# What animal gave us SARS? part 3
## Character tables
* Back in the day, biologists constructed phylogenies not from DNA and protein sequences but from anatomical and physiological features called characters. 
* Ever row in an n x m character table represents a *character vector*, holding the values of m characters corresponding to one of n existing species.
* Goal: construct an evolutionary tree in which leaves corresponding to present-day species with similar character vectors occur near each other in the tree.
* Goal: Asisgn m character values to each internal node in the tree in order to best explain the characters of ancestral species.
* Another fucking goal: construct a tree whose leaves correspond to the rows of this alignment and whose internal nodes correspond to ancestral sequences in accordance with the most parsimonious evolutionary scenario.
* Dollo's principle of irreversibility: when a species loses a complex organ, such as wings, the organ will not reappear in exactly the same form in the specie's descendants

## Small parsimony problem
* label each leaf of a tree by a row of multiple alignment
* given a tree T with every node labeled by a string of length m, set the length of edge (v,w) equal to the number of substitutions (hamming distance) between the strings labeling v and w. 
* the parsimony score of T is the sum of the lengths of the edges
* Small Parsimony Problem: find the most parsimonious labeling of the internal nodes of a rooted tree

# Was T.rex just a big chicken?
* T.rex and chicken collagens are nearly identical
* Mass spectrometers sequence proteins. They generate a cryptic peptide called a mass spectra

## Sequencing proteins with mass spectrometry
* most mass spectrometers can only measure masses of rather short peptides (e.g. < 30-40 amino acids). To bypass this limitation:
  - proteases (e.g., trypsin) break proteins into short peptides
  - a mass spectrometer breaks these peptides into charged fragment ions and measures the mass/charge ratio* and intensity of each ion
  - for simplicity, we assume that all masses are integers and all charges are 1
* How do we construct the peptide from the collection of mass/charge ratios?

## Decoding an ideal spectrum
* We don't know which masses correspond
* Decoding an ideal spectrum problem: reconstruct a peptide from its ideal spectrum
  - input: a collection of integers Spectrum
  - output: an amino acid string Peptide that explains Spectrum
* Graph representation
  - Nodes: masses in the spectrum
  - Edges: connect node i to node j if j-i is the mass of an amino acid a. Label this edge by a.
* DecondingIdealSpectrum(Spectrum)
  - construct Graph(Spectrum)
  - find a path Path from source to sink in Graph(Spectrum)
    * return amino acid string spelled by labels of Path
* Does this really work?

## Peptide sequencing
* Score of Peptide against Spectrum is the *dot product* of Peptide and Spectrum


# Was t.rex just a big chicken? part 2
## Peptide identification
* We need to develop a method for evaluating the statistical significance of identified peptides.
* Given a parameter *threshold*, a peptide Peptide and a spectral vector Spectrum for a Peptide-Spectrum Match (PSM) if:
  - Peptide is the highest-scoring peptide against Spectrum among all peptides in Proteome
  - Score(Peptide, Spectrum) >= threshold
* PSM_threshold(Proteome, SpectralVectors): set of Peptide-Spectrum Matches (PSMs) resulting from a set of SpectralVectors (for a given Proteome and threshold)
* PSM search problem: Identify all Peptide-Spectrum Matches scoring above a threshold for a set of spectra and proteome

## Spectral Dictionaries
* How can we estimate the statistical significance of an individual PSM?
* The Monkey and the Typewriter Problem: find the expected number of strings from dictionary appearing in a randomly generated text
  - input: set of strings Dictionary and an integer n
  - output: expected number of strings from Dictionary that appear in a randomly generated string of length n

## Stepik
* Although the correct peptide often does not achieve the highest score among all peptides, it typically does score highest among all peptides limited to the specie's proteome

# Final Project
* Objective 1: place the strain causing the 2014 outbreak within the evolavirus phylogeny by constructing a multiple alignment of ebola genome sequences
* Objective 2: Create phylogenic tree from a multiple alignment of indivuduals that have contracted the different strains of ebola virus
* Questions
  - How are viruses actually sequenced?
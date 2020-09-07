# How did yeast become a wine maker?
* Why do winemakers store grapes in sealed barrels
  - Yeast lives on grapevines and can convert glucose into ethanol.
  - When the glucose runs out, yeast inverts its metabolism, and ethanol becomes its new food.
  - This change in metabolism (the diauxic shift) can only occur in the presence of oxygen. What genes are responsible for the diauxic shift?
* What does it take to convert glucose into ethanol?
  - Imagine the time when the first fruit-bearing plants evolved.
  - The first species to metabolize to metabolize glucose would have had an enormous evolutionary advantage.
  - Metabolizing glucose or ethanol is not easy. It required creating new metabolic pathways with many genes working together.
* How did yeast invest the diauxic shift?
  - Susumu Ohno: two hyptheses with different fates
  - Random breakage model: genomic architectures are shaped by rearrangments that occur randomly.
  - Whole genome duplication model: big leaps in evolution would have been impossible without whole genome duplications.
* Whole genome duplication enables evolutionary breakthroughs
  - Ohno argued that a WGD would provide a platform for such a revolutionary innovation, since every gene would have two copies
  - One copy would be free to evolve without compromising the gene's existing function
  - Another copy would perform the existing function

# Gene expression matrices
* expression level of gene i at checkpoint j
* goal: partition all yeast genes into clusters so that:
  - genes in the same cluster have similar behavior

# Clustering as an optimization problem
* clustering problem: find a partition of expression vectors into clusters satisfying the good clustering principle
  - input: a collection of n vectors and an integer k
  - output: partition of n vectors into k disjoint clusters satisfying the good clustering principle
* modifying the objective function: maximal distance => squared error distortion
  - k-center clustering => k-means clustering
* center of gravity theorem: the center of gravity of points data is the only point solving the 1-means clustering problem
  - sum of all points datapoint in data / number points in data
* lloyd algorithm: select k arbitrary data points as centers and then iteratively perform the following steps:
  - centers to clusters: assign each data point to the cluster corresponding to its nearest center (ties are broken arbitrarily)
  - clusters to centers: after the assignment of data points to k clusters, compute new centers as clusters' center of gravity

# From hard to soft clustering
* estimating the unknown bias
  - flip a loaded coin with an unknown bias theta (probability that the coin lands on heads)
  - the lands on heads i out of n times
  - for a known bias, we can compute the probability of the resulting sequence of flips

# From coin flipping to k-means clustering
* What are data, hiddenvector, and parameters?
  - data: data points
  - parameters: centers
  - hidden vector: assignment of data points to k centers

# Expectation Maximization
* coin flipping: how would you select between coins A and B if Pr(sequence|theta_a) == Pr(sequence|theta_b)
* k-means clustering: what cluster would you assign a data point to if it is a midpoint of centers C_1 and C_2?
* soft assignments: assigning C_1 and C_2 "responsibility" ~0.5 for a midpoint

# Hierarchical clustering
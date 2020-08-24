from math import log2

def entropy(probabilities):
    return -1* sum([p*log2(p) for p in probabilities])

# print(-1 * (sum([0.7*log2(0.7), 0.1*log2(0.1), 0.2*log2(0.2)]) + sum([0.6*log2(0.6), 0.2*log2(0.2), 0.2*log2(0.2)]) + 1.0*log2(1.0) + 1.0*log2(1.0) + sum([0.9*log2(0.9), 0.1*log2(0.1)]) + sum([0.9*log2(0.9), 0.1*log2(0.1)]) + sum([0.9*log2(0.9), 0.1*log2(0.1)]) + sum([0.5*log2(0.5), 0.4*log2(0.4), 0.1*log2(0.1)]) + sum([0.8*log2(0.8), 0.1*log2(0.1), 0.1*log2(0.1)]) + sum([0.7*log2(0.7), 0.1*log2(0.1), 0.2*log2(0.2)]) + sum([0.4*log2(0.4), 0.3*log2(0.3), 0.3*log2(0.3)]) + sum([0.6*log2(0.6), 0.4*log2(0.4)])))
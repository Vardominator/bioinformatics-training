def completement(substring):
    complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    complement = "".join([complements[c] for c in substring][::-1])
    print(complement)
    return complement

# with open("Vibrio_cholerae.txt", 'r') as handle:
#     dataset = handle.readlines()

# pattern = "CTTGATCAT"
# genome = dataset[0].strip()

# matched_indices = []
# for i in range(0, len(genome) - len(pattern)):
#     # if completement(genome[i:i+len(pattern)]) == pattern:
#     #     print i
#     if genome[i:i+len(pattern)] == pattern:
#         matched_indices.append(i)

# print(" ".join([str(i) for i in matched_indices]))

print(completement("GCTAGCT"))
def completement(substring):
    complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    complement = "".join([complements[c] for c in substring[::-1]])
    return complement

def encoding(rna, mapping):
    amino = ''
    for i in range(0, len(rna), 3):
        if rna[i:i+3] in mapping:
            amino += mapping[rna[i:i+3]]
    return amino


def find_peptide_matchings(mapping, rna, peptide):
    matches = []
    rna_sub = ''
    amino = ''

    for i in range(0, len(rna), 3):
        if len(amino) == len(peptide):
            amino = ''
            rna_sub = ''
        if rna[i:i+3] in mapping:
            amino += mapping[rna[i:i+3]]
            rna_sub += rna[i:i+3]
            if amino == peptide:
                matches.append(rna_sub)
                amino = ''
                rna_sub = ''
    return matches

rna_codon_mapping = {}

with open('data/RNA_codon_table.txt', 'r') as stream:
    for row in stream.read().splitlines():
        rna, code = row.split(' ')
        rna_codon_mapping[rna] = code


# with open('data/Bacillus_brevis.txt', 'r') as stream:
#     genes = stream.read().splitlines()
#     original_dna = ''.join([g for g in genes])
#     peptide = "VKLFPWFNQY"

#     matches = []
#     for k in range(0, 3*len(peptide)):
#         dna = original_dna[k:]
#         for i in range(0, len(dna), 3*len(peptide)):
#             sub_dna = dna[i:i+3*len(peptide)]
#             sub_dna_comp = completement(dna[i:i+3*len(peptide)])
#             sub_rna = sub_dna.replace('T', 'U')
#             sub_rna_comp = sub_dna_comp.replace('T', 'U')

#             if encoding(sub_rna, rna_codon_mapping) == peptide:
#                 matches.append(sub_dna)
            
#             if encoding(sub_rna_comp, rna_codon_mapping) == peptide:
#                 matches.append(completement(sub_dna_comp))
#         print(len(matches))

# with open('data/Bacillus_brevis_result.txt', 'w') as stream:
#     stream.write(len(matches))


print(encoding('CCAAGUACAGAGAUUAAC', rna_codon_mapping))
print(encoding('CCAAGAACAGAUAUCAAU', rna_codon_mapping))
print(encoding('CCUCGUACAGAAAUCAAC', rna_codon_mapping))
print(encoding('CCGAGGACCGAAAUCAAC', rna_codon_mapping))
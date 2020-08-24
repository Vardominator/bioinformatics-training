def peptide_mass(peptide, mass_table):
    s = 0
    for p in peptide.split('-'):
        s += int(p)
    return s

def cyclospectrum(s):
    subs = [""]
    looped = s + s
    for i in range(len(s)):
        for j in range(1, len(s)):
            subs.append(looped[i:i + j])
    return subs

def consistent(peptide, spectrum):
    spectrum_counts = {}
    for s in spectrum:
        if s not in spectrum_counts:
            spectrum_counts[s] = 1
        else:
            spectrum_counts[s] += 1

    peptide_counts = {}
    for p in peptide:
        if p not in peptide_counts:
            peptide_counts[p] = 1
        else:
            peptide_counts[p] += 1
    
    for subpeptide in peptide_counts.keys():
        if subpeptide in spectrum:
            if peptide_counts[subpeptide] > spectrum_counts[subpeptide]:
                return False
        else:
            return False
    return True

def expand(candidate_peptides, mass_table):
    letters = list(mass_table.keys())
    new_candidates = []
    for peptide in candidate_peptides:
        # candidate_peptides.remove(peptide)
        for letter in letters:
            new_candidates.append(peptide + '-' + mass_table[letter])
    return new_candidates

def equals(cyclospectrum, spectrum):
    if len(cyclospectrum) != len(spectrum):
        return False
    cyclospectrum.sort()
    spectrum.sort()
    for i in range(len(cyclospectrum)):
        if cyclospectrum[i] != spectrum[i]:
            return False
    return True

def cyclopeptide_sequencing(spectrum, mass_table):
    candidate_peptides = [""]
    final_peptides = []
    spectrum_mass = peptide_mass(spectrum)
    while len(candidate_peptides) != 0:
        candidate_peptides = expand(candidate_peptides, mass_table)
        for peptide in candidate_peptides:
            if peptide_mass(peptide) == spectrum_mass:
                if equals(cyclospectrum(peptide), spectrum):
                    final_peptides.append(peptide)
                candidate_peptides.remove(peptide)
            elif not consistent(peptide, spectrum):
                candidate_peptides.remove(peptide)
    return final_peptides

mass_table = {}
with open('data/integer_mass_table.txt', 'r') as stream:
    for row in stream.read().splitlines():
        subpeptide, mass = row.split(' ')
        mass_table[mass] = subpeptide

print(mass_table)
with open('data/dataset_98_5.txt', 'r') as stream:
    spectrum = stream.read().split(' ')


cyclo_peptide = cyclospectrum("ABCDABCD")
def linear_peptide_count(length):
    s = 1
    for i in range(1, length + 1):
        s += i
    return s

mass_table = {}
with open('data/integer_mass_table.txt', 'r') as stream:
    for row in stream.read().splitlines():
        subpeptide, mass = row.split(' ')
        mass_table[subpeptide] = int(mass)

print(linear_peptide_count(17757))
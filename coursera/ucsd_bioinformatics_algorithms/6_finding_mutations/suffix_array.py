text = "ananas$"
suffixes = []

for i in range(len(text) - 1):
    suffixes.append(text[i:])


sorted_indices = [len(text) - 1] + sorted(range(len(suffixes)), key=lambda k: suffixes[k])
print(' '.join([str(i) for i in sorted_indices]))
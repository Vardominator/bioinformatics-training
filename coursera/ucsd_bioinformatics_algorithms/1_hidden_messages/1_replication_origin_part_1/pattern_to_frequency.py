value_mapping = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

pattern_mapping = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}

def pattern_to_number(text):
    size = len(text) - 1
    total = 0
    for t in text:
        total += value_mapping[t] * pow(4, size)
        size -= 1
    return total

def number_to_pattern(number):
    curr_num = number
    pattern = ''
    while curr_num != 0:
        pattern += pattern_mapping[curr_num % 4]
        curr_num = curr_num / 4
    return pattern[::-1]

def frequency_counts(text, k):
    frequencies = [0]*(pow(4, k))
    for i in range(0, len(text) - k + 1):
        p_to_n = pattern_to_number(text[i:i+k])
        frequencies[pattern_to_number(text[i:i+k])] += 1
    return frequencies

print(number_to_pattern(7769))

with open('data/dataset_3010_2.txt', 'r') as f1:
    pattern = f1.readlines()[0].strip()
# print(pattern_to_number(pattern))

with open('data/dataset_2994_5.txt', 'r') as f2:
    blah = f2.readlines()
    text = blah[0].strip()
    k = int(blah[1].strip())

with open('data/freq_array_results.txt', 'w') as hello:
    result = " ".join([str(f) for f in frequency_counts(text, k)])
    hello.write(result)

# 2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
# 1 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
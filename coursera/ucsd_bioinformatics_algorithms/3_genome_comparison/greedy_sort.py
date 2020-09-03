def greedy_sort(elements):
    i = 0
    num_reversals = 0
    results = []
    while i < len(elements):
        if abs(elements[i]) != i + 1:
            # not sorted
            j = i
            while j < len(elements) and abs(elements[j]) != i + 1:
                j += 1
            elements[i:j+1] = [-1*l for l in elements[i:j+1][::-1]]
            # print(elements)
            results.append(elements.copy())
            num_reversals += 1
        
        if elements[i] != abs(elements[i]):
            elements[i] = abs(elements[i])
            results.append(elements.copy())
            # print(elements)
        i += 1
    return results

with open('data/week4problem1.txt') as stream:
    r = stream.readline().strip().split(' ')
    elements = [-1*int(l[1:]) if l[0] == '-' else 1*int(l[1:]) for l in r]

# print(elements)
# elements = [5,4,3,2,1]
results = greedy_sort(elements)
print(len(results))

with open('output/week4problem1.txt', 'w') as stream:
    for r in results:
        stream.write(' '.join(['{}'.format(str(n)) if n < 0 else '+{}'.format(str(n)) for n in r]) + '\n')
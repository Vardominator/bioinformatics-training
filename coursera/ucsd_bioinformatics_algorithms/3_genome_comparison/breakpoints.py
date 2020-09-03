def count_breakpoints(elements):
    count = 0
    for i in range(1, len(elements)):
        if elements[i] - elements[i-1] != 1:
            count +=1
    if elements[0] - 0 != 1:
        count += 1
    if elements[-1] - len(elements) + 1 != 1:
        count += 1
    return count

with open('data/week4problem2.txt') as stream:
    r = stream.readline().strip().split(' ')
    elements = [-1*int(l[1:]) if l[0] == '-' else 1*int(l[1:]) for l in r]

print(count_breakpoints(elements))
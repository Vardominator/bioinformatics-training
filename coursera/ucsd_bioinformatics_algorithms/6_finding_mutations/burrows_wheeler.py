text = "ACCAACACTG$"


def bwt(text):
    cycles = []
    for i in range(len(text)):
        cycles.append(text[-i:] + text[:-i])
    cycles.sort()
    return ''.join([c[-1] for c in cycles])

with open('data/dataset_297_5.txt', 'r') as stream:
    text = stream.read().strip()

    with open('output/1.txt', 'w') as stream:
        stream.write(bwt(text))
def convolution(spectrum):
    diffs = {}
    for n in spectrum:
        for l in spectrum:
            d = abs(n - l)
            if d in diffs:
                diffs[d] += 1
            else:
                diffs[d] = 1   
    res = []
    del diffs[0]
    for d in diffs.keys():
        for i in range(diffs[d] // 2):
            res.append(d)
    return res

with open('data/dataset_104_4.txt', 'r') as stream:
    spectrum = [int(s) for s in stream.readline().strip().split(' ')]


print(convolution(spectrum))
# print(' '.join([str(s) for s in res]))

# spectrum = [0, 57, 118, 179, 236, 240, 301]
# diffs = {}
# for n in spectrum:
#     for l in spectrum:
#         d = abs(n - l)
#         if d in diffs:
#             diffs[d] += 1
#         else:
#             diffs[d] = 1

# import operator
# print(diffs)
# print(max(diffs.items(), key=operator.itemgetter(1))[0])
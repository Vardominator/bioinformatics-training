def change(money, coins):
    min_num_coins = [0]*(money + 1)
    for m in range(1, money + 1):
        min_num_coins[m] = 10000000
        for i in range(len(coins)):
            if m >= coins[i]:
                if min_num_coins[m - coins[i]] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - coins[i]] + 1
    print(min_num_coins)
    return min_num_coins[money]

with open('data/week1problem1.txt', 'r') as stream:
    money = int(stream.readline().strip())
    coins = [int(s) for s in stream.readline().strip().split(',')]

print(change(21, [2,3]))


def count(arr, m, N):
    count = [0 for i in range(N + 1)]
    count[0] = 1
    for i in range(1, N + 1):
        for j in range(m):
            if (i >= arr[j]):
                count[i] += count[i - arr[j]]

    return count[N]

arr = [2,3]
print(count(arr, len(arr), 22))
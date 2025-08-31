t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    minimum = a[0]
    for i in range(n):
        minimum = min(a[i], minimum)
    count = 0
    for i in range(n):
        if a[i] == minimum:
            count += 1
    print(n - count)


def minToMax():
    t = int(input())

    while t > 0:
        n = int(input())  # size of array
        a = list(map(int, input().split()))

        minimum = min(a)

        count = a.count(minimum)
        print(n - count)
        t -= 1

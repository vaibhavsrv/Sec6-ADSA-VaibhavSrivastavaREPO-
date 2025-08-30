def arrayLeader():
    n = int(input())
    arr = list(map(int, input().split()))
    leader = []
    for i in range(n):
        if all(arr[i] > arr[j] for j in range(i + 1, n)):
            leader.append(arr[i])
    return leader
print(arrayLeader())

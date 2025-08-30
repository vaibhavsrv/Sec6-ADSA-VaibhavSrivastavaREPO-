def moveZero():
    
    arr = list(map(int , input().split(",")))
    n = len(arr)
    
    insert = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[insert] , arr[i] = arr[i] , arr[insert]
            insert += 1
    return arr
print(moveZero())
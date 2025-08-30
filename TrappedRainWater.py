def trappedRainWater():
    arr = list(map(int, input().split(",")))
    n = len(arr)
    
    left = 0
    right = n - 1
    left_max = arr[left]
    right_max = arr[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, arr[left])
            water += left_max - arr[left]
        else:
            right -= 1
            right_max = max(right_max, arr[right])
            water += right_max - arr[right]
    
    return water
print(trappedRainWater())
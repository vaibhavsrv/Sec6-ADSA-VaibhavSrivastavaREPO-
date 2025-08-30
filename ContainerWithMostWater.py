def container():
    
    arr = list(map(int , input().split(",")))
    left = 0
    right = len(arr) - 1
    
    waterTrapped = 0
    
    while (left < right):
        
        height = min(arr[left] , arr[right])
        water = right - left
        
        area = height * water
        
        waterTrapped = max(waterTrapped ,area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
            
    return waterTrapped

print(container())
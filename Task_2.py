def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
            if upper_bound is None or arr[mid] < upper_bound:
                upper_bound = arr[mid]  
        else:
            upper_bound = arr[mid]
            break

    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)

arr = [1.5, 2.3, 3.4, 4.7, 5.6, 6.8, 8.9]
target = 4.5
print(binary_search(arr, target)) 
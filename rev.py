def reverse_list(arr):
    for i in range(0, len(arr)//2):
        arr[i], arr[-i-1] = arr[-i-1], arr[i]
    return arr
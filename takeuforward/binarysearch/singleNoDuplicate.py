def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    ans = 0
    # XOR all the elements
    for i in range(n):
        ans = ans ^ arr[i]
    return ans

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)
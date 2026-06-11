#Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. Assume the given array does not contain any duplicate numbers.



def searchElement(arr,target):
    """:param arr: List of integers
       :param target: Integer to be searched
       :return: Index of the target if found, else -1
    
    """
    low=0
    high=len(arr) -1
    
    # Binary search algorithm
    # loop until low is less than or equal to high
    while low <= high:
        mid=low + (high - low) // 2
        if arr[mid] == target: # If the middle element is equal to the target, return the index
            return mid
        elif arr[mid] < target: # If the middle element is less than the target, search in the right half
            low = mid + 1
        elif arr[mid] > target: # If the middle element is greater than the target, search in the left half
            high = mid - 1
    return -1

def BinarySearchRecursive(arr,low,high,target):
    if low > high:
        return -1
    
    # Find Middle Index
    mid = (low + high)//2
    
    if (arr[mid] == target):
        return mid
    elif (arr[mid] > target):
        high=mid - 1
        return BinarySearchRecursive(arr,low,high,target)
    elif (arr[mid] < target):
        low=mid + 1
        return BinarySearchRecursive(arr,low,high,target)

if __name__ == "__main__":
    arr=[4,6,7,8,9]
    element=8
    print(searchElement(arr,element))
    print(BinarySearchRecursive(arr,0,len(arr)-1,element))
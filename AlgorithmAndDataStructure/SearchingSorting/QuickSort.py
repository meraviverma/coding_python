def quick_srt(arr):
    if len(arr) < 1:
        return arr

    pivot=arr[len(arr) //2]

    left=[x for x in arr if  x < pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]

    return quick_srt(left) + middle + quick_srt(right)

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
    
def partition(arr,low,high):

    #choose pivot
    pivot=arr[high]

    #Index the smaller element and indicates
    #the right position of pivot found so far
    i = low - 1

    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            swap(arr,i,j)

    swap(arr,i+1,high)
    return i + 1


if __name__=="__main__":
    arr=[3,6,8,10,1,2,1]
    print("Sorted Array Is : ",quick_srt(arr))


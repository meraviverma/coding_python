"""
Selection Sort is a comparison-based sorting algorithm.
It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and
swapping it with the first unsorted element. This process continues until the entire array is sorted.

First we find the smallest element and swap it with the first element. This way we get the smallest
element at its correct position.
Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
We keep doing this until we get all elements moved to correct position.
"""

class Solution:
    def selection_sort(self,arr):
        for i in range(len(arr)):

            #Assume the current position holds the minimum element.
            min_index=i

            #Itertate through the unsorted position to find the actual minimum.
            for j in range(i+1,len(arr)):
                if(arr[j] < arr[min_index]):

                    #update index if minimum is found
                    min_index=j
             #swap. move the smallest element to the correct position
            arr[i],arr[min_index]=arr[min_index],arr[i]

        return arr

    def selection_sort_recursion(self,arr,start=0):

        #Base case: if the start index is at the last element or beyond, return
        if start >= len(arr)-1:
            return

        min_index = start
        #find minimum element in the unsorted portion
        for i in range(start+1,len(arr)):

            if(arr[i]<arr[min_index]):
                min_index=i

        #Swap the minimum element with the element at the start index
        arr[start],arr[min_index]=arr[min_index],arr[start]


        #Recursive sort rest of the array
        self.selection_sort_recursion(arr, start + 1)





if __name__=="__main__":
    arr=[5,9,0,4,7,8]
    print("Original Array",arr)
    obj=Solution()
    sorted_arr=obj.selection_sort_recursion(arr)
    print("Sorted Array",arr)

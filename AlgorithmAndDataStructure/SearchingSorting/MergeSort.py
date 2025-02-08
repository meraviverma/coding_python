class Solution:
    def merge_sort(self,arr):
        if len(arr) > 1:

            ##Find middle of array
            mid=len(arr) // 2

            #Divide the array element into two halves
            left_half=arr[:mid]
            right_half=arr[mid:]

            #sorting the first half
            merge_sort(left_half)

            #sorting the second half
            merge_sort(right_half)

            i=j=k=0
            
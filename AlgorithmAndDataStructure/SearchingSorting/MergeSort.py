class Solution:
    def merge_sort(self,arr):
        if len(arr) > 1:

            ##Find middle of array
            mid=len(arr) // 2

            #Divide the array element into two halves
            left_half=arr[:mid]
            right_half=arr[mid:]

            #sorting the first half
            self.merge_sort(left_half)

            #sorting the second half
            self.merge_sort(right_half)

            i=j=k=0

            #copy the data to temp arrays L[] and R[]
            while i< len(left_half) and j < len(right_half):
                if left_half[i] < right_half[i]:
                    arr[k]=left_half[i]
                    i+=1
                else:
                    arr[k]=right_half[j]
                    j+=1
                k+=1

            #checking if element was left
            while i < len(left_half):
                arr[k]=left_half[i]
                i+=1
                k+=1

            while j < len(right_half):
                arr[k]=right_half[j]
                j+=1
                k+=1

        return arr

if __name__=="__main__":
    obj=Solution()
    arr=[12,11,13,5,6,7]
    print(obj.merge_sort(arr))
# Problem Statement: ou're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x

# Example 1:
# Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
# Result: 4 7
# Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

# Example 2:
# Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 8
# Result: 8 8
# Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
# 3,4,6,7,8,10 {x=5}


from typing import List

class Solution:
        """This class contains the method to find the floor and ceiling of an element in a sorted array"""
        def find_ceil_floor(self,arr:List[int],element):
            """This method takes a sorted array and an element as input and returns the floor and ceiling of the element in the array"""
            low = 0 
            high = len(arr) - 1 # Initialize low and high pointers
            ceil = -1 # Initialize ceil and floor to -1, which will be returned if the element is not found in the array
            floor = -1
            while ( low <= high): # While low is less than or equal to high, we will continue to search for the element in the array
                mid = (low + high ) // 2 # Calculate the mid index
                if ( arr[mid] == element): # If the element is found at the mid index, then we will return the element as both ceil and floor
                    ceil = arr[mid] # If the element is found at the mid index, then we will return the element as both ceil and floor
                    floor = arr[mid]
                    break # If the element is found at the mid index, then we will return the element as both ceil and floor
                elif (arr[mid] < element): # If the element at the mid index is less than the element we are looking for, then we will update the floor to the element at the mid index and move the low pointer to mid + 1
                    floor = arr[mid] # If the element at the mid index is less than the element we are looking for, then we will update the floor to the element at the mid index and move the low pointer to mid + 1
                    low = mid + 1 # If the element at the mid index is less than the element we are looking for, then we will update the floor to the element at the mid index and move the low pointer to mid + 1
                else:
                    ceil = arr[mid] # If the element at the mid index is greater than the element we are looking for, then we will update the ceil to the element at the mid index and move the high pointer to mid - 1
                    high = mid - 1
            return ceil,floor

if __name__=="__main__":
    arr= [3,4,4,7,8,10]
    element = 0
    myobj= Solution()
    ceil,floor = myobj.find_ceil_floor(arr,element)
    print(f"Floor = {floor} And ceiling = {ceil}")
                
                    
                
            
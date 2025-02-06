"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use
O(1)
O(1) additional space.

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

"""
from typing import List
class Solution:
    #Brute Force
    def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

    #BinarySearch
    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []

    def twoSum_twopointer(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []

if __name__=="__main__":
    obj= Solution()
    input=[1,2,3,4]
    target=3
    print(obj.twoSumBruteForce(input,target))
    print(obj.twoSumBinarySearch(input, target))
    print(obj.twoSum_twopointer(input, target))
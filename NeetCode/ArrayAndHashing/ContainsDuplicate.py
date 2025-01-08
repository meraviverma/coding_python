"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

"""

from typing import List
class Solution:
    def hasDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def hasDuplicateSorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def hasDuplicatehashset(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
"""
Time & Space Complexity for brutforce
Time complexity: O(n*2)
Space complexity: O(1)

Time & Space Complexity for HashSet
Time complexity: O(n)
Space complexity: O(n)

"""
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    nums2 = [1, 2, 3, 3]
    obj=Solution()
    print(obj.hasDuplicateSorting(nums))
    print(obj.hasDuplicateBruteForce(nums))
    print(obj.hasDuplicatehashset(nums))

    print(obj.hasDuplicateSorting(nums2))
    print(obj.hasDuplicateBruteForce(nums2))
    print(obj.hasDuplicatehashset(nums2))

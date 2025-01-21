"""
Description
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

It means we have to return two most frequent element in the array.
"""
import heapq
from typing import List
class Solution:
    """
        Time & Space Complexity for Sorting
            Time complexity: O(nlogn)
            Space complexity: O(n)
        """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


    """
    Time & Space Complexity for Sorting
        Time complexity: O(nlogk)
        Space complexity: O(n+k)
    """
    def topKFrequentheapmap(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    """
    Time & Space Complexity for BucketSort
        Time complexity: O(n)
        Space complexity: O(n)
    """
    def topKFrequentbucketsort(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

if __name__=="__main__":
    myobj=Solution()
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(myobj.topKFrequent(nums,k))
    print(myobj.topKFrequentheapmap(nums,k))
    print(myobj.topKFrequentbucketsort(nums, k))
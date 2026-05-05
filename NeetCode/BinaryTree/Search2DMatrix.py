# You are given an m x n 2-D integer array matrix and an integer target.
#
# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

#https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150

# Return true if target exists within matrix or false otherwise.
#
# Can you write a solution that runs in O(log(m * n)) time?

from typing import List
class Solution:
    def searchMatrix(self,matrix: List[List[int]],target:int)->bool:



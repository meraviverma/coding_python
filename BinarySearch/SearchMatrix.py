# Description
# You are given an m x n 2-D integer array matrix and an integer target.
#
# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous
# row.
# Return true if target exists within matrix or false otherwise.
#
# Can you write a solution that runs in O(log(m * n)) time?

from typing import List
def searchMatrix(matrix:List[List[int]],target:int)->bool:
    ROWS,COLS=len(matrix),len(matrix[0])

    l,r = 0,ROWS*COLS - 1
    while l <=r:
        m=l+(r-l)//2
        row,col=m // COLS,m % COLS
        if target > matrix[row][col]:
            l=m+1
        elif target < matrix[row][col]:
            r=m-1
        else:
            return True
    return False

if __name__=="__main__":
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 10
    target1=50
    print(searchMatrix(matrix,target))
    print(searchMatrix(matrix, target1))



"""
Problem Statement: Given two arrays representing children’s green factor and
cookie sizes, the goal is to maximise the number of content children.

Each child i has a greed factor of g[i],
which is the minimum size of a cookie that will make the child content.
Each cookie j has a size of s[j]. If s[j] >= g[j], we can assign cookie j
to child i, making the child content. Each child can only receive one cookie.

Link:
https://takeuforward.org/Greedy/assign-cookies
"""
from typing import List
class Solution:
    # Function to find the maximum
    # number of content children
    def findContentChildren(self,greed: List[int], cookieSize: List[int]) -> int:
        # Get the size of
        # the greed array
        n = len(greed)

        # Get the size of
        # the cookieSize array
        m = len(cookieSize)

        # Sort the greed factors in ascending
        # order to try and satisfy the
        # least greedy children first
        greed.sort()

        # Sort the cookie sizes in ascending
        # order to use the smallest cookies first
        cookieSize.sort()

        # Initialize a pointer for the
        # cookieSize array, starting
        # from the first cookie
        l = 0

        # Initialize a pointer for the
        # greed array, starting from
        # the first child
        r = 0

        # Iterate while there are
        # cookies and children
        # left to consider
        while l < m and r < n:
            # If the current cookie can
            # satisfy the current child's greed
            if greed[r] <= cookieSize[l]:
                # Move to the next child,
                # as the current child is satisfied
                r += 1
            # Always move to the next cookie
            # whether the current child
            # was satisfied or not
            l += 1

        # The value of r at the end of
        # the loop represents the number
        # of children that were satisfied
        return r

if __name__ == "__main__":
    greed = [1, 5, 3, 3, 4]
    cookieSize = [4, 2, 1, 2, 1, 3]

    print("Array Representing Greed: ", end="")
    for g in greed:
        print(g, end=" ")
    print()

    print("Array Representing Cookie Size: ", end="")
    for c in cookieSize:
        print(c, end=" ")
    print()

    obj=Solution()
    ans = obj.findContentChildren(greed, cookieSize)

    print(f"\nNo. of kids assigned cookies {ans}")
class Solution:
    def findPeakElement(self,arr: [int]) -> int:
        n = len(arr)  # Size of the array

        # Edge cases:
        if n == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2

            # If arr[mid] is the peak:
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid

            # If we are in the left:
            if arr[mid] > arr[mid - 1]:
                low = mid + 1

            # If we are in the right:
            # Or, arr[mid] is a common point:
            else:
                high = mid - 1

        # Dummy return statement
        return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    abc = Solution()
    ans = abc.findPeakElement(arr)
    print("The peak is at index:", ans)

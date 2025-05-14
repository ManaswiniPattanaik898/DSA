
from typing import List


class Solution:
    def findClosest(self, arr, k):
        # code here
        left, right = 0, len(arr) - 1
        closest = arr[0]

        while left <= right:
            mid = (left + right) // 2
            current = arr[mid]

            if abs(current - k) < abs(closest - k):
                closest = current
            elif abs(current - k) == abs(closest - k):
                closest = max(closest, current)

            if current < k:
                left = mid + 1
            elif current > k:
                right = mid - 1
            else:
                return current

        return closest

        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findClosest(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
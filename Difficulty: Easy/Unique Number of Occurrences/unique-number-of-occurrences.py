
from typing import List

from collections import Counter
class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        freq=Counter(arr)
        seen_frequencies = set()  # Store unique frequency values
        for count in freq.values():
            if count in seen_frequencies:  # If frequency is already seen, return False
                return False
            seen_frequencies.add(count) 
        return True



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.isFrequencyUnique(n, arr)
        
        result_val = 1 if res else 0
        print(result_val)

        print("~")
# } Driver Code Ends
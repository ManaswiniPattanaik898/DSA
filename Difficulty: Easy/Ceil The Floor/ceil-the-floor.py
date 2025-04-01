#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        floor,ceil=-1,-1
        for num in arr:
            if num<=x:
                floor=max(floor,num)
            if num>=x:
                ceil=min(ceil,num) if ceil!=-1 else num
        return [floor,ceil]
            
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
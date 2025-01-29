
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum=0
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(1,n+1):
            sum+=i
        return sum



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)
        print("~")

# } Driver Code Ends
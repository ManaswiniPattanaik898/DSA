class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        set_arr=set(arr)
        for num in range(A,B+1):
            if num not in set_arr:
                return False
        return True
                    
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':

    t = int(input())
    for _ in range(0, t):
        l = list(map(int, input().split()))
        n = l[0]
        k = l[1]
        y = l[2]
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.check_elements(a, n, k, y)
        if (ans):
            print("True")
        else:
            print("False")
        print("~")

# } Driver Code Ends
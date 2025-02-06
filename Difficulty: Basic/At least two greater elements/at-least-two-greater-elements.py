#User function Template for python3

class Solution:
    def findElements(self,arr):
        # Your code goes here
        lst=[]
        max_val=float('-inf')
        max_val_2=float('-inf')
        for num in arr:
            if max_val<num:
                max_val_2=max_val
                max_val=num
            elif max_val_2<num<max_val:
                max_val_2=num
        lst=sorted([i for i in arr if i!=max_val and i!=max_val_2])
        return lst
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(*ob.findElements(arr))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
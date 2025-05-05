#User function Template for python3
class Solution:
    def minAnd2ndMin(self, arr):
        #code here
        if len(arr)<2:
            return (-1,)
        first=second=float('inf')
        for num in arr:
            if num<first:
                second=first
                first=num
            elif first<num<second:
                second=num
        if second==float('inf'):
            return (-1,)
        
        return (first,second)
        
        
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        product = obj.minAnd2ndMin(arr)
        if product[0] == -1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
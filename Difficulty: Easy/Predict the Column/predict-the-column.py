#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here 
        max_zeros = 0
        result_col = -1

        for col in range(N):
            count_zeros = 0
            for row in range(N):
                if arr[row][col] == 0:
                    count_zeros += 1

            if count_zeros > max_zeros:
                max_zeros = count_zeros
                result_col = col

        if max_zeros == 0:
            return -1
        return result_col


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


        print("~")
# } Driver Code Ends
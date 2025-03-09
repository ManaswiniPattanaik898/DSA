#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        arr.sort()
        i,j=0,len(arr)-1
        lst=[]
        while i<j:
            summ=arr[i]+arr[j]
            if summ==0:
                lst.append([arr[i],arr[j]])
                i+=1
                j-=1
                while i < j and arr[i] == arr[i - 1]:
                    i += 1
                while i < j and arr[j] == arr[j + 1]:
                    j -= 1
            elif summ < 0:
                i += 1
            else:
                j -= 1
        return lst
                    
            


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.getPairs(arr)
        if len(res) == 0:
            print()
        else:
            IntMatrix().Print(res)
        print("~")
# } Driver Code Ends
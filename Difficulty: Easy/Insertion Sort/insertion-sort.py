#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        #code here
        n=len(arr)
        for current in range(1,n):
            currentCard=arr[current]
            correctPosition=current-1
            while correctPosition>=0:
                if arr[correctPosition]<currentCard:
                    break
                else:
                    arr[correctPosition+1]=arr[correctPosition]
                    correctPosition-=1
            arr[correctPosition+1]=currentCard
        return arr


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.insertionSort(arr)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends
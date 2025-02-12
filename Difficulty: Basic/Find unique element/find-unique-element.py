from collections import Counter
class Solution:
    def find_unique(self, k, arr):
        #code here
        freq=Counter(arr)
        for i in arr:
            if freq[i]==1:
                return i


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())
    for _ in range(t):
        k = int(input().strip())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        print(solution.find_unique(k, arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
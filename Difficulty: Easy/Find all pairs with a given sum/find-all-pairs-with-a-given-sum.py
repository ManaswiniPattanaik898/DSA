#User function Template for python3
from collections import defaultdict
class Solution:
    def allPairs(self, target, arr1, arr2):
        
        # Your code goes here 
        freq_map = defaultdict(int)
        for num in arr2:
            freq_map[num] += 1

        # Step 2: Find all valid pairs
        result = []
        for num in arr1:
            complement = target - num
            if complement in freq_map:
                for _ in range(freq_map[complement]):
                    result.append((num, complement))

        # Step 3: Sort by first element (u), then second (v) if needed
        result.sort()

        return result
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        arr1 = [int(x) for x in input().strip().split()]
        arr2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        answer = ob.allPairs(x, arr1, arr2)
        sz = len(answer)

        if sz == 0:
            print(-1)

        else:

            for i in range(sz):
                if i == sz - 1:
                    print(*answer[i])
                else:
                    print(*answer[i], end=', ')

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
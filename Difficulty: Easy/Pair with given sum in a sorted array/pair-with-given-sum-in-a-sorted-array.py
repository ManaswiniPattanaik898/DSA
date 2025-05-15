#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        n = len(arr)
        i, j = 0, n - 1
        count = 0

        while i < j:
            s = arr[i] + arr[j]

            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                if arr[i] == arr[j]:
                    total = j - i + 1
                    count += total * (total - 1) // 2
                    break
                else:
                    count_i = 1
                    count_j = 1
                    while i + 1 < j and arr[i] == arr[i + 1]:
                        count_i += 1
                        i += 1
                    while j - 1 > i and arr[j] == arr[j - 1]:
                        count_j += 1
                        j -= 1
                    count += count_i * count_j
                    i += 1
                    j -= 1

        return count





#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
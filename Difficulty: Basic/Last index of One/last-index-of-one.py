#User function Template for python3

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        if '1' not in s:
            return -1
        else:
            return s.rindex('1')

        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        s = input()
        ob = Solution()
        print(ob.lastIndex(s))

        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
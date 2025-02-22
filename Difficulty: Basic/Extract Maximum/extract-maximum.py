#User function Template for python3

class Solution:
    def extractMaximum(self,S): 
        max_num=-1
        current_num=0
        found_digit=False
        
        for char in S:
            if char.isdigit():
                current_num=current_num*10+int(char)
                found_digit=True
            else:
                max_num=max(max_num,current_num)
                current_num=0
        max_num=max(max_num,current_num)
        return max_num if found_digit else -1
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        print(ob.extractMaximum(S)) 

        print("~")
# } Driver Code Ends
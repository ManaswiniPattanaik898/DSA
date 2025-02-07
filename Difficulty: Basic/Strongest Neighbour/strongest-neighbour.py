#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to find maximum for every adjacent pairs in the array.
def maximumAdjacent(sizeOfArray, arr):
    
    
    # Your code here
    # Function should print max of all adjacents
    for i in range(sizeOfArray-1):
        print(max(arr[i],arr[i+1]),end=" ")
    
    

#{ 
 # Driver Code Starts.
    
# Driver Code
def main():
    
    # testcase input
    testcases = int(input())
    
    # looping through all testcases
    while testcases > 0:
        
        sizeOfArray = int(input())
        
        arr = [int(x) for x in input().split()]
        
        maximumAdjacent(sizeOfArray, arr)
        
        print()
        
        testcases -= 1

        print("~")
if __name__ == '__main__':
    main()
    
    
# } Driver Code Ends
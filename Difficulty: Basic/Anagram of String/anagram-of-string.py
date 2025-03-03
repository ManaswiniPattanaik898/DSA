# function to calculate minimum numbers of characters
# to be removed to make two strings anagram

def remAnagram(s1,s2):
    s1_s=sorted(s1)
    s2_s=sorted(s2)
    i,j=0,0
    count=0
    
    while i < len(s1_s) and j < len(s2_s):
        if s1_s[i]==s2_s[j]:
            count+=1
            i+=1
            j+=1
        elif s1_s[i]<s2_s[j]:
            i+=1
        else:
            j+=1
    return (len(s1)-count)+(len(s2)-count)
    
    
    #add code here
    
    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        str2 = input()
        print(remAnagram(str1, str2))
        print("~")

# } Driver Code Ends
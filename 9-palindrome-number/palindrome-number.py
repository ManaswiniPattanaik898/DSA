def rev_no(x):
    temp=x
    rev_no=0
    for i in range(len(str(x))):
        last_dig=temp%10
        rev_no=rev_no*10+last_dig
        temp=temp//10
    return rev_no


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x==rev_no(x)




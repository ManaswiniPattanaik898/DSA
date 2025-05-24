class Solution:
    def sumSubstrings(self,s):
        # code here
        n = len(s)
        total_sum = 0
        prev_sum = 0

        for i in range(n):
            digit = int(s[i])
            curr_sum = prev_sum * 10 + digit * (i + 1)
            total_sum += curr_sum
            prev_sum = curr_sum

        return total_sum
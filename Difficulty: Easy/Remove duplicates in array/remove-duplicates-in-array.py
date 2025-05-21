class Solution:
    def removeDuplicates(self, arr):
        # code here 
        seen=set()
        result=[]
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result
        
    
class Solution:    
    def ValidCorner(self,mat): 
        # Code here 
        n = len(mat)
        m = len(mat[0])
    
    # Dictionary: key = (col1, col2), value = row where this pair occurred
        seen_pairs = {}
    
        for i in range(n):
        # Find all column indices with 1 in current row
            ones = [j for j in range(m) if mat[i][j] == 1]
        
        # Check all pairs of 1s in the current row
            for a in range(len(ones)):
                for b in range(a + 1, len(ones)):
                    c1, c2 = ones[a], ones[b]
                    if (c1, c2) in seen_pairs:
                    # A previous row also had 1s in same columns
                        return True
                    seen_pairs[(c1, c2)] = i
    
        return False
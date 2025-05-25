class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	n = len(arr)
        squared = [x * x for x in arr]
        squares_set = set(squared)

        for i in range(n):
            for j in range(i + 1, n):
                sum_squares = squared[i] + squared[j]
                if sum_squares in squares_set:
                # Ensure the triplet uses 3 different indices
                    if sum_squares != squared[i] and sum_squares != squared[j]:
                        return True
                # Or check frequency in original array if numbers are repeated
                    if squared.count(sum_squares) > 1:
                        return True
        return False

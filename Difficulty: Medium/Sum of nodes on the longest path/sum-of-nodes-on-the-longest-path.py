'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
          # Initialize variables to track the maximum path length and its corresponding sum
        self.max_sum = 0
        self.max_len = 0

        def dfs(node, current_sum, current_len):
            if not node:
                return

            # Update current sum and length
            current_sum += node.data
            current_len += 1

            # If it's a leaf node
            if not node.left and not node.right:
                # Check if this path is the longest or has the maximum sum among longest paths
                if current_len > self.max_len:
                    self.max_len = current_len
                    self.max_sum = current_sum
                elif current_len == self.max_len:
                    self.max_sum = max(self.max_sum, current_sum)
                return

            # Recurse to left and right children
            dfs(node.left, current_sum, current_len)
            dfs(node.right, current_sum, current_len)

        # Start DFS from root
        dfs(root, 0, 0)
        return self.max_sum
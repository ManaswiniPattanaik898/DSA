class Solution:
	def leafNodes(self, preorder):
		# code here
		stack = []
        leaf_nodes = []
        n = len(preorder)

        for i in range(n - 1):
            found = False
            if preorder[i + 1] < preorder[i]:
                stack.append(preorder[i])
            else:
                while stack and preorder[i + 1] > stack[-1]:
                    stack.pop()
                    found = True
                if found:
                    leaf_nodes.append(preorder[i])

        leaf_nodes.append(preorder[-1])
        return leaf_nodes

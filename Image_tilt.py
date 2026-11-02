
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.t=0
        def dfs(node):
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            self.t+=abs(l-r)
            return l+r+node.val
        dfs(root)
        return self.t

        

from collections import deque

def deserialize(self, data):
    vals = deque(data.split(','))
    
    def dfs():
        val = vals.popleft()
        if val == 'N':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    
    return dfs()

def serialize(root):
    res = []
    def dfs(node):
        if not node:
            res.append('N')
            return
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ','.join(res)

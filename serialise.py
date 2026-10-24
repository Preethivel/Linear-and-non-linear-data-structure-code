def serialize(node):
    res=[]
    def dfs(root)
        if not root:
            res.append('N')
            return
        res.append(str(root.val))
        dfs(root.left)
        dfs(root.right)
    dfs(node)
    return ','.join(res)

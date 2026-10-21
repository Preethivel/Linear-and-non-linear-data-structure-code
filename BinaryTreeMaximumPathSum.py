def BinaryTreeMaximumPathSum(root):
  res=float('-inf')
  def dfs(node):
    nonlocal res
    if not node:
      return 0
    l=max(dfs(node.left),0)
    r=max(dfs(node.right),0)
    res=max(res,node.val+l+r)
    return node.val+max(l,r)
  dfs(root)
  return res
  

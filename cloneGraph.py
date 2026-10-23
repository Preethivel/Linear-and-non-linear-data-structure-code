def cloneGraph(root):
  if not root:
    return None
  visited={}
  def dfs(node):
    if node in visited:
      return visited[node]
    clone=Node(node.val)
    visited[node]=clone
    for n in node.neighbors:
      clone.neighbors.append(dfs(n))
    return clone
  return dfs(root)


  
        

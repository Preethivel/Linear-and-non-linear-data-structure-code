from collections import deque
def levelorder (root) :
  if not root:
    return None
  q=deque ( [root] )
  res=[]
  while q:
    1=1en (q)
    k=[]
    for i in range(1) :
      node=q.popleft()
      k. append (node.val)
      if node.left:
        q. append (node . left)
      if node.right:
        q. append (node. right)
    res.append (1)
  return res

class Node:
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right=None
class BinaryTree:
  def __init__(self):
    self.root=None
  def insert(self,val):
    newNode=Node(val)
    if self.root is None:
      self.root=newNode
      return
    queue=deque([self.root])
    while queue:
      node=queue.popleft()
      if node.left is None:
        node.left=newNode
        return
      else:
        queue.append(node.left)
      if node.right is None:
        node.right=newNode
        return
      else:
        queue.append(node.left)
  def search(self,val):
    return self._search(self.root,val)
  def _search(self,node,val):
    if node is None:
      return False
    if node.val==val:
      return True
    return self._search(node.left,val) or self._search(node.right,val)
  def height(self):
    return self._height(self.root)
  def _height(self,node):
    if not self.root is None:return 1+max(self._height(self.root),self._height(root.right))
  def contu(self):
    return self._cnt(self.root)
  def _height(self,node):
    if not self.root is None:return 1+seelf._cnt(self.root),self._cnt(root.right))
      
  
  

def FromPostorderAndInorderToTree(postorder,inorder):
  if not postorder:
    return None
  root_val=postorder[-1]
  root=TreeNode(root_val)
  mid=inorder.index(root_val)
  root.left=FromPreorderAndInorderToTree(postorer[:mid],inorder[:mid])
  root.right=FromPreorderAndInorderToTree(postorder[mid:-1],inorder[mid+1:])
  return root

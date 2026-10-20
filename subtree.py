def isSubtree(root, subRoot):
    def serialize(node):
        if not node:
            return "#null"
        return f"#{node.val}{serialize(node.left)}{serialize(node.right)}"
    
    return serialize(subRoot) in serialize(root)

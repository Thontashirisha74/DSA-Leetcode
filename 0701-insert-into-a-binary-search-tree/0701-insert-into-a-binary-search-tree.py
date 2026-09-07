class Solution:
    def insertIntoBST(self, root, val):
        
        # If tree is empty
        if root is None:
            return TreeNode(val)
        
        current = root
        
        while True:
            
            if val < current.val:
                
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                
                current = current.left
            
            else:
                
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                
                current = current.right
        
        return root
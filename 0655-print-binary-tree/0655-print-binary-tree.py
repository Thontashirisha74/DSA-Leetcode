class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # Find height
        def get_height(node):
            if not node:
                return -1

            return 1 + max(get_height(node.left),
                           get_height(node.right))

        height = get_height(root)

        rows = height + 1
        cols = 2 ** (height + 1) - 1

        res = [[""] * cols for _ in range(rows)]

        def fill(node, row, col):
            if not node:
                return

            res[row][col] = str(node.val)

            if node.left:
                left_col = col - 2 ** (height - row - 1)
                fill(node.left, row + 1, left_col)

            if node.right:
                right_col = col + 2 ** (height - row - 1)
                fill(node.right, row + 1, right_col)

        fill(root, 0, (cols - 1) // 2)

        return res
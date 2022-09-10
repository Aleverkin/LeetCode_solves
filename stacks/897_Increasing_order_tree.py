def increasingBST(self, root: TreeNode) -> TreeNode:
    def recurse_create_stack(root):
        stack = [root]

        stack_left = [] if root.right is None else recurse_create_stack(root.right)
        stack_right = [] if root.left is None else recurse_create_stack(root.left)

        return stack_left + stack + stack_right

    stack = recurse_create_stack(root)

    new_root = stack.pop(-1)
    node = new_root
    while len(stack) > 0:
        node.left = None
        node.right = stack.pop(-1)
        node = node.right

    node.left = None
    node.right = None

    return new_root
def postorder(self, root: 'Node') -> List[int]:
    def create_stack(root):
        stack = []
        stack.append(root.val)

        for child in root.children[::-1]:
            stack += create_stack(child)

        return stack

    if root is not None:
        stack = create_stack(root)
    else:
        stack = []
    return stack[::-1]
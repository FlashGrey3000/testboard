class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_node(self, node: TreeNode):
        if node.val >= self.val:
            if self.right is not None:
                self.right.add_node(node)
            else:
                self.right = node
        else:
            if self.left is not None:
                self.left.add_node(node)
            else:
                self.left = node
    
    def print_tree(self):
        queue = [self]

        while (len(queue) != 0):
            curr = queue.pop(0)
            print(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


if __name__ == '__main__':
    root = TreeNode(10)
    
    root.add_node(TreeNode(7))
    root.add_node(TreeNode(8))
    root.add_node(TreeNode(9))
    root.add_node(TreeNode(11))
    root.add_node(TreeNode(12))
    root.add_node(TreeNode(5))

    root.print_tree()
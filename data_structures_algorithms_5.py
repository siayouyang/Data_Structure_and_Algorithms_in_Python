#05 binary tree - encapsulation

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    #parse tuple
    @staticmethod
    def tuple_to_tree(tree_tuple):
        if isinstance(tree_tuple, tuple) == True:   #and len(tree_tuple) == 3:
            node = TreeNode(tree_tuple[1])
            node.left = TreeNode.tuple_to_tree(tree_tuple[0])
            node.right = TreeNode.tuple_to_tree(tree_tuple[2])
        elif tree_tuple is None:
            node = None
        else:
            node = TreeNode(tree_tuple)
        return node


    def tree_to_tuple(self):
        tuple = ()
        if self.left is None and self.right is None:
            left = self.key
            return left
        elif self.left is None and (self.right is None) == False:
            left = None
        else:
            left = TreeNode.tree_to_tuple(self.left)

        mid = self.key

        if self.right is None and self.left is None:
            right = self.key
            return right
        elif self.right is None and (self.left is None) == False:
            right = None
        else:
            right = TreeNode.tree_to_tuple(self.right)

        tuple += (left, mid, right)
        return tuple

    def __repr__(self):
        return f"{self.tree_to_tuple()}"

    def __str__(self):
        return self.__repr__()
        #return f"{self.tree_to_tuple()}"


            # visualizing tree 90 degree rotated
    def visualize_tree(self, space='\t', level=0):
        if self == None:
            print(space * level + f'o')
            return

        if self.right is None and self.left is None:
            print(space * level + f'{self.key}')
            return

        TreeNode.visualize_tree(self.right, '\t', level + 1)
        print(space * level + f'{self.key}')
        TreeNode.visualize_tree(self.left, '\t', level + 1)

    # inorder traversal(left subtree) (left, root, right)
    def inorder_traversal_left(self):
        if self is None:
            return []
        return TreeNode.inorder_traversal_left(self.left) + [self.key] + TreeNode.inorder_traversal_left(self.right)


    #preorder traversal (root, left, right)
    def preorder_traversal(self):
        if self is None:
            return []
        return [self.key] + TreeNode.preorder_traversal(self.left) + TreeNode.preorder_traversal(self.right)

    # inorder traversal(right subtree)
    def inorder_traversal_right(self):
        if self is None:
            return []
        return TreeNode.inorder_traversal_right(self.right) + [self.key] +TreeNode.inorder_traversal_right(self.left)

    # postorder traversal (left, right, root)
    def postorder_traversal(self):
        if self is None:
            return []
        return TreeNode.postorder_traversal(self.left) + TreeNode.postorder_traversal(self.right) + [self.key]

    # tree height
    def tree_height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height(self.left), TreeNode.tree_height(self.right))

    # tree size
    def tree_size(self):
        if self is None:
            return 0
        return 1 + TreeNode.tree_size(self.left) + TreeNode.tree_size(self.right)

if __name__ == "__main__":
    tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

    tree = TreeNode.tuple_to_tree(tree_tuple)
    print(tree.key, tree.left.key, tree.right.key, tree.left.left.key, tree.left.right)

    tree_tuple2 = TreeNode.tree_to_tuple(tree)
    print(tree_tuple2)
    print(tree_tuple)

    TreeNode.visualize_tree(tree)

    print(TreeNode.inorder_traversal_left(tree))

    print(TreeNode.preorder_traversal(tree))

    print(TreeNode.inorder_traversal_right(tree))

    print(TreeNode.postorder_traversal(tree))

    print(TreeNode.tree_height(tree))

    print(TreeNode.tree_size(tree))

    print(tree)
#04 binary tree

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#parse tuple
def tuple_to_tree(tree_tuple):
    if isinstance(tree_tuple, tuple) == True:   #and len(tree_tuple) == 3:
        node = TreeNode(tree_tuple[1])
        node.left = tuple_to_tree(tree_tuple[0])
        node.right = tuple_to_tree(tree_tuple[2])
    elif tree_tuple is None:
        node = None
    else:
        node = TreeNode(tree_tuple)
    return node


tree = tuple_to_tree(tree_tuple)
print(tree.key, tree.left.key, tree.right.key, tree.left.left.key, tree.left.right)

def tree_to_tuple(tree):
    tuple = ()
    if tree.left is None and tree.right is None:
        left = tree.key
        return left
    elif tree.left is None and (tree.right is None) == False:
        left = None
    else:
        left = tree_to_tuple(tree.left)

    mid = tree.key

    if tree.right is None and tree.left is None:
        right = tree.key
        return right
    elif tree.right is None and (tree.left is None) == False:
        right = None
    else:
        right = tree_to_tuple(tree.right)

    tuple += (left, mid, right)
    return tuple


tree_tuple2 = tree_to_tuple(tree)
print(tree_tuple2)
print(tree_tuple)

#visualizing tree 90 degree rotated
def visualize_tree(tree, space='\t', level = 0):
    if tree == None:
        print(space * level + f'o')
        return

    if tree.right is None and tree.left is None:
        print(space*level + f'{tree.key}')
        return

    visualize_tree(tree.right, '\t', level + 1)
    print(space * level + f'{tree.key}')
    visualize_tree(tree.left, '\t', level + 1)


visualize_tree(tree)

#inorder traversal(left subtree) (left, root, right)
def inorder_traversal_left(tree):
    if tree is None:
        return []
    return inorder_traversal_left(tree.left) + [tree.key] + inorder_traversal_left(tree.right)

print(inorder_traversal_left(tree))

#preorder traversal (root, left, right)
def preorder_traversal(tree):
    if tree is None:
        return []
    return [tree.key] + preorder_traversal(tree.left) + preorder_traversal(tree.right)

print(preorder_traversal(tree))

#inorder traversal(right subtree)
def inorder_traversal_right(tree):
    if tree is None:
        return []
    return inorder_traversal_right(tree.right) + [tree.key] + inorder_traversal_right(tree.left)

print(inorder_traversal_right(tree))

#postorder traversal (left, right, root)
def postorder_traversal(tree):
    if tree is None:
        return []
    return postorder_traversal(tree.left) + postorder_traversal(tree.right) + [tree.key]

print(postorder_traversal(tree))

#tree height
def tree_height(tree):
    if tree is None:
        return 0
    return 1 +  max(tree_height(tree.left) , tree_height(tree.right))

print(tree_height(tree))

#tree size
def tree_size(tree):
    if tree is None:
        return 0
    return 1 + tree_size(tree.left) + tree_size(tree.right)

print(tree_size(tree))
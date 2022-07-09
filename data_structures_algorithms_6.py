#06 binary search tree(bst)

########################
#import
from data_structures_algorithms_5 import TreeNode

tree_tuple = (('aakash','biraj','hemanth'),'jadhesh',('siddhant','sonaksh','vishal'))
tree = TreeNode.tuple_to_tree(tree_tuple)
print(tree)

def remove_none(list):
    return [i for i in list if i is not None]

def is_bst(tree):
    if tree is None:
        return True, None, None

    node_is_bst_left, min_left, max_left = is_bst(tree.left)
    node_is_bst_right, min_right, max_right = is_bst(tree.right)

    node_is_bst = (node_is_bst_left == True) and (node_is_bst_left == True) and\
                  (max_left is None or max_left <= tree.key) and (min_right is None or min_right > tree.key)
    min_key = min(remove_none([min_left, tree.key, min_right]))
    max_key = max(remove_none([max_left, tree.key, max_right]))

    return node_is_bst, min_key, max_key

print(is_bst(tree))

###############
from data_structures_algorithms_3 import User

aakash = User(user_name = 'aakash', name = 'aakash', email = 'aakash@gmail.com')
biraj = User(user_name = 'biraj', name = 'biraj', email = 'biraj@gmail.com')
hemanth = User(user_name = 'hemanth', name = 'hemanth', email = 'hemanth@gmail.com')
jadhesh = User(user_name = 'jadhesh', name = 'jadhesh', email = 'jadhesh@gmail.com')
siddhant = User(user_name = 'siddhant', name = 'siddhant', email = 'siddhant@gmail.com')
sonaksh = User(user_name = 'sonaksh', name = 'sonaksh', email = 'sonaksh@gmail.com')
vishal = User(user_name = 'vishal', name = 'vishal', email = 'vishal@gmail.com')

class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return self.__repr__()

#level 0
bst_node = BSTNode(jadhesh.user_name, jadhesh)
#level 1
bst_node.left = BSTNode(biraj.user_name, biraj)
bst_node.left.parent = bst_node
bst_node.right = BSTNode(sonaksh.user_name, sonaksh)
bst_node.right.parent = bst_node
#level 2
bst_node.left.left =BSTNode(aakash.user_name, aakash)
bst_node.left.left.parent = bst_node.left
bst_node.left.right =BSTNode(hemanth.user_name, hemanth)
bst_node.left.right.parent = bst_node.left
#
bst_node.right.left =BSTNode(siddhant.user_name, siddhant)
bst_node.right.left.parent = bst_node.right
bst_node.right.right =BSTNode(vishal.user_name, vishal)
bst_node.right.right.parent = bst_node.right
#
print(TreeNode.tree_to_tuple(bst_node))
print(bst_node.right.left.value)
TreeNode.visualize_tree(bst_node)

####################
#insert
def bst_insert(bst, key, value):
    if bst is None:
        bst = BSTNode(key, value)
    elif key <= bst.key:
        bst.left = bst_insert(bst.left, key, value)
        bst.left.parent = bst
    elif key > bst.key:
        bst.right = bst_insert(bst.right, key, value)
        bst.right.parent = bst
    return bst

import copy
bst_node2 = copy.deepcopy(bst_node)
tamil = User(user_name = 'tamil', name = 'tamil', email = 'tamil@gmail.com')

bst_node2 = bst_insert(bst_node2, tamil.user_name, tamil)
TreeNode.visualize_tree(bst_node2)

#find
def find(bst, key):
    if bst is None:
        node = None
    elif bst.key == key:
        node = bst
    elif key <= bst.key:
        node = find(bst.left, key)
    elif key > bst.key:
        node = find(bst.right, key)
    return node

print(find(bst_node2, 'tamil'))
print(find(bst_node2, 'cina')) #None
print(find(bst_node2, 'biraj'))

#update
def update(bst, key, value):
    node = find(bst, key)
    if node is not None:
        node.value = value

biraj2 = User(user_name = 'biraj', name = 'biraj2', email = 'biraj2@gmail.com')
update(bst_node2, 'biraj', biraj2)
print(find(bst_node2, 'biraj'))

#list_all
def list_all(bst):
    if bst is None:
        return []
    return list_all(bst.left) + [bst] +list_all(bst.right)
print(list_all(bst_node))

#balanced binary search tree?
def is_balanced(bst):
    if bst is None:
        return True, 0
    balanced_l, height_l = is_balanced(bst.left)
    balanced_r, height_r = is_balanced(bst.right)

    balanced = (balanced_l) and (balanced_r) and\
               (abs(height_l-height_r) <= 1)

    height = max([height_l, height_r]) + 1

    return balanced, height

print(is_balanced(bst_node))
print(is_balanced(bst_node2))
TreeNode.visualize_tree(bst_node)
TreeNode.visualize_tree(bst_node2)

################################
#make balanced bst
sorted_list = list_all(bst_node)
print(sorted_list)

#node1 = BSTNode(sorted_list[0].key, sorted_list[0])
#print(node1.key, node1.value)

def make_balanced_bst(sorted_list, lo=0, hi=None, parent = None):
    if hi is None:
        hi = len(sorted_list)-1
    if hi < lo:
        return None

    mid = (lo + hi)//2
    bst_node = BSTNode(sorted_list[mid].key, sorted_list[mid])
    bst_node.parent = parent

    bst_node.left = make_balanced_bst(sorted_list, lo=lo, hi=(mid-1), parent = bst_node)
    bst_node.right = make_balanced_bst(sorted_list, lo=(mid+1), hi=hi, parent = bst_node)

    return bst_node

balanced_node = make_balanced_bst(sorted_list)
TreeNode.visualize_tree(balanced_node)

#balance an unbalanced bst
def balance_bst(bst):
    list = list_all(bst)
    return make_balanced_bst(list)

balanced_node2 = balance_bst(bst_node2)
TreeNode.visualize_tree(bst_node2)
TreeNode.visualize_tree(balanced_node2)
print(find(balanced_node2,'tamil'))
print(find(balanced_node2,'tamil').parent)
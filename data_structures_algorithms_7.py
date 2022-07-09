#07 binary search tree(bst)
#create a generic class
########################
from data_structures_algorithms_5 import TreeNode

tree_tuple = (('aakash','biraj','hemanth'),'jadhesh',('siddhant','sonaksh','vishal'))
tree = TreeNode.tuple_to_tree(tree_tuple)


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


###############
from data_structures_algorithms_3 import User

aakash = User(user_name = 'aakash', name = 'aakash', email = 'aakash@gmail.com')
biraj = User(user_name = 'biraj', name = 'biraj', email = 'biraj@gmail.com')
hemanth = User(user_name = 'hemanth', name = 'hemanth', email = 'hemanth@gmail.com')
jadhesh = User(user_name = 'jadhesh', name = 'jadhesh', email = 'jadhesh@gmail.com')
siddhant = User(user_name = 'siddhant', name = 'siddhant', email = 'siddhant@gmail.com')
sonaksh = User(user_name = 'sonaksh', name = 'sonaksh', email = 'sonaksh@gmail.com')
vishal = User(user_name = 'vishal', name = 'vishal', email = 'vishal@gmail.com')
tamil = User(user_name = 'tamil', name = 'tamil', email = 'tamil@gmail.com')

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


#insert
def insert(bst, key, value):
    if bst is None:
        bst = BSTNode(key, value)
    elif key <= bst.key:
        bst.left = insert(bst.left, key, value)
        bst.left.parent = bst
    elif key > bst.key:
        bst.right = insert(bst.right, key, value)
        bst.right.parent = bst
    return bst


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


#update
def update(bst, key, value):
    node = find(bst, key)
    if node is not None:
        node.value = value


#list_all
def list_all(bst):
    if bst is None:
        return []
    return list_all(bst.left) + [bst] +list_all(bst.right)


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

#make balanced bst
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


#balance an unbalanced bst
def balance_bst(bst):
    list = list_all(bst)
    return make_balanced_bst(list)

#generic class
class TreeMap:
    def __init__(self):
        self.node = None

    def __setitem__(self, key, value):
        if find(self.node, key) is None:
            self.node = insert(self.node, key, value)
            self.node = balance_bst(self.node)
        else:
            update(self.node,key, value)

    def __getitem__(self, item):
        return find(self.node, item)

    def __iter__(self):
        return (i for  i in list_all(self.node))

    def __len__(self):
        return TreeNode.tree_size(self.node)

    def display(self):
        return TreeNode.visualize_tree(self.node)


if __name__ == "__main__":
    tree_map_node = TreeMap()
    tree_map_node['aakash'] = aakash
    tree_map_node['jadhesh'] = jadhesh
    tree_map_node['sonaksh'] = sonaksh
    tree_map_node['biraj'] = biraj
    tree_map_node['siddhant'] = siddhant
    tree_map_node['tamil'] = tamil
    tree_map_node['hemanth'] = hemanth
    tree_map_node['sonaksh'] = sonaksh #repeated
    tree_map_node['vishal'] = vishal
    tree_map_node.display()
    print(tree_map_node['sonaksh'])
    for i in tree_map_node:
        print(i)
    print(len(tree_map_node))


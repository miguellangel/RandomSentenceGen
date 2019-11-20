"""File:               TestBinaryTree.py
    Description:        Binary Tree ops
    Student Name:       Miguel Arriaga
    Student UT EID:     maa5798
    Partner Name:       Sommer Chavez
    Partner UT EID:     ssc2364
    Course Name:        CS 313E
    Unique Number:      51350
    Date Created:       11/14/2018
    Date Last Modified: 11/16/2018 """


class Node(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def __str__(self):
        return str(self.data)
    def __int__(self):
        return int(self.data)
    def __eq__(self, other):
        return self.data == other
    def __le__(self, other):
        return self.data <= other
    def __ge__(self, other):
        return self.data >= other
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other


class Tree(object):
    def __init__(self):
        self.root = None
        self.num_lnodes = 0
        self.num_rnodes = 0
        self.num_nodes_ = 0

    def insert(self, data):
        new_node = Node(data)
        if (self.has_duplicates(data)) == False:     # makes sure that duplicates are not inserted
            if self.root == None:  # if the tree is empty
                self.root = new_node
            else:
                current = self.root  # copy of the root, current
                if new_node > current:
                    self.num_rnodes += 1
                else:
                    self.num_lnodes += 1
                parent = self.root  # copy of the parent node, previous
                while current != None:
                    parent = current

                    if data < current.data:
                        current = current.left
                    else:
                        current = current.right
                if data < parent.data:
                    parent.left = new_node
                else:
                    parent.right = new_node

            self.num_nodes_ += 1

    def has_duplicates(self, ch):   # checks if ch has already been inserted into tree. returns bool
        start = self.root
        current = start

        while current != None and current.data != ch:  # loop runs until we find data

            if ch > current.data:
                current = current.right

            elif ch < current.data:
                current = current.left

        if current == None:
            return False
        else:
            return True

    def is_similar_helper(self, tree1_node, tree2_node):
        if (tree1_node == None) and (tree2_node == None):   # if both nodes are empty, that means they are the same
            return True

        elif (tree1_node.data != tree2_node.data):    # returns False at first instance where actual node values are unequal
            return False

        elif (tree1_node != None) and (tree2_node != None): # while both nodes do not equal None
            return self.is_similar_helper(tree1_node.left, tree2_node.left) and self.is_similar_helper(tree1_node.right, tree2_node.right)
        else:
            return False

    # Returns true if two binary trees are similar
    def is_similar(self, other):
        return self.is_similar_helper(self.root, other.root)

    def print_level_helper(self, node, current_level, abs_level, str_level):
        if (node == None):  # if node is empty return nothing
            return

        if current_level == abs_level:  # check if current level is desired level
            str_level.append(str(node.data))    # save the node data in list

        elif current_level < abs_level:  # keeps running while less than desired level
            self.print_level_helper(node.left, current_level + 1, abs_level, str_level) # checks left branches
            self.print_level_helper(node.right, current_level + 1, abs_level, str_level)    # checks right branches

    def print_level(self, level):
        str_level = []  # holds values
        current_level = 1   # starting level
        self.print_level_helper(self.root, current_level, level, str_level) # actual
        return ' '.join(str_level)

    # Returns the height of the tree
    def get_height_helper(self, node):
        if node == None:    # if starting value is None, height is 0
            return 0
        else:   # choose the larger of the two and keep increasing counter by 1
            return (self.get_height_helper(node.left) and self.get_height_helper(node.right)) + 1

    def get_height(self):
        return self.get_height_helper(node = self.root)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes_traverse(self, node, num_nodes):    # use traversal to count num of nodes instead of printing
        if node != None:
            self.num_nodes_traverse(node.left, num_nodes)
            num_nodes[0] = num_nodes[0] + 1
            self.num_nodes_traverse(node.right, num_nodes)

    def num_nodes(self):
        num_nodes = [0]
        self.num_nodes_traverse(self.root, num_nodes)
        return num_nodes[0]

def main():
    # Create three trees - two are the same and the third is different
    tree1 = Tree()
    letters = ["y", "a", "c", "b", "d", "e", "f", "g", "z"]
    for letter in letters:
        tree1.insert(letter)

    root = tree1.root
    print(root, root.right, root.left)
    
    print(tree1.get_height())

main()

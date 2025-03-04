# Implementation & testing of the BinaryTree

# Import file
from TEST_CODE import *
import os
from BinTreeClass import BinaryTree

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    # TEST 1 - Test BinaryNode nested class
    # BEFORE TESTING: implement BinaryNode actions & attributes
    TEST_binary_node(BinaryTree)


    # TEST 2 - Test Position nested class
    # BEFORE TESTING: implement Position actions & attributes
    TEST_position(BinaryTree)

    BT = BinaryTree()
    
    # TEST 3 - Test BinaryTree initialization
    # BEFORE TESTING: implement BinaryTree __init__
    TEST_new_binary_tree(BT)


    # TEST 4 - Test make position & validate
    # BEFORE TESTING: implement __make_position, __validate
    TEST_make_position_validate(BT, BinaryTree)


    # TEST 5 - Test add methods
    # BEFORE TESTING: implement add_root, add_left, add_right
    nodes = TEST_add_nodes(BT)


    # Tree Review!
    # This is not a test and has nothing to do with your code
    VIEW_tree()
    

    # TEST 6 - Test getters (1)
    # BEFORE TESTING: implement is_root, is_leaf, is_ancestor
    #                           are_siblings, num_children 
    TEST_bool_getters(BT, nodes)


    # TEST 7 - Test  getters (2)
    # BEFORE TESTING: implement BinaryTree get_root, get_left, get_right
    #                           Positon __eq__, __ne__
    TEST_BinNode_getters(BT, nodes)


    # TEST 8 - Test getters (3)
    # BEFORE TESTING: implement get_ancestors, get_parent,
    #                           get_children, get_sibling, get_depth
    TEST_family_relationships(BT, nodes)

    
    # TEST 9 - Test replace & delete nodes
    # BEFORE TESTING: implement replace, delete
    TEST_replace_delete(BT, nodes)
    

    # TEST 10 - Test docstrings
    # BEFORE TESTING: implement all docstrings
    TEST_docs(BT, BinaryTree)
    

if __name__ == "__main__":
    os.system("clear")
    main()
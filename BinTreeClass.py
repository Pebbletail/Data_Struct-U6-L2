#Brook Brudnok
#2/25/25

class BinaryTree:

  class BinaryNode:
    def __init__(self, val):
      self.__value = val
      self.__parent = None
      self.__left = None
      self.__right = None

    def __set_parent(self, node):
      """update parent pointer"""
      if type(node) != type(self) and type(node) != type(None):
        raise TypeError("Parent must be of type BinaryNode")
      else:
        self.__parent = node

    def __set_left(self, node):
      """update left child pointer"""
      if type(node) != type(self) and type(node) != type(None):
        raise TypeError("Left child must be of type BinaryNode or None")

      if self.__right is node and node != None:
        raise TypeError("Left child cannot be the same as right child")
      
      if node is self:
        raise ValueError("Node cannot be a child of itself")

      self.__left = node

    def __set_right(self, node):
      """update right child pointer"""
      if type(node) != type(self) and type(node) != type(None):
        raise TypeError("Right child must be of type BinaryNode or None")

      if self.__left is node and node != None:
        raise ValueError("Right child cannot be the same as left child")
      
      if node is self:
        raise ValueError("Node cannot be a child of itself")

      self.__right = node

    def __str__(self):
      """Display to enable view for whole tree"""
      return f"|{self.__value}| \n({self.__value})L: {self.__left} \n({self.__value})R: {self.__right}"
    

  class Position:

    def __init__(self, member, node):
      self.__member_of = member
      self.__node = node

    def get_value(self):
      """returns the value at a given position"""
      return self.__node._BinaryNode__value

    def __eq__(self, other):
      """returns true if two nodes are the same object"""
      if type(self) == type(other):
        if self.__node is other.__node:
          return True
        
      return False

    def __ne__(self, other):
      """returns true if two nodes are not the same object"""
      if type(self) == type(other):
        if self.__node is not other.__node:
          return True
        
      return False

  ##start of BinaryTree methods and attributes
  def __init__(self):
    self.__root = None
    self.__size = 0

  def __validate(self, pos):
    """return node in specified position or raise exception if position does not belong to list or not a position"""
    if type(pos) != self.Position:
      raise TypeError("Argument is not of type Position")
    if pos._Position__member_of != self:
      raise ValueError("Argument is not in selected list")

    return pos._Position__node

  def __make_position(self, node):
    """return new position object for a given node or return None if not given node"""
    if type(node) != type(self.BinaryNode(None)):
      return None
    else:
      new_pos = self.Position(self, node)
      return new_pos

  def add_root(self, val):
    """inserts new root into an empty tree"""
    if type(self.__root) != type(None):
      raise Exception("Root cannot be added to non-empty tree")

    root = self.__make_position(self.BinaryNode(val))
    self.__root = root
    self.__size += 1
    return root

  def add_left(self, pos, val):
    """adds value as left child to given position"""
    pos_node = self.__validate(pos)

    if pos_node._BinaryNode__left != None:
      raise Exception("Cannot add left child to node with existing left child")

    new_child = self.BinaryNode(val)
    pos_node._BinaryNode__set_left(new_child)
    new_child._BinaryNode__set_parent(pos_node)

    self.__size += 1
    return self.__make_position(new_child)

  def add_right(self, pos, val):
    """adds value as right child to given position"""
    pos_node = self.__validate(pos)

    if pos_node._BinaryNode__right != None:
      raise Exception("Cannot add right child to node with existing right child")

    new_child = self.BinaryNode(val)
    pos_node._BinaryNode__set_right(new_child)
    new_child._BinaryNode__set_parent(pos_node)

    self.__size += 1
    return self.__make_position(new_child)

  def replace(self, pos, val):
    """replaces contents of node, returns old contents"""
    pos_node = self.__validate(pos)
    v = self.Position.get_value(pos)
    pos_node._BinaryNode__value = val
    return v

  def delete(self, pos):
    """removes a node from the tree"""
    pos_node = self.__validate(pos)
    c_num = self.num_children(pos)
    if c_num == 2:
      raise Exception("Cannot delete node with multiple children")
    
    v = self.Position.get_value(pos)

    if self.is_root(pos) == True:
      self.__root = None
      self.__size -= 1
      return v
    
    parent = pos_node._BinaryNode__parent
    child = None
      
    if parent._BinaryNode__left == pos_node:
      c_pos = "l"
    else:
      c_pos = "r"

    if c_num == 0:
      child = self.get_children(pos)
      if c_pos == "l":
        parent._BinaryNode__set_left(child)
      else:
        parent._BinaryNode__set_right(child)
      if self.is_root(pos) == True:
        self.__root = None


    if c_num == 1:
      print(type(child))
      child = self.__validate(self.get_children(pos)[0])
      if c_pos == "l":
        parent._BinaryNode__set_left(child)
      else:
        parent._BinaryNode__set_right(child)
      if self.is_root(pos) == True:
        self.__root = None

      child._BinaryNode__set_parent(parent)

    pos_node._BinaryNode__set_parent(pos_node)
    self.__size -= 1
    return v

  def is_root(self, pos):
    """determines if given position is the root"""
    pos_node = self.__validate(pos)
    if type(pos_node._BinaryNode__parent) == type(None):
      return True
    else:
      return False

  def is_leaf(self, pos):
    """determines if given postion is a leaf"""
    pos_node = self.__validate(pos)
    if type(pos_node._BinaryNode__left) == type(None) and type(pos_node._BinaryNode__right) == type(None):
      return True
    else:
      return False

  def is_ancestor(self, ancestor, descendant):
    """determines if one node is ancestor of another"""
    if self.is_root(descendant) or ancestor == descendant:
      return False
    desc_node = self.__validate(descendant)
    check = desc_node

    while type(check._BinaryNode__parent) != type(None):
      if self.__make_position(check) == ancestor:
        return True
      else:
        check = check._BinaryNode__parent

    return False

  def are_siblings(self, sib1, sib2):
    """determine if two nodes are siblings"""
    if sib1 == sib2:
      return False
    sib1_node = self.__validate(sib1)
    sib2_node = self.__validate(sib2)

    parent = sib1_node._BinaryNode__parent
    if sib2_node._BinaryNode__parent == parent:
      return True
    else:
      return False

  def num_children(self, pos):
    """returns the number of children of given"""
    pos_node = self.__validate(pos)
    c = 0
    if type(pos_node._BinaryNode__left) != type(None):
      c += 1
    if type(pos_node._BinaryNode__right) != type(None):
      c+= 1
    return c


  def get_root(self):
    """returns root in position"""
    return self.__root

  def get_left(self, pos):
    """returns left child of given in position"""
    pos_node = self.__validate(pos)
    leftC = pos_node._BinaryNode__left
    return self.__make_position(leftC)

  def get_right(self, pos):
    """returns right child of given in position"""
    pos_node = self.__validate(pos)
    rightC = pos_node._BinaryNode__right
    return self.__make_position(rightC)

  def get_parent(self, pos):
    """returns parent of given in position"""
    pos_node = self.__validate(pos)
    parent = pos_node._BinaryNode__parent
    return self.__make_position(parent)

  def get_children(self, pos):
    """returns list of children of given in positions"""
    pos_node = self.__validate(pos)
    if self.num_children(pos) == 0:
      return None

    c_list = []
    if type(pos_node._BinaryNode__left) != type(None):
      c_list.append(self.__make_position(pos_node._BinaryNode__left))
    if type(pos_node._BinaryNode__right) != type(None):
      c_list.append(self.__make_position(pos_node._BinaryNode__right))
    return c_list

  def get_sibling(self, pos):
    """returns sibling of given in position"""
    pos_node = self.__validate(pos)
    if self.is_root(pos) == True:
      return None
    parent = pos_node._BinaryNode__parent
    if self.num_children(self.__make_position(parent)) == 1:
      return None

    if parent._BinaryNode__left is not pos_node:
      return self.__make_position(parent._BinaryNode__left)
    if parent._BinaryNode__right is not pos_node:
      return self.__make_position(parent._BinaryNode__right)

  def get_ancestors(self, pos):
      """returns list of ancestors in positions"""
      pos_node = self.__validate(pos)
      if self.is_root(pos) == True:
        return None
      anc_list = []
      anc = pos_node

      while type(anc._BinaryNode__parent) != type(None):
        anc_list.append(self.__make_position(anc._BinaryNode__parent))
        anc = anc._BinaryNode__parent

      return anc_list

  def get_depth(self, pos):
    """returns depth of given"""
    ancestors = self.get_ancestors(pos)
    if type(ancestors) == type(None):
      return 0

    return len(ancestors)

  def __len__(self):
    """returns number of nodes"""
    return self.__size

  def __str__(self):
    """Convert root to string"""
    return str(self.__root)

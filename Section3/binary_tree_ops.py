class Node:
    """
        A class representing a node in a binary tree
    """
    def __init__(self, data):
        """
        Define a node of a binary tree.
        :param data: the data or payload that the node holds.
        """
        self._data = data
        self._right = None
        self._left = None

    def insert_left(self, data):
        """
        Insert a node as a left child of the node.
        :param data: payload for the left child
        :return: None
        """
        pass

    def insert_right(self, data):
        """
        Insert a node as a right child of the node.
        :param data: payload for the right child
        :return: None
        """
        pass

    def get_left_child(self):
        """
        Get the left child of the node
        :return: left child of the node
        """
        return self._left

    def get_right_child(self):
        """
        Get the right child of the node
        :return: right child of the node
        """
        return self._right

    def set_left_child(self, new_node):
        """
        Set the left child of the node
        :param new_node: Node to be set as the left child
        :return: None
        """
        self._left = new_node

    def set_right_child(self, new_node):
        """
        Set the right child of the node
        :param new_node: Node to be set as the left child
        :return: None
        """
        self._right = new_node

    def get_data(self):
        """
        Get the data of the node
        :return: data/payload of the node
        """
        return self._data

    def set_data(self, new_value):
        """
        Set the data or payload of the node to a new value
        :param new_value: Payload or the data that the node will hold from now on.
        :return: None
        """
        self._data = new_value

class BinaryTree:
    """
    A class representing a Binary Tree
    """
    def __init__(self, data):
        """
        Initialize the tree with a root node holding data.
        :param data: payload of the root node
        """
        self._root = Node(data)

    def get_root(self):
        """
        Get the root node of the binary tree.
        :return: Node representing the root of the tree.
        """
        return self._root

    def in_order(self):
        """
        Traverse the tree using in order traversal method.
        """
        pass


if __name__ == "__main__":
    """
                        5
                       / \
                      /   \
                     /     \
                    3       7
                   / \     / \
                  /   \   /   \
                 2     4 6
    """
    pass
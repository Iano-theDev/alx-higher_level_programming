#!/usr/bin/python3
"""Defines classes Node and SinglyLinkedList"""


class Node:
    """Represents a node in a linked list"""
    def __init__(self, data, next_node=None):
        """Initializes the Node instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data attribute
        Args:
            value(int): Data held by the node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @property
    def next_node(self):
        """Getter for the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node
        Args:
            value(Node): a node of type Node
        """
        if isinstance(value, Node) is False:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __str__(self):
        """String representation of a Node
        Return:
            A formated string representating a Node"""
        return str(self.__data)
        
class SinglyLinkedList:
    """Represents a singly linked list"""
    def __init__(self):
        """Initializes thr singly-linked-list class"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new NOde into the correct sorted position
           in the list according to increasing order
        Args:
            value(Node): node to be inserted in the list
        Return:
            A sorted SinglyLinkedList list."""
        
        

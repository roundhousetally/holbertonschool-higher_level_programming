#!/usr/bin/python3
""" Sinlgy linked list mod """


class Node:
    """ singly linked list """
    def __init__(self, data, next_node=None):
        """ private att
        Args:
             data - info in list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ data """
        return self.__data

    @data.setter
    def data(self, value):
        """ set value in a node in a linked list """
        if not isinstace(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the next node """
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
""" Does More Docstring go here, I really don't know """


class SinglyLinkedList:
    """ linked list """
    def __init__(self):
        """ head """
        self.__head = None

    def sorted_insert(self, value):
        """ node """
        New = Node(value)
        New.__next_node = self.__head
        self.__head = New
        return self.__head

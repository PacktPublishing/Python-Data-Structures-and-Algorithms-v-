class EmptyStackError(Exception):
    """
        Custom Error for empty stack.
    """
    pass

class Stack:
    """
        Stack: LIFO Data Structure.
        Operations:
            push(item)
            pop()
            peek()
            isEmpty()
            size()
    """

    def __init__(self):
        """
            Define an empty stack.
            Here we are using list to implement the Stack data structure.
        """
        pass

    def isEmpty(self):
        """
            Test if the stack has no items.
            :return: True if Stack is Empty. False Otherwise
        """
        pass

    def push(self, item):
        """
            Pushes an item at the top of the stack updating the top of the stack.
            :param item: item to be added on to the stack
        """
        pass

    def pop(self):
        """
            Removes an item from the top of the stack modifying it.
            :return: item removed from the top of the stack.
            :raises: EmptyStackError if stack has no elements.
        """
        pass

    def peek(self):
        """
            Just returns the item at the top of the stack without modifying the stack.

            :return: item at the top of the stack.
            :raises: EmptyStackError if stack has no elements.
        """
        pass

    def size(self):
        """
            Returns the number of elements currently in the stack.
            :return: size of the stack.
        """
        pass


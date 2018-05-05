class EmptyDequeError(Exception):
    """
        Custom Error for empty Deque.
    """
    pass

class Deque:
    """
        Deque: Hybrid Data Structure.
        Operations:
            addFront(item)
            addRear(item)
            removeFront()
            removeRear()
            isEmpty()
            size()
    """

    def __init__(self):
        """
            Define an empty Deque.
            Here we are using list to implement the Deque data structure.
        """
        pass

    def addFront(self, item):
        """
            Insert the item at the Front of the Deque
            :param item: item to be added on to the Deque
        """
        pass

    def addRear(self, item):
        """
            Insert the item at the rear of the Deque
            :param item: item to be added on to the Deque
        """
        pass

    def removeFront(self):
        """
            Removes an item from the front of the Deque.
            :return: item removed from the front of the Deque.
            :raises: EmptyDequeError if Deque has no elements.
        """
        pass

    def removeRear(self):
        """
            Removes an item from the rear of the Deque.
            :return: item removed from the front of the Deque.
            :raises: EmptyDequeError if Deque has no elements.
        """
        pass

    def size(self):
        """
            Returns the number of elements currently in the Deque.
            :return: size of the Deque.
        """
        pass


    def isEmpty(self):
        """
            Test if the Deque has no items.
            :return: True if Deque is Empty. False Otherwise
        """
        pass
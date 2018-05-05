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
        self._data = []

    def addFront(self, item):
        """
            Insert the item at the Front of the Deque
            :param item: item to be added on to the Deque
        """
        self._data.insert(0, item)

    def addRear(self, item):
        """
            Insert the item at the rear of the Deque
            :param item: item to be added on to the Deque
        """
        self._data.append(item)

    def removeFront(self):
        """
            Removes an item from the front of the Deque.
            :return: item removed from the front of the Deque.
            :raises: EmptyDequeError if Deque has no elements.
        """
        if self.isEmpty():
            raise EmptyDequeError("removeFront: Removing from an empty Deque")

        return self._data.pop(0)

    def removeRear(self):
        """
            Removes an item from the rear of the Deque.
            :return: item removed from the front of the Deque.
            :raises: EmptyDequeError if Deque has no elements.
        """
        if self.isEmpty():
            raise EmptyDequeError("removeFront: Removing from an empty Deque")

        return self._data.pop()

    def size(self):
        """
            Returns the number of elements currently in the Deque.
            :return: size of the Deque.
        """
        return len(self._data)


    def isEmpty(self):
        """
            Test if the Deque has no items.
            :return: True if Deque is Empty. False Otherwise
        """
        return self.size() == 0

if __name__ == "__main__":
    q = Deque()

    q.addFront("Hello")
    q.addFront("Hi,")
    q.addRear("World")
    q.addRear("Guys")

    print("Size of the Deque is: {}.".format(q.size()))

    while not q.isEmpty():
        print(q.removeFront())

    import time

    time.sleep(1)  # To ensure the output from program and exception is not interleaved.

    # Try to remove from empty Deque.
    q.removeRear()
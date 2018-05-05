class EmptyHeapError(Exception):
    pass

class MinHeap:
    def __init__(self):
        self._list = [0]
        self._size = 0

    def insert(self, key):
        self._list.append(key)
        self._size += 1
        self._perc_up(self._size)

    def find_minimum(self):
        if self.isEmpty():
            raise EmptyHeapError("No Element found in the heap")

        return self._list[1]

    def delete_minimum(self):
        if self.isEmpty():
            raise EmptyHeapError("No Element found in the heap")

        minimum = self._list[1]

        self._list[1] = self._list.pop()
        self._size -= 1
        self._perc_down(1)

        return minimum

    def size(self):
        return self._size

    def __len__(self):
        return self.size()

    def isEmpty(self):
        return self.size() == 0

    def _perc_up(self, pos):
        while pos // 2 > 0:
            if self._list[pos] < self._list[pos // 2]:
                (self._list[pos], self._list[pos // 2]) = (self._list[pos // 2], self._list[pos])

            pos = pos // 2

    def _perc_down(self, pos):
        while pos * 2 <= self._size:
            min_child = self._min_child(pos)
            if self._list[pos] > self._list[min_child]:
                (self._list[pos], self._list[min_child]) = (self._list[min_child], self._list[pos])

            pos = min_child

    def _min_child(self, pos):
        if pos * 2 + 1 > self._size:
            return pos * 2
        else:
            if self._list[pos * 2] < self._list[pos * 2 + 1]:
                return pos * 2
            else:
                return pos * 2 + 1

    def __repr__(self):
        return str(self._list)


if __name__ == "__main__":
    min_heap = MinHeap()

    for i in [20, 30, 40, 60, 10, 50]:
        min_heap.insert(i)

    print(min_heap)

    print("Minimum Item in the min heap is: {}".format(min_heap.find_minimum()))

    min_heap.delete_minimum()

    print(min_heap)

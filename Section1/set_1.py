
class Set:

    def __init__(self, *args):
        self._data = dict()

        for arg in args:
            self.add_item(arg)


    def __iter__(self):
        return iter(self._data)


    def __len__(self):
        return len(self._data)


    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, str(self._data.keys()))


    def add_item(self, item):
        self._data[item] = item


    def remove_item(self, item):
        self._data.pop(item)


    def contains_item(self, item):
        return item in self._data


    def items(self):
        return self._data.keys()


    def union(self, other_set):
        if type(other_set) != type(self):
            raise TypeError("other_set is not of type {}".format(type(self)))

        result = Set()

        for item in self:
            result.add_item(item)

        for item in other_set:
            result.add_item(item)

        return result


    def intersection(self, other_set):
        if type(other_set) != type(self):
            raise TypeError("other_set is not of type {}".format(type(self)))

        result = Set()

        for item in self:
            if item in other_set:
                result.add_item(item)

        return result


if __name__ == "__main__":
    s = Set(1, 2, 3, 4, 5)

    print(s)

    for i in s:
        print(i)

    s.add_item(7)
    s.add_item(6)

    print(s)

    p = Set(4, 5, 6, 7, 8)

    print(s.union(p))
    print(s.intersection(p))
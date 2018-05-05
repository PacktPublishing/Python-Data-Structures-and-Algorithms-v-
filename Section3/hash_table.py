
class HashTable:
    """
        HashTable: Key-Value Map/Associative Array.
        Operations:
            put(key, value)
            get(key)
    """

    def __init__(self):
        """
            Define an empty hashtable.
            We use lists to implement an hash table.
        """
        self._size = 4
        self._table = [None] * self._size

    def hash_function(self, key):
        return key % self._size

    def put(self, key, value):
        """
            Add a key-value pair into the hash table.
            :param key: key is item used to calculate the hash
            :param value: Actual value stored in the slot.
        """
        # If the table is 75% or more full, resize it to twice the current size.
        if self.utilization >= 0.75:
            self._resize()

        slot = self.hash_function(key)

        # Do a linear probe until a slot is found in case of collision.
        if self._table[slot] is not None and self._table[slot][0] != key:
            slot = self._findslot(slot, key)

        self._table[slot] = (key, value)

    def get(self, key):
        """
            Return the value for a particular key.
            :param key: key for which value is returned.
            :return: value corresponding to the key.
        """
        slot = self.hash_function(key)

        # Do a linear probe until a slot is found in case of collision.
        if self._table[slot] is not None and self._table[slot][0] != key:
            slot = self._findslot(slot, key)

        return self._table[slot][1] if self._table[slot] is not None else None

    def _findslot(self, slot, key):
        """
            Determine the next slot where the key would fit in case of collision.
            :param slot: Current slot that resulted in collision.
            :param key: key we are trying to put/get.
            :return: next slot where the key would fit.
        """
        next_slot = self.hash_function(slot + 1)

        while self._table[next_slot] is not None and self._table[next_slot][0] != key:
            next_slot = self.hash_function(next_slot + 1)

        return next_slot

    def _resize(self):
        """
            Resize the table to twice its current size.
        """
        self._size = self._size * 2
        old_table = self._table
        self._table = [None] * self._size

        for item in old_table:
            if item is not None:
                self.put(item[0], item[1])

    def __iter__(self):
        return iter([(item[0], item[1]) for item in self._table if item is not None])

    @property
    def utilization(self):
        return float(len(self)) / float(self._size)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return len([k for k in self._table if k is not None])


if __name__ == "__main__":
    h_t = HashTable()

    h_t[18] = "18"
    h_t[18] = "19"
    h_t[21] = "21"
    h_t[35] = "35"
    h_t[26] = "26"
    h_t[34] = "34"
    h_t[89] = "89"

    for k, v in h_t:
        print(k, v)

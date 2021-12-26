class Array(object):
    """
    Represent an array

    """

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed on each position"""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """this method is used to get the capacity of the array"""
        return len(self._items)

    def __str__(self):
        """
        The string representation of the array

        """
        return str(self._items)

    def __iter__(self):
        """
        Supports traversal with a for loop
        """
        return iter(self._items)

    def __getitem__(self, index):
        """
        Subscript operator for access at index
        :param index:
        :return:
        """
        return self._items[index]

    def __setitem__(self, index, newItem):
        """

        :param index:
        :param newItem:
        :return:
        """
        self._items[index] = newItem


if __name__ == '__main__':
        a = Array(5)
        print(len(a))
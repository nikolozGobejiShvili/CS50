class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if capacity < 0:
            raise ValueError("Capacity is less than 0")


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Exceed capacity")

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There are less cookies than you asked to remove")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity is less than 0")
        self._capacity = capacity

    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        self._size = size
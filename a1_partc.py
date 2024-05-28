

class Stack:
    def __init__(self, cap=10):
        self._data = [None] * cap  
        self._size = 0  
        self._capacity = cap  

    def capacity(self):
        return self._capacity

    def push(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = data
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError('pop() used on empty stack')
        self._size -= 1
        return self._data[self._size]

    def get_top(self):
        if self._size == 0:
            return None
        return self._data[self._size - 1]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_cap


class Queue:
    def __init__(self, cap=10):
        self._data = [None] * cap
        self._front = 0
        self._size = 0
        self._capacity = cap

    def capacity(self):
        return self._capacity

    def enqueue(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = data
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError('dequeue() used on empty queue')
        val = self._data[self._front]
        self._data[self._front] = None  #
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return val

    def get_front(self):
        return None if self._size == 0 else self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._front = 0
        self._capacity = new_cap




class Deque:
    def __init__(self, cap=10):
        self._data = [None] * cap
        self._front = 0
        self._size = 0
        self._capacity = cap

    def capacity(self):
        return self._capacity

    def push_front(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = data
        self._size += 1

    def push_back(self, data):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = data
        self._size += 1

    def pop_front(self):
        if self._size == 0:
            raise IndexError('pop_front() used on empty deque')
        val = self._data[self._front]
        self._data[self._front] = None  
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return val

    def pop_back(self):
        if self._size == 0:
            raise IndexError('pop_back() used on empty deque')
        rear = (self._front + self._size - 1) % self._capacity
        val = self._data[rear]
        self._data[rear] = None  
        self._size -= 1
        return val

    def get_front(self):
        return None if self._size == 0 else self._data[self._front]

    def get_back(self):
        if self._size == 0:
            return None
        rear = (self._front + self._size - 1) % self._capacity
        return self._data[rear]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __getitem__(self, k):
        if k < 0 or k >= self._size:
            raise IndexError('Index out of range')
        return self._data[(self._front + k) % self._capacity]

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._front = 0
        self._capacity = new_cap
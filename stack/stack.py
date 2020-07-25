"""
A stack is a data structure whose primary purpose is to store and
return values in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

'''
Stack class with list storage structure.
'''


class Stack:
    class Node:
        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return not self

    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            result = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return result

    def top(self):
        if self.is_empty():
            return None
        return self.head.value


s = Stack()
s.push(5)
s.push('five')
s.push(9)
s.push('nine')
print(s.top())

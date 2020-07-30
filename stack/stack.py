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


# class Stack:
#    def __init__(self):
#        self.size = 0
#        self.storage = []

#    def __len__(self):
#        return self.size

#    def push(self, value):
# add an element to front of array
#        self.size += 1
#        self.storage.insert(0, value)

#    def pop(self):
#        if len(self.storage) == 0:
#            return None
# remove first element in storage
#       self.size -= 1
#       node = self.storage.pop(0)
#      return node.value


new_stack = Stack()
print(len(new_stack))
new_stack.push(2)
new_stack.push(3)
new_stack.push(5)
print(len(new_stack))
print(new_stack.storage)

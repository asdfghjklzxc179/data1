# data structures allow us to
# -access data , e.g., arr[3], data_read():, ... (Node and LinkedList classes)
# -add data (insertion), e.g., arr.append(), dict("new_key") = value (functions that add)
# -delete (functions that delete)
# -search through a data structure, e.g., (functions to search_)

# what is a linked list?
#

# node needs a value and the next node


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


# this is like a NodeManager, it's go nna know theend and start of the ll (track head and tail)
class LinkedList:
    def __init__(self):
        self.head = None  # stores a node, that corresponds the first node in list
        self.tail = None  # stores end of list n ode


def add_to_head(self, value):
    # create a new node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
        self.head = new_node
        self.tail = new_node
    else:
        # make new node the head
        new_node.next_node = self.head
        # move head to new node
        self.head = new_node

    pass


def add_to_tail(self, value):
    # check if list is empty
    if self.head is None and self.tail is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next_node = self.tail
        self.tail = new_node


def remove_head(self):
    if not self.head:
        return None
    if self.head.next_node = None:
        head_value = self.head.value
        self.head = None
        self.tail = None
        return None


def contains(self, value):
    pass

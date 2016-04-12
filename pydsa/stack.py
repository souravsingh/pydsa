class Stack(object):
    """
    Stack data structure for PyDSA
    """

    def __init__(self):
        """ Constructor """
        self.items = []

    def push(self, x):
        """ Pushes element x on top of the stack """
        self.items.append(x)

    def pop(self):
        """ Pops the element from the top """
        return self.items.pop()

    def peek(self):
        """ Peek next element """
        return self.items[self.size() - 1]

    def size(self):
        """ Returns the size of the stack """
        return len(self.items)

    def is_empty(self):
        """ Returns True if the stack is empty """
        return self.size() == 0

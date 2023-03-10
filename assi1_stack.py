class Node:  #creating a node
    def __init__(self, value):
        self.value = value  # each node has a value which holds number that is to be stored in stack.
        self.next = None    # each node has next which reference to the next node in the stack.

class Stack:
    def __init__(self):
        self.top = None     #reference the top node
        self.size = 0       #tracks size

    def push(self, item):
        newNode = Node(item)      #new node  object
        newNode.next = self.top   #next is made to reference the current top node
        self.top = newNode        #top is made to reference the new node
        self.size += 1            #size is increased

    def pop(self):
        if self.is_empty():
            raise Exception('Your stack is empty') 
        item = self.top.value     #storing the value of the top node to return
        self.top = self.top.next  #making top node reference to next which was the previous node
        self.size -= 1            #size is decreased
        return item               

    def peek(self):
        if self.is_empty():
            print('Your stack is empty')
        return self.top.value

    def is_empty(self):
        return self.top is None

''' 
The stack is implemented using node. Whenever user writes push(x), a node is created with value x
 and refers to the current top node. This new node is now made the top node and this refers to the
   previous node. Now, whenever someone use pop(), this node makes top node the previous node. '''
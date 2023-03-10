class Node:    #creating a node
    def __init__(self, value):
        self.value = value    # value to hold the value that is to be added in the queue
        self.next = None      # referencing next node

class Queue:
    def __init__(self):
        self.front = None    # stores the front node 
        self.back = None     # stores the back node

    def enqueue(self, item):
        newNode = Node(item)
        if self.back:
            self.front.next = newNode    #The previous node is made to refer the new node
            self.back = newNode          #The new node is made the back node
        else:
            self.front = newNode         #front and back both node stores this new node
            self.back = newNode

    def dequeue(self):
        if not self.front:
            raise Exception("Your queue is empty")
        item = self.front.value        #storing the value to return
        self.front = self.front.next   #the new front node is now the node which was refered by the previous
        if not self.front:
            self.back = None
        return item

    def peek(self):
         if self.front:
            return self.front.value
         raise Exception("Your queue is empty")

    def is_empty(self):
        return self.front is None

''' The queue is implemented using node. The first element when is added is saved as both front and back node
        After that if some element is added, the front node is made to point at that node and back node is 
            made that node. Now when someone uses dequeue(), the front node is made the next node.'''

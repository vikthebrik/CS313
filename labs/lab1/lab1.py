class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class
        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue
        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """
    Class Queue uses parent class node and implements the data structure of a queue

    — A brief summary of its purpose and behavior
    — Any public methods, along with a brief description"""
    def __init__(self):
        """Constructs (or initializes) the attributes for an object of the class
        Parameters
        ----------
        self - inherits needed parameters from parent
        initialized to be empty
        """
        self.__head = None
        self.__tail = None
        

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        out = []
        head = self.__head
        while head:
            out.append(head.getData())
            head = head.getNext()
        return str(out)
            
    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        new_node = Node(newData)
        if self.isEmpty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.setNext(new_node)
            self.__tail = new_node



    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty():
            return None
        temp = self.__head
        self.__head = self.__head.getNext()
        if self.__head is None: 
            self.__tail = None
        return temp.getData()
    
    def isEmpty(self):
        '''Check if the Queue is empty.'''
        return self.__head is None


class Stack(object):
    """Constructs (or initializes) the attributes for a Stack

        Parameters
        ----------
        Node Object
        """
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__top = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        out = []
        top = self.__top
        while top:
            out.append(top.getData())
            top = top.getNext()
        return str(out)

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        new = Node(newData)
        new.setNext(self.__top)
        self.__top = new

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.isEmpty():
            return None
        temp = self.__top
        self.__top = self.__top.getNext()
        return temp.getData()

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        return self.__top is None


def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Return appropriate value

    # Convert the input to lowercase and remove non-alphanumeric characters

    # Push to stack and enqueue to queue
    for char in s:
        myStack.push(char)
        myQueue.enqueue(char)

    # Compare stack and queue outputs
    while not myStack.isEmpty():
        if myStack.pop() != myQueue.dequeue():
            return False
    return True

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    return

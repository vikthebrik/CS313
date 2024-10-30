class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.
    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations -- using __swap method.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        return self.heap


    def insert(self, data):
        """Insert an element into the heap.

        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        # Parameters:
        # data: The value to be inserted into the heap.
        #
        # Raises:
        # IndexError: If the heap is full.
        if self.length >= self.max_size:
            raise IndexError("Heap is full")
        self.heap[self.length] = data
        self.length += 1
        curr_index = self.length - 1
        # Swap upwards till rules are met
        while curr_index > 0:
            parent_index = self.__get_parent(curr_index)
            if self.heap[curr_index] > self.heap[parent_index]:
                self.__swap(curr_index, parent_index)
                curr_index = parent_index
            else:
                break
        
    def peek(self):
        """Return the maximum value in the heap."""
        if self.length == 0:
            return None
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.
        
        Returns:
        The maximum value in the heap, or None if the heap is empty.
        
        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        if self.length == 0:
            raise KeyError("Heap is empty")
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.length -= 1
        self.__heapify(0)
        return max_value

    def sort_in_place(self):
        """Perform heatsort in-place (e.g., reorder elements in ascending order for self.heap)
        Note that the heap is no longer "valid" once this method is called.
        Tip 1. Use the list_length parameter for __heapify method to limit the scope of self.heap
        Tip 2. Only use build_heap once, and then call __heapify for index where max-heap property is violated
        """
        self.build_heap()
        for i in range(self.length - 1, 0, -1):
            self.__swap(0, i)
            self.__heapify(0, i)


    def __heapify(self, curr_index, list_length = None):
        """Ensure the max-heap property for the heap, starting at the specified index.
        Parameters:
        curr_index (int): The index at which to start heapifying.
        list_length (int, optional): Length of the portion of the list to consider.
                                     Defaults to the current length of the heap.
        """
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        if list_length is None:
            list_length = self.length
        largest = curr_index
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)

        if left < list_length and self.heap[left] > self.heap[largest]:
            largest = left
        if right < list_length and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest, list_length)


    def build_heap(self):
        """Build a max-heap from the current list.
        
        This method is typically used to initialize a valid heap from an unsorted list.
        """
        # builds max heap from the list l.
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        for i in range(self.length // 2 - 1, -1, -1):
            self.__heapify(i)

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    

def heap_sort(l):
    """The public heap_sort should do the following.
    1. Create a max_heap object using the provided list l
    2. Call sort_in_place method to sort the list "in-place"
    """
    heap = max_heap(data=l)
    heap.sort_in_place()
    return heap.get_heap()
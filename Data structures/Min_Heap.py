"""
Resources:
    * https://en.wikipedia.org/wiki/Binary_heap
    * https://runestone.academy/ns/books/published/pythonds/Trees/BinaryHeapImplementation.html
    * https://favtutor.com/blogs/heap-in-python


    * Binary heap:
        - Complete binary tree where all levels are completely filled except the last level
        - Every element in the heap is smaller than its children
        * Properties:
            - A binary heap can be represented as a flat array array[1..n] where the root node is array[1] and for each node array[i], its children (if they exist) are elements array[2i] and array[2i + 1]
            - An existing array can be converted into a heap in place in O(n) time.
            - A new item can be inserted into a binary heap in O(log(n)) time.
            - The maximum element can be removed from a binary heap in O(log(n)) time.
        * Operations:
            - Heapify: Convert an array into a min/max heap
            - Insert: Insert an element into the heap
            - Remove: Remove the an element
            - Extract: Remove min or max element
            - Search: Finding an arbitrary element
            - Decrease key: Change the key of an element
            * Internal procedures:
                - Rise: Move an element higher up the heap until it satifies the heap propertiy
                - Fall: Move an element down the heap until it satifies the heap propertiy

"""

class Min_Heap():
    def __init__(self) -> None:
        self.size = 0
        self.heap = [0] # for simple integer division in other methods
        
    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        return str(self.heap[1:])
    

    def heapify(self, array: list) -> None:
        """
        - Convert an array into a min heap
        """
        self.heap = [0]
        i = len(array)//2
        n = len(array)
        self.size = n
        for i in range(n):
            self.heap.append(array[i])
        while (i>0):
            self.fall(i)
            i -= 1
    
    def insert(self, value: int) -> None:
        """
        - Insert an element into the heap
        """
        self.heap.append(value)
        self.size += 1
        self.rise(self.size)
        print("Insert: ", value)
        
    def rise(self, i)-> None:
        """
        Move an element higher up the heap until it satifies the heap propertiy
        """
        while i//2 > 0:
            if self.heap[i] < self.heap[i//2]:
                tmp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = tmp
            i = i//2
            
    def min_child(self, i) -> int:
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def extract_min(self) -> int:
        """
        Remove the an element
        """
        min_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.fall(1)
        print("Extract min: ", min_value)
        return min_value
    
    def fall(self, i):
        """
        Move an element down the heap until it satifies the heap propertiy
        """
        while (i * 2) <= self.size:
            min_child = self.min_child(i)
            if self.heap[i] > self.heap[min_child]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[min_child]
                self.heap[min_child] = tmp
            i = min_child
  
if __name__ == '__main__':
    H = Min_Heap()
    
    # testing inserting manually 

    H.insert(67)
    H.insert(10)
    H.insert(11)
    H.insert(15)
    H.insert(1)
    H.insert(155)
    H.insert(-5)
    print(H)
    H.extract_min()
    print(H)
    
    #  testing min heapyfying a given list

    a_list = [9, 6, 5, 2, 3]
    H.min_heapify(a_list)
    print(H)
    H.extract_min()
    print(H)

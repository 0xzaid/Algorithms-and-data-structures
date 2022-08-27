"""
Resources:
    * https://en.wikipedia.org/wiki/Binary_heap
    * https://runestone.academy/ns/books/published/pythonds/Trees/BinaryHeapImplementation.html
    * https://favtutor.com/blogs/heap-in-python


    * Binary heap:
        - Complete binary tree where all levels are completely filled except the last level
        - Every element in the heap is no smaller than its children
        * Properties:
            - A binary heap can be represented as a flat array array[1..n] where the root node is array[1] and for each node array[i], its children (if they exist) are elements array[2i] and array[2i + 1]
            - An existing array can be converted into a heap in place in O(n) time.
            - A new item can be inserted into a binary heap in O(log(n)) time.
            - The maximum element can be removed from a binary heap in O(log(n)) time.
        * Operations:
            - Heapify: Convert an array into a max heap
            - Insert: Insert an element into the heap
            - Remove: Remove the an element
            - Extract: Remove max element
            - Search: Finding an arbitrary element
            - Decrease key: Change the key of an element
            * Internal procedures:
                - Rise: Move an element higher up the heap until it satifies the heap propertiy
                - Fall: Move an element down the heap until it satifies the heap propertiy

"""

class Max_Heap():
    def __init__(self) -> None:
        self.size = 0
        self.heap = [0] # for simple integer division in other methods
        
    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        return str(self.heap[1:])
        
    def get_heap(self) -> str:
        return self.heap[1:]
    

    def heapify(self, array: list) -> None:
        """
        - Convert an array into a max heap
        """
        self.heap = [0]
        self.size = 0
        n = len(array)
        for i in range(n):
            self.insert(array[i])

    def insert(self, value: int) -> None:
        """
        - Insert an element into the heap
        """
        self.heap.append(value)
        self.size += 1
        self.rise(self.size)
        #print("Insert: ", value)
        
    def rise(self, i)-> None:
        """
        Move an element higher up the heap until it satifies the heap propertiy
        """
        while i//2 > 0:
            if self.heap[i] > self.heap[i//2]:
                tmp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = tmp
            i = i//2
            
    def max_child(self, i) -> int:
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i*2] > self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def extract_max(self) -> int:
        """
        Remove the an element
        """
        max_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.fall(1)
        print("Extract max: ", max_value)
        return max_value
    
    def peek(self) -> int:
        """
        - Return the max element
        """
        if self.size > 0:
            return self.heap[1]
        else:
            return("The heap is empty")
    
    def fall(self, i):
        """
        Move an element down the heap until it satifies the heap propertiy
        """
        while (i * 2) <= self.size:
            max_child = self.max_child(i)
            if self.heap[i] < self.heap[max_child]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[max_child]
                self.heap[max_child] = tmp
            i = max_child
  
if __name__ == '__main__':
    H = Max_Heap()
    
    # testing inserting manually 

    # H.insert(3)
    # H.insert(9)
    # H.insert(2)
    # H.insert(1)
    # H.insert(4)
    # H.insert(5)
    # print(H)
    # H.extract_max()
    # print(H)
    
    #  testing max heapyfying a given list

    # a_list = [3,9,2,1,4,5]
    # H.heapify(a_list)
    # print(H)
    # H.extract_max()
    # print(H)
    
    m = [1,2,3,4,5,6]
    H.heapify(m)
    print(H.peek()) # 6
    H.insert(1)
    H.insert(11)
    H.extract_max() # 11
    H.insert(7)
    H.insert(9)
    H.insert(15)
    H.extract_max() # 15 
    print(H)
    

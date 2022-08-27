"""
* Resources:
    - https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

What is a stack
    - A stack is a linear data structure that follows the LIFO principle.
    - A stack is a list of elements where the last element added is the first element to be removed.
"""

class Array_Stack():
    def __init__(self, max_capacity=None) -> None:
        self.length = 0
        self.array = [None] * max_capacity
        
    def __len__(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def clear(self) -> None:
        self.length = 0
        
    def is_full(self) -> bool:
        return len(self) == len(self.array)
    
    def push(self, item) -> None:
        if self.is_full():
            raise Exception("Stack is full")
        self.array[len(self)] = item
        self.length += 1
        
    def pop(self) -> list:
        if self.is_empty():
            raise Exception("Stack is empty")
        self.length -= 1
        print("Popped:", self.array[self.length])
        return self.array[self.length]
    
    def peek(self) -> list:
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.array[self.length-1]
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Stack is empty"
        string = "["
        for i in range(len(self)):
            string += str(self.array[i]) + "|"
        return string[:-1]+"] <- Top"
            
    
if __name__ == '__main__':
    s = Array_Stack(5)
    s.push(10)
    s.push(12)
    s.push(14)
    s.push(141)
    s.push(13)
    print(str(s))
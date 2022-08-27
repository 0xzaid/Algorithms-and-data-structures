
import heapq

class Node:
    def __init__(self, count, char = None):
        self.char = char
        self.count = count
        self.right = None
        self.left = None
        
    def encoding(self, previous):
        if self.left is None and self.right is None:
            yield (self.char, previous)
        else:
            for v in self.left.encoding(previous + '0'):
                yield v
            for v in self.right.encoding(previous + '1'):
                yield v
                        
    def __lt__(self, node):
        return self.count < node.count

class huffman:
    def __init__(self, initial):
        """Construct encoding given initial corpus."""
        self.initial = initial
        self.result = None
        self.count = len(initial)
        self.encoding = []
        
        # Count frequencies
        freq = [0]*255
        for i in initial:
            index = ord(i)
            freq[index] += 1

        # pq construction
        heap = []
        for i in range(len(freq)):
            if freq[i] > 0:
                heap.append(Node(freq[i], chr(i)))
        heapq.heapify(heap)
        
        # huffman algo
        while len(heap) > 1:
            min1 = heapq.heappop(heap)
            min2 = heapq.heappop(heap)
            new_node = Node(min1.count + min2.count)
            new_node.left = min1
            new_node.right = min2
            heapq.heappush(heap, new_node)
    
        start = ''
        i = 0
        for char,count in heap[i].encoding(start):
            self.encoding.append([char,count])
            
        self.encoding = sorted(self.encoding)
        self.result = self.encoding
        self.count = len(self.encoding)
     
    def __call__(self):
        return self.result

    def __getitem__(self, item):
         return self.result[item]
     
    def __len__(self):
        return self.count
    
    def __str__(self):
        return "Result: " + str(sorted(s.encoding, key= lambda x: x[1]))
    
if __name__ == '__main__':
    text = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
    s = huffman(text)
    print(s)
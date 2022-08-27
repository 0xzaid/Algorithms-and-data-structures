import sys

class DisjointSet:
    """
    Disjoint set data structure and operations
    """
    def __init__(self, vertices, file):
        self.v = vertices
        self.parent = []
        self.read_file(file)

    def add_edge(self, u, v, w):
        self.parent.append([u, v, w])
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union_by_rank(self, parent, rank, x, y):
        """ 
        Union by rank/height
        """
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if xroot == yroot:
            return
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            
    
    def union_by_size(self, parent, x, y):
        """ 
        Union by size
        """
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if xroot == yroot:
            return
        
        size_x = -parent[xroot]
        size_y = -parent[yroot]

        if size_x > size_y:
            parent[yroot] = xroot
            parent[xroot] = -(size_x+size_y)
        else:
            parent[xroot] = yroot
            parent[yroot] = -(size_x+size_y)

    def read_file(self, file_name):
        """
        This function reads an input file that contains all the edges, then adds 
        all the edges into the parent array by using the add_edge function
        """
        f = open(file_name)
        file_content = f.read().split('\n')
        data = []
        for i in file_content:
            data.append(i.split())
        edges = int(data[0][1])
        for i in range(1, edges+1):
            u = int(data[i][0])
            v = int(data[i][1])
            w = int(data[i][2])
            self.add_edge(u, v, w)
            
def v_count(file_name):
    """
    This function reads the first number in the input file, which is the number of vertices and returns it.
    """
    f = open(file_name)
    file_content = f.read().split('\n')
    data = []
    for i in file_content:
        data.append(i.split())
    v = int(data[0][0])
    return v
            
if __name__ == '__main__':
    file = "testing/ukkonen_input.txt"
    v_count = v_count(file)
    s = DisjointSet(v_count, file)
    s.union_by_size()
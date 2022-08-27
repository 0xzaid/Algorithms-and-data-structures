"""
Resources
    * https://en.wikipedia.org/wiki/Heapsort

- What is Heap sort
    - comparison based sorting algorithm that works by building a binary tree of the elements and then 
      repeatedly swapping the root element (maximum or minimum) with the last element of the tree.
    * Binary heap:
        - Complete binary tree where all levels are completely filled except the last level
        - Every element in the heap is smaller than its children
    * Steps:
        1. create max heap -- O(n)
        2. Swap first element of the list with the final element, then decrease the range by 1 -- O(1)
        3. Call fall function to heapify the list -- O(log n)
        4. Repeat from step 2 until the range is one element
- Complexity
    - Best case: O(Nlog(N))
    - Average case: O(Nlog(N))
    - Worst case: O(Nlog(N))
    - Space complexity: O(1)
- Stable: Doesn't maintain the relative order among elements
- In-place
"""


def heapSort_heapify(an_array, n, i):
    largest = i 
    left_child = 2*i+1    
    right_child = 2*i+2  
    
    if left_child < n and an_array[largest] < an_array[left_child]:
        largest = left_child
    if right_child < n and an_array[largest] < an_array[right_child]:
        largest = right_child
    if largest != i:
        swap(an_array, i, largest) 
        heapSort_heapify(an_array, n, largest)
  
def heap_sort(a_list):
    n = len(a_list)
    for i in range(n//2, -1, -1):
        heapSort_heapify(a_list, n, i)
    for i in range(n-1, 0, -1):
        swap(a_list, i, 0)
        heapSort_heapify(a_list, i, 0)
    
    return a_list
    
def swap(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]

if __name__ == '__main__':
    random_list = [5,1,6,10,65,25,-15,0,3]
    already_sorted = [1,2,3,4,5,6,7,8,9,10]
    test = [19,5,12,7]
    test_2 = [14514,51,5,15,51,5,1,51,551515515,1523674,46,18551,6,3,74,72,6,3,26,2,76,262,2,6,2,62,6,26,2,7,8,0,8,76,5,4,2,34,8,66457,3,73,73]
    test_3 = [4,2,5,14,11,8,15,13,19,10]
    

    a = heap_sort(random_list)
    print("Final result: " + str(a))
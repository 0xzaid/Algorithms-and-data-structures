"""
- What is Bubble sort
    - Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in wrong order.
    Steps:
        - Start at leftmost element X
        - Compare X to the element Y to its right
        - if X > Y then swap them, otherwise dont+
        - Move one position to the right
- Complexity
    - Best case: O(n)
    - Average case: O(n^2)
    - Worst case: O(n^2)
    - Space complexity: O(1)
- Stable: Maintains the relative order among elements
- Incremental: does not need to re-compute everything after a small change
"""
import random

def bubble_sort(a_list):
    counter = 1
    n = len(a_list)
    for mark in range(n-1, 0, -1):
        for i in range(mark):
            if a_list[i] > a_list[i+1]:
                print("Step " + str(counter) + ": Swapping " +  str(a_list[i]) + " And " + str(a_list[i+1]))
                counter += 1
                swap(a_list, i, i+1)
               
    if counter == 1:
        print("Already sorted!") 
    return a_list

def swap(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]
    
    
if __name__ == '__main__':
    random_list = [5,1,6,10,65,25,-15,0,3]
    already_sorted = [1,2,3,4,5,6,7,8,9,10]
    
    result_1 = bubble_sort(random_list)
    print("Final result: " + str(result_1))
    
    result_2 = bubble_sort(already_sorted)
    print("Final result: " + str(result_2))

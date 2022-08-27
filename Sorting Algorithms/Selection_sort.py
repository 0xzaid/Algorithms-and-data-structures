"""
- What is Selection sort
    - Selection sort is a simple sorting algorithm that works by taking the smallest element in an 
      unsorted array, and bringing it to the front.
    Steps:
        - Start at leftmost element, set as current minimum
        - Traverse the rest and find the minimum element in the rest of the list
        - Swap it with the leftmost unsorted element
- Complexity
    - Best case: O(N^2)
    - Average case: O(N^2)
    - Worst case: O(N^2)
    - Space complexity: O(1)
- Stable: Does not maintain the relative order among elements
- Incremental: Does need to re-compute everything after a small change
"""

def selection_sort(a_list):
    counter = 1
    n = len(a_list)
    for mark in range(n-1):
        min_index = Find_Min_Element_Pos(a_list, mark, n)
        counter += 1
        print("Step " + str(counter) + ": Swapping " +  str(a_list[mark]) + " And " + str(a_list[min_index]))
        Swap(a_list, mark, min_index)
    return a_list

def Find_Min_Element_Pos(a_list, mark, n):
    pos_min = mark
    for i in range(mark+1, n):
        if a_list[i] < a_list[pos_min]:
            pos_min = i
    return pos_min
    
def Swap(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]

if __name__ == '__main__':
    random_list = [5,1,6,10,65,25,-15,0,3]
    already_sorted = [1,2,3,4,5,6,7,8,9,10]
    
    result_1 = selection_sort(random_list)
    print("Final result: " + str(result_1))
    
    result_2 = selection_sort(already_sorted)
    print("Final result: " + str(result_2))
"""
- What is Insertion sort
    - Insertion sort is a sorting algorithm that works by creating the final sorted array one element at a time
    Steps:
        - Split the list into
            - Part S (already sorted -- initialy one element)
            - Part U (Unsorted)
        - Extend S by taking any element from U and inserting it in S maintaining the order
- Complexity
    - Best case: O(N)
    - Average case: O(N^2)
    - Worst case: O(N^2)
    - Space complexity: O(1)
- Stable: Does maintain the relative order among elements
- Incremental: Doesn't need to re-compute everything after a small change
"""

def insertion_sort(a_list):
    counter = 1
    n = len(a_list)
    for mark in range(1, n):
        temp = a_list[mark]
        i = mark-1
        while i >= 0 and a_list[i] > temp:
            print("Step " + str(counter) + ": Swapping " +  str(a_list[i]) + " And " + str(temp))
            a_list[i+1] = a_list[i]
            i -= 1
            counter += 1
        a_list[i+1] = temp
    if counter == 1:
        print( str(a_list) + " is Already sorted!")
    return a_list
 
if __name__ == '__main__':
    random_list = [5,1,6,10,65,25,-15,0,3]
    already_sorted = [1,2,3,4,5,6,7,8,9,10]
    test = [19,5,12,7]
    
    result_1 = insertion_sort(random_list)
    print("Final result: " + str(result_1))
    
    result_2 = insertion_sort(already_sorted)
    print("Final result: " + str(result_2))
    
    result_3 = insertion_sort(test)
    print("Final result: " + str(result_3))
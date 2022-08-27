"""
- What is Quick sort
    - Quick sort is a divide and conquer algorithm, it picks a pivot element and partitions the list into two sublists
      then the sublists are sorted recursively
    - Using Hoae partition scheme
    Steps:
        - Choose a pivot
        - Partition the list into two sublists where left elements are less or equal to 
          pivot and right elements are greater than the pivot
        - quick sort left sublist, then right sublist
- Complexity
    - Best case: O(Nlog(N))
    - Average case: O(Nlog(N))
    - Worst case: O(N^2)
    - Space complexity: O(log(N))
- Stable: Doesn't maintain the relative order among elements
- In-place
"""
COUNTER = 0 

def quick_sort(a_list, lo, hi):
    global COUNTER
    if lo >= hi: return a_list
    
    pivot = hoare_partitioning_scheme(a_list, lo, hi)
    COUNTER += 1
    print("Partition(" + str(COUNTER) + "): "+ str(a_list[lo:hi+1]) + "\n" + "pivot: " + str(a_list[pivot]) + "\n")
    quick_sort(a_list, lo, pivot)
    quick_sort(a_list, pivot+1, hi)
    

def hoare_partitioning_scheme(a_list, lo, hi):
    pivot = a_list[(lo+hi)//2]
    i,j = lo-1, hi+1
    
    while True:
 
        while True:
            i = i + 1
            if a_list[i] >= pivot:
                break
 
        while True:
            j = j - 1
            if a_list[j] <= pivot:
                break
 
        if i >= j:
            return j
 
        swap(a_list, i, j)
            
def swap(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]

if __name__ == '__main__':
    random_list = [5,1,6,10,65,25,-15,0,3]
    already_sorted = [1,2,3,4,5,6,7,8,9,10]
    test = [19,5,12,7]
    test_2 = [14514,51,5,15,51,5,1,51,551515515,1523674,46,18551,6,3,74,72,6,3,26,2,76,262,2,6,2,62,6,26,2,7,8,0,8,76,5,4,2,34,8,66457,3,73,73]
    test_3 = [4,2,5,14,11,8,15,13,19,10]
    

    # quick_sort(random_list, 0 , len(random_list)-1)
    # print("Final result: " + str(random_list))
    
    # quick_sort(already_sorted, 0 , len(already_sorted)-1)
    # print("Final result: " + str(already_sorted))

    # quick_sort(test, 0 , len(test)-1)
    # print("Final result: " + str(test))
    
    # quick_sort(test_2, 0, len(test_2)-1)
    # print("Final result: " + str(test_2))
    
    quick_sort(test_3, 0 , len(test_3)-1)
    print("Final result: " + str(test_3))
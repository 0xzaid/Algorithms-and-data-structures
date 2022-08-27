"""
- What is Merge sort
    - Merge sort is a divide-and-conquer sorting algorithm that sorts a given sequence by dividing it
      into two halves, sorting those halves and then merging the sorted halves back together
    Steps:
        - Divide list into two sublists until base case is reached
        - Sort each sublist recursively
        - Recombine each sorted sublist into the final sorted list
- Complexity
    - Best case: O(Nlog(N))
    - Average case: O(Nlog(N))
    - Worst case: O(Nlog(N))
    - Space complexity: O(n)
- Stable: Does maintain the relative order among elements
- Not in-place
"""
# global variable merge counter to keep track of how many times merge function is called 
MERGE_COUNTER = 0 

def merge_sort(a_list):
    global MERGE_COUNTER
    
    if len(a_list) <= 1:
        return a_list
    else:
        # get mid
        middle = len(a_list) // 2
        
        # sorts left_sublist
        left_sublist = merge_sort(a_list[:middle])
        # sorts right_sublist
        right_sublist = merge_sort(a_list[middle:])
        
        MERGE_COUNTER += 1
        print("Merge(" + str(MERGE_COUNTER) + "): "+ str(left_sublist) + " <---> " + str(right_sublist))
        
        # merge sublists
        return merge(left_sublist, right_sublist)

def merge(left_sublist, right_sublist):
    i, j = 0, 0
    result = []
    
    while i < len(left_sublist) and j < len(right_sublist):
        if left_sublist[i] > right_sublist[j]:
            result.append(right_sublist[j])
            j += 1
       
        elif left_sublist[i] < right_sublist[j]:
            result.append(left_sublist[i])
            i += 1

        else:
            result.append(left_sublist[i])
            result.append(right_sublist[j])
            i += 1
            j += 1
            
    while i < len(left_sublist):
        result.append(left_sublist[i])
        i += 1
        
    while j < len(right_sublist):
        result.append(right_sublist[j])
        j += 1
        
    return result

if __name__ == '__main__':
    random_list = [5,1,6,10,65,25,-15,0,3]
    already_sorted = [1,2,3,4,5,6,7,8,9,10]
    test = [19,5,12,7]
    
    result_1 = merge_sort(random_list)
    print("Final result: " + str(result_1))
    
    result_2 = merge_sort(already_sorted)
    print("Final result: " + str(result_2))
    
    result_3 = merge_sort(test)
    print("Final result: " + str(result_3))
    

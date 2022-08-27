""""
Binary search algorithm

For binary search to work, first we need the list to be sorted.
Gonna use selection sort for that.
"""

from selection_sort import selection_sort

def binary_search(sorted_list, target):
    """
    :time complexity: O(logN)
    :space complexity: O(1)
    """
    length = len(sorted_list)
    left = 0
    right = length-1
    while left <= right:
        mid = (left+right)//2
        if sorted_list[mid] < target:
            left = mid + 1
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            return mid
    return "Not found"


def main():
    a_list = [5,1,6,10,65,25,-15,0,3]
    sorted_list = selection_sort(a_list)
    target = 5
    print("The sorted list is: " + str(sorted_list))
    print("The target item [" + str(target) + "] is at position: " + str(binary_search(sorted_list, target)))

if __name__ == '__main__':
    main()
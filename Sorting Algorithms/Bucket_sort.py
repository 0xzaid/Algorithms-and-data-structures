"""
Bucket sort is an efficient sorting algorithm that works by distributing elements into a number of "buckets," 
then sorting the elements within each bucket. It is a distribution sort, meaning that it works by distributing
the elements of the input list into a number of "buckets," then sorting the elements within each bucket.

Steps:
    1. Create an empty array of buckets
    2. Scatter: Go over the original array, putting each object in its bucket
    3. Sort each non-empty bucket
    4. Gather: Visit the buckets in order and put all elements back into the original array

Complexity:
    - Best case: O(N)
        where n is the number of elements in the input array. This is because the time taken to sort the 
        elements within each bucket is constant, so the overall time complexity is linear.
    - Worst case: O(N^2) or O(NlogN)
        based on the sorting algorithm used to sort each bucket
        O(N^2) if the sorting algorithm used is Insertion sort
        O(NlogN) if the sorting algorithm used is Merge sort
        
Bucket sort is stable, meaning that it preserves the relative order of elements with equal keys.

Optimizations for Bucket sort:
    - Use larger buckets to reduce the number of buckets
    - Use a different sorting algorithm for each bucket like merge sort or quick sort
    
"""

from Insertion_sort import insertion_sort


def bucket_sort(arr, k=10):
    # Get the max value in the array
    max_val = max(arr)
    min_val = min(arr)

    # Create k empty buckets
    buckets = [[] for _ in range((max_val - min_val) // k + 1)]

    # Place each element in the appropriate bucket
    for i in range(len(arr)):
        buckets[(arr[i] - min_val) // k].append(arr[i])

    # Sort each bucket using insertion sort
    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    # Concatenate the sorted buckets
    sorted_arr = []
    for i in range(len(buckets)):
        sorted_arr.extend(buckets[i])

    return sorted_arr


if __name__ == '__main__':
    random_list = [5, 1, 6, 10, 65, 25, -15, 0, 3]
    result = bucket_sort(random_list)
    print(result)

    # Test case 1
    arr = [3, 1, 4, 2, 5]
    assert bucket_sort(arr) == [1, 2, 3, 4, 5]

    # Test case 2
    arr = [3, 1, 4, 2, 5, 2]
    assert bucket_sort(arr) == [1, 2, 2, 3, 4, 5]

    # Test case 3
    arr = [3, 1, 4, 2, 5, 2, 6]
    assert bucket_sort(arr) == [1, 2, 2, 3, 4, 5, 6]

    # Test case 4
    arr = [3, 1, 4, 2, 5, 2, 6, 7]
    assert bucket_sort(arr) == [1, 2, 2, 3, 4, 5, 6, 7]

    # Test case 5
    arr = [3, 1, 4, 2, 5, 2, 6, 7, 8]
    assert bucket_sort(arr) == [1, 2, 2, 3, 4, 5, 6, 7, 8]

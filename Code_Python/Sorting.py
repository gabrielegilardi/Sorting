"""
Lists and Arrays Sorting and Searching Methods

Copyright (c) 2021 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Sorting and searching functions implementation for lists and arrays.
- Lists (strings or numbers) work with any sorting method.
- Numpy arrays work with any sorting method but heap and merge sort.
- Possible to sort using the specific method or using a general function.
- Possible to specify a descending sorting direction, the gap parameter in the
  shell short method, and the pivot element in the quick sort method.
- Possible to sort in place and to build the index array.
- Duplicates items are allowed.
- Examples of usage are at the end of the file.

Orders
------
Bubble sort             O(N^2).
Short bubble sort       O(N^2), but may stop early.
Selection sort          O(N^2).
Insertion sort          O(N^2).
Shell sort              Between O(N) and O(N^2).
Heap sort               O(N log N)
Quick sort              O(N log N), but may degrade to O(N^2).
Merge sort              O(N log N), but requires additional space.
Sequential search       O(N) for ordered/unordered lists.
Binary search           O(log N) for ordered (ascending) lists.

Functions
---------
partition               Recursively partition and sort a list.
bubble_sort             Sorts a list using the bubble sort method.
short_bubble_sort       Sorts a list using the short-bubble sort method.
selection_sort          Sorts a list using the selection sort method.
insertion_sort          Sorts a list using the insertion sort method.
shell_sort              Sorts a list using the shell sort method.
heap_sort               Sorts a list using a binary heap.
quick_sort              Sorts a list using the quick sort method.
merge_sort              Sorts a list using recursively the merge sort method.
reverse                 Reverses a list/array.
binary_search           Searches a value in a (sorted) list.
sequential_search       Searches a value in a list.
build_index             Returns the index array.
sort                    Sorts a list/array using the specified method.

References
----------
- "Problem Solving with Algorithms and Data Structures", by Miller and Ranum,
  @ runestone.academy/runestone/books/published/pythonds/index.html
- Binary heap class:
  @ github.com/gabrielegilardi/DataStructures.git
"""


import numpy as np
from BinaryHeap import BinaryHeap


def partition(a, start, end, fact):
    """
    Recursively partition and sort a list (used by the quick sort method).

    Note: argument <fact> must be between 0 and 1, with 0 specifying the
          starting point <start> and 1 the ending point <end>.
    """
    if (start < end):

        # Determine the index of the pivot and put the pivot as first element
        idx = int(fact * (end - start) + start)
        a[start], a[idx] = a[idx], a[start]

        pivot = a[start]
        left = start + 1
        right = end

        # Find the split point
        while (True):

            # Move the left mark up
            while (left <= right and a[left] <= pivot):
                left += 1

            # Move the right mark down
            while (right >= left and a[right] >= pivot):
                right -= 1

            # Marks crossed --> the right mark is the split point
            if (right < left):
                a[start], a[right] = a[right], a[start]
                break

            # Marks did not cross --> switch the two elements
            else:
                a[left], a[right] = a[right], a[left]

        # Partition the left side
        partition(a, start, right-1, fact)

        # Partition the right side
        partition(a, right+1, end, fact)


def bubble_sort(a):
    """
    Sorts a list using the bubble sort method.
    """
    for n_pass in range(len(a)-1, 0, -1):

        for i in range(n_pass):

            # Swap elements
            if (a[i] > a[i+1]):
                a[i+1], a[i] = a[i], a[i+1]


def short_bubble_sort(a):
    """
    Sorts a list using the short-bubble sort method.
    """
    for n_pass in range(len(a)-1, 0, -1):
        is_sorted = True

        for i in range(n_pass):

            # Swap elements
            if (a[i] > a[i+1]):
                a[i+1], a[i] = a[i], a[i+1]
                is_sorted = False

        # Stop if the list is already fully sorted
        if (is_sorted):
            break


def selection_sort(a):
    """
    Sorts a list using the selection sort method.
    """
    for n_pass in range(len(a)-1, 0, -1):
        i_max = 0

        # Search the max. element
        for i in range(1, n_pass+1):
            if (a[i] > a[i_max]):
                i_max = i

        # Swap current and max. element
        a[i_max], a[n_pass] = a[n_pass], a[i_max]


def insertion_sort(a, start=0, gap=1):
    """
    Sorts a list using the insertion sort method.
    """
    for n_pass in range(start+gap, len(a), gap):

        value = a[n_pass]       # Current value
        j = n_pass

        # Shift the elements while searching the insertion point
        while (j >= gap and a[j-gap] > value):
            a[j] = a[j-gap]
            j -= gap

        # Insert the current value
        a[j] = value


def shell_sort(a, gap=1):
    """
    Sorts a list using the shell sort method.
    """
    n_lists = len(a) // gap

    # Sort the sub-lists
    for i in range(n_lists+1):
        start = n_lists * i
        insertion_sort(a, start=start, gap=gap)

    # Sort the sorted sub-lists
    insertion_sort(a, start=0, gap=1)


def heap_sort(a):
    """
    Sorts a list using a binary heap.
    """
    # Create the binary heap
    heap = BinaryHeap(a)

    # Build the sorted list
    for i in range(len(a)):
        a[i] = heap.get()


def quick_sort(a, fact=0):
    """
    Sorts a list using the quick sort method.
    """
    partition(a, 0, len(a)-1, fact)


def merge_sort(a):
    """
    Sorts a list recursively using the merge sort method.
    """
    if (len(a) > 1):

        # Split the list
        m = len(a) // 2
        left = a[:m]
        right = a[m:]

        # Split and merge the left and right sides
        merge_sort(left)
        merge_sort(right)

        # Merge the lists
        i = 0
        j = 0
        k = 0

        # Compare elements between left and right side
        while (i < len(left) and j < len(right)):

            # If the left element is smaller
            if (left[i] < right[j]):
                a[k] = left[i]
                i += 1

            # Otherwise
            else:
                a[k] = right[j]
                j += 1
            k += 1

        # Complete the left side
        while (i < len(left)):
            a[k] = left[i]
            i += 1
            k += 1

        # Complete the right side
        while (j < len(right)):
            a[k] = right[j]
            j += 1
            k += 1


def reverse(a):
    """
    Reverses a list/array.
    """
    for i in range(len(a) // 2):
        a[i], a[-1-i] = a[-1-i], a[i]


def binary_search(a, value):
    """
    Searches a value in a (sorted) list. Return the index if found, otherwise
    returns <None>.
    """
    start = 0
    end = len(a) - 1

    while (start <= end):

        i = (start + end) // 2          # Middle point

        # If found the value
        if (a[i] == value):
            return i

        # If not found the value
        else:
            if (a[i] > value):
                end = i - 1             # Check left side
            else:
                start = i + 1           # Check right side

    return None


def sequential_search(a, value):
    """
    Searches a value in a list. Return the index if found, otherwise returns
    <None>.
    """
    for i in range(len(a)):

        # If found the value
        if (a[i] == value):
            return i

    return None


def build_index(a_sorted, a_original):
    """
    Returns the index array.
    """
    n = len(a_sorted)
    idx = np.zeros(n, dtype=int)

    # sorted[index] --> original
    for i in range(n):
        idx[i] = sequential_search(a_sorted, a_original[i])

    # original[index] --> sorted
    return idx[idx]


def sort(data, method='merge', descending=False, param=None):
    """
    Sorts a list or array using the specified method. Returns also the index
    array.
    """
    # Make a copy
    a = data.copy()

    # Sort (in place) the list
    if (method == 'bubble'):
        bubble_sort(a)

    elif (method == 'short_bubble'):
        short_bubble_sort(a)

    elif (method == 'selection'):
        selection_sort(a)

    elif (method == 'insertion'):
        insertion_sort(a, start=0, gap=1)

    elif (method == 'shell'):
        gap = 1 if (param is None) else param
        shell_sort(a, gap)

    elif (method == 'quick'):
        fact = 0 if (param is None) else param
        quick_sort(a, fact)

    elif (method == 'heap'):
        heap_sort(a)

    else:
        merge_sort(a)

    # Build the index array
    idx = build_index(a, data)

    # Reverse it if wanted in descending order
    if (descending):
        reverse(a)
        reverse(idx)

    return a, idx


if __name__ == '__main__':
    """
    Test the sorting and searching functions.
    """
    a1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]           # List
    a2 = ['d', 'f', 'a', 'k', 'b', 'g', 'z']            # List
    a3 = np.asarray(a1)                                 # Array

    print('\n==== Sort lists using the main function')
    # sorted = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # index = [3 8 1 5 6 0 7 4 2]

    print('\nBubble sort:')
    a1_sorted, a1_idx = sort(a1, method='bubble')
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nShort bubble sort:')
    a1_sorted, a1_idx = sort(a1, method='short_bubble')
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nSelection sort:')
    a1_sorted, a1_idx = sort(a1, method='selection')
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nInsertion sort:')
    a1_sorted, a1_idx = sort(a1, method='insertion')
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nShell sort (with gap of 3):')
    a1_sorted, a1_idx = sort(a1, method='shell', param=3)
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nQuick sort (with 1st element as pivot):')
    a1_sorted, a1_idx = sort(a1, method='quick', param=0)
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nHeap sort:')
    a1_sorted, a1_idx = sort(a1, method='heap')
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nMerge sort (default method):')
    a1_sorted, a1_idx = sort(a1, method='merge')
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nExample with descending order (using merge sort):')
    # sorted = [93, 77, 55, 54, 44, 31, 26, 20, 17]
    # index = [2 4 7 0 6 5 1 8 3]
    a1_sorted, a1_idx = sort(a1, descending=True)
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nExample with strings (using heap sort):')
    # sorted = ['a', 'b', 'd', 'f', 'g', 'k', 'z']
    # index = [0 5 2 4 3 1 6]
    a2_sorted, a2_idx = sort(a2, method='heap')
    print('sorted = ', a2_sorted)
    print('index = ', a2_idx)

    print('\nExample with arrays (using shell sort, with gap of 2):')
    # sorted = [17 20 26 31 44 54 55 77 93]
    # index = [3 8 1 5 6 0 7 4 2]
    a3_sorted, a3_idx = sort(a3, method='shell')
    print('sorted = ', a3_sorted)
    print('index = ', a3_idx)

    print('\n==== Sort lists using directly the functions')

    print('\nExample without index array (using insertion sort):')
    # sorted = [17 20 26 31 44 54 55 77 93]
    insertion_sort(a3_sorted)                   # Sort
    print('sorted = ', a3_sorted)

    print('\nExample with index array (using bubble sort):')
    # sorted = [17 20 26 31 44 54 55 77 93]
    # index = [3 8 1 5 6 0 7 4 2]
    a1_sorted = a1.copy()                       # Make a copy (needed for idx)
    bubble_sort(a1_sorted)                      # Sort
    a1_idx = build_index(a1_sorted, a1)         # Index array
    print('sorted = ', a1_sorted)
    print('index = ', a1_idx)

    print('\nExample with descending order (using heap sort):')
    # sorted = ['z', 'k', 'g', 'f', 'd', 'b', 'a']
    # index = [6 1 3 4 2 5 0]
    heap_sort(a2_sorted)                        # Sort
    reverse(a2_sorted)                          # Reverse
    print('sorted = ', a2_sorted)
    print('index = ', a2_idx)

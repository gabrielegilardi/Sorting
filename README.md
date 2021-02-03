# Sorting and Searching

Sorting and searching functions for lists and arrays.

## References

[Problem Solving with Algorithms and Data Structures](https://runestone.academy/runestone/books/published/pythonds/index.html), by Miller and Ranum.

## Files

`Sorting.py` Implementation of sorting and searching functions for lists and arrays.

```python
"""
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
"""
```

- Written and tested in Python 3.8.5.

- Lists (strings or numbers) work with any sorting method.

- Numpy arrays work with any sorting method but heap and merge sort.

- Possible to:

  - Sort using the specific method or using the general function *sort*.

  - Specify a descending sorting direction.

  - Specify the gap parameter in the shell short method.
  
  - Specify the pivot element in the quick sort method.

  - Sort in place.
  
  - Build the index array.

  - Have duplicates items.

`BinaryHeap.py` Min/max binary heap data structure implementation using lists (see [here](https://github.com/gabrielegilardi/DataStructures.git)).

## Examples

Examples of usage are at the end of the file.

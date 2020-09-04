import random as rnd
import sorting_algorithms as sa


def print_array(arraytype, array):
    print('Array sorted by ' + str(arraytype) + ": " + str(array))
    print("""
    --------------------*******--------------------
    """)

unsorted_array = []
for i in range(10):
    unsorted_array.append(rnd.randint(0, 250))
print("unsorted array: " + str(unsorted_array))
print("______________________________________\n")

mergesort = sa.MergeSort
sorted_array = sa.MergeSort.sort(unsorted_array)
print_array('mergesort', sorted_array)
print_array('unsorted', unsorted_array)

quicksort = sa.QuickSort
sorted_array = quicksort.sort(unsorted_array, 0, len(unsorted_array)-1)
print_array('quicksort   ', sorted_array)
print_array('unsorted', unsorted_array)

insertionsort = sa.InsertionSort
sorted_array = insertionsort.sort(unsorted_array, len(unsorted_array)-1)
print_array('insertionsort', sorted_array)
print_array('unsorted', unsorted_array)

bubblesort = sa.BubbleSort
sorted_array = bubblesort.sort(unsorted_array)
print_array('bubblesort', sorted_array)
print_array('unsorted', unsorted_array)
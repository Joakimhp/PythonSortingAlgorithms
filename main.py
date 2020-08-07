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
print_array('mergesort', unsorted_array)

mergesort = sa.MergeSort
sorted_array = mergesort.sort(unsorted_array)
print("Array sorted by mergesort: " + str(sorted_array))

quicksort = sa.QuickSort
sorted_array = quicksort.sort(unsorted_array, 0, len(unsorted_array)-1)
print_array('quicksort', sorted_array)
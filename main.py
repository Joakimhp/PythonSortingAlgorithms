import random as rnd
import sorting_algorithms as sa

unsorted_array = []
for i in range(10):
    unsorted_array.append(rnd.randint(0, 250))
print("Unsorted array: " + str(unsorted_array))


mergesort = sa.MergeSort()
sorted_array = mergesort.sort(unsorted_array)
print("Array sorted by mergesort: " + str(sorted_array))

import random as rnd

unsorted_array = []
for i in range(10):
    unsorted_array.append(rnd.randint(0, 250))
print("Unsorted array: " + str(unsorted_array))

from mergesort import MergeSort

mergesort = MergeSort()
sorted_array = mergesort.sort(unsorted_array)
print("Array sorted by mergesort: " + str(sorted_array))

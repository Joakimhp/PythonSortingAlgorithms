from sorting_superclass import SortingAlgorithm
from copy import deepcopy

class BubbleSort(SortingAlgorithm):
    local_array = []

    def set_array(self, arr):
        self.local_array = deepcopy(arr)

    def sort(self, arr):
        self.set_array(arr)

        array_length = len(self.local_array)

        for iteration in range(array_length-1):
            current_index = 0
            while current_index < (array_length - iteration - 1):
                if self.local_array[current_index] > self.local_array[current_index+1]:
                    self.local_array[current_index], self.local_array[current_index + 1] = \
                        self.local_array[current_index + 1], self.local_array[current_index]
                current_index += 1
        return self.local_array

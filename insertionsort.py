from sorting_superclass import SortingAlgorithm
from copy import deepcopy

class InsertionSort(SortingAlgorithm):
    local_array = []

    def set_array(self, arr):
        self.local_array = deepcopy(arr)

    def sort(self, arr, current_number_index):
        self.set_array(arr)
        if current_number_index > 0:
            self.sort(self.local_array, current_number_index - 1)
            current_number = self.local_array[current_number_index]
            shiftingIndex = current_number_index - 1
            while shiftingIndex >= 0 and self.local_array[shiftingIndex] > current_number:
                self.local_array[shiftingIndex + 1] = self.local_array[shiftingIndex]
                shiftingIndex -= 1
            self.local_array[shiftingIndex + 1] = current_number
        return self.local_array
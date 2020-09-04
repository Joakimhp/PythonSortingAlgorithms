from sorting_superclass import SortingAlgorithm
from copy import deepcopy

class QuickSort(SortingAlgorithm):
    local_array = []

    def set_array(self, arr):
        self.local_array = deepcopy(arr)

    #Using Lommuto partition scheme
    def sort(self, arr, index_low, index_high):
        self.set_array(arr)
        #print("1us" + str(arr) + " - sa" + str(self.local_array))
        if index_low < index_high:
            #print("2us" + str(arr) + " - sa" + str(self.local_array))
            p = self.partition(index_low, index_high)
            self.sort(self.local_array, index_low, p - 1)
            self.sort(self.local_array, p + 1, index_high)
        return self.local_array

    def partition(self, index_low, index_high):
        pivot = self.local_array[index_high]
        i = index_low
        for j in range(index_low, index_high):
            if self.local_array[j] < pivot:
                self.local_array[i], self.local_array[j] = self.local_array[j], self.local_array[i]
                i = i+1
        self.local_array[i], self.local_array[index_high] = self.local_array[index_high], self.local_array[i]
        return i

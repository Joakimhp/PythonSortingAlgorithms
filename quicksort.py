from sorting_superclass import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    #Using Lommuto partition scheme
    def sort(self, arr, indexLow, indexHigh):
        if indexLow < indexHigh:
            p = self.partition(arr, indexLow, indexHigh)
            self.sort(arr, indexLow, p-1)
            self.sort(arr, p+1, indexHigh)
        return arr

    def partition(self, arr, indexLow, indexHigh):
        pivot = arr[indexHigh]
        i = indexLow
        for j in range(indexLow, indexHigh):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i = i+1
        arr[i], arr[indexHigh] = arr[indexHigh], arr[i]
        return i

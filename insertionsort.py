from sorting_superclass import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    def sort(self, arr, current_number_index):
        if current_number_index > 0:
            self.sort(arr, current_number_index - 1)
            current_number = arr[current_number_index]
            shiftingIndex = current_number_index - 1
            while shiftingIndex >= 0 and arr[shiftingIndex] > current_number:
                arr[shiftingIndex + 1] = arr[shiftingIndex]
                shiftingIndex -= 1
            arr[shiftingIndex + 1] = current_number
        return arr
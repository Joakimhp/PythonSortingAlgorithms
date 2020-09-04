from sorting_superclass import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    def sort(self, arr):
        if len(arr) > 1:
            splitone, splittwo = self.split(arr)
            mergeone = self.sort(splitone)
            mergetwo = self.sort(splittwo)
            return self.merge(mergeone, mergetwo)
        else:
            return arr

    def split(self, arr):
        splitone = arr[0:len(arr) // 2]
        splittwo = arr[(len(arr) // 2):len(arr)]
        return splitone, splittwo

    def merge(self, arrone, arrtwo):
        merged_array = []
        while len(arrone) > 0 or len(arrtwo) > 0:
            if len(arrone) > 0 and len(arrtwo) > 0:
                if arrone[0] < arrtwo[0]:
                    merged_array.append(arrone.pop(0))
                else:
                    merged_array.append(arrtwo.pop(0))
            elif len(arrone) == 0:
                merged_array.append(arrtwo.pop(0))
            else:
                merged_array.append(arrone.pop(0))
        return merged_array

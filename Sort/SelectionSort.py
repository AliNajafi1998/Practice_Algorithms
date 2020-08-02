from Sort.utils import Utils


class SelectionSort:
    def __init__(self, array: list):
        self.array = array

    def sort(self):
        length = len(self.array)
        for i in range(0, length):
            min_index = i
            for j in range(i + 1, length):
                if Utils.is_lt(self.array, j, min_index):
                    min_index = j
            Utils.exchange(self.array, min_index, i)


if __name__ == '__main__':
    test_array = [-13, 15, 10, 4, 5]
    selection_sort = SelectionSort(test_array)
    selection_sort.sort()
    print(selection_sort.array)

from Sort.utils import Utils


class InsertionSort:
    def __init__(self, array: list):
        self.array = array

    def sort(self):
        length = len(self.array)
        for i in range(1, length):
            j = i
            while j > 0 and Utils.is_lt(self.array, j, j - 1):
                Utils.exchange(self.array, j, j - 1)
                j -= 1


if __name__ == '__main__':
    test_array = [-13, 15, 10, 4, 5]
    insertion_sort = InsertionSort(test_array)
    insertion_sort.sort()
    print(insertion_sort.array)

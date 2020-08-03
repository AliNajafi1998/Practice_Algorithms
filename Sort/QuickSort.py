from Sort.utils import Utils


class QuickSort:
    def __init__(self, array: list):
        self.array = array

    def partition(self, low, high):
        i = low
        j = high + 1
        v = low
        while True:
            i += 1
            while Utils.is_lt(self.array, i, v):
                i += 1
                if i == high:
                    break
            j -= 1
            while Utils.is_lt(self.array, v, j):
                j -= 1
                if j == low:
                    break
            if i >= j:
                break
            Utils.exchange(self.array, i, j)

        Utils.exchange(self.array, low, j)
        return j

    def sort(self, low, high):
        if high <= low:
            return
        j = self.partition(low, high)
        self.sort(low, j - 1)
        self.sort(j + 1, high)


if __name__ == '__main__':
    test_array = [-13, 314, 13333, 15, 10, 4, 5, 5]
    quick_sort = QuickSort(test_array)
    quick_sort.sort(0, len(test_array) - 1)
    print(quick_sort.array)

from Sort.utils import Utils


class MergeSort:
    def __init__(self, array: list):
        self.array = array
        self.temp_array = [None for _ in range(len(self.array))]

    def merge(self, low, mid, high):
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            self.temp_array[k] = self.array[k]
        for k in range(low, high + 1):
            if i > mid:
                self.array[k] = self.temp_array[j]
                j += 1
            elif j > high:
                self.array[k] = self.temp_array[i]
                i += 1
            elif Utils.is_lt(self.temp_array, j, i):
                self.array[k] = self.temp_array[j]
                j += 1
            else:
                self.array[k] = self.temp_array[i]
                i += 1

    def sort(self, low, high):
        if high <= low:
            return
        mid = low + (high - low) // 2
        self.sort(low, mid)
        self.sort(mid + 1, high)
        self.merge(low, mid, high)


if __name__ == '__main__':
    test_array = [-13, 15, 10, 4, 5, 5]
    merge_sort = MergeSort(test_array)
    merge_sort.sort(0, len(test_array) - 1)
    print(merge_sort.array)

from Sort.utils import Utils


class ShellSort:
    def __init__(self, array: list):
        self.array = array

    def sort(self):
        length = len(self.array)
        h = 1
        while h < length / 3:
            h = h * 3 + 1
        while h >= 1:
            for i in range(h, length):
                j = i
                while j >= h and Utils.is_lt(self.array, j, j - h):
                    Utils.exchange(self.array, j, j - h)
                    j -= h
            h //= 3


if __name__ == '__main__':
    test_array = [-13, 15, 10, 4, 5]
    shell_sort = ShellSort(test_array)
    shell_sort.sort()
    print(shell_sort.array)

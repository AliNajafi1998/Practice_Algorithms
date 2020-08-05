class BinarySearch:
    def __init__(self, array: list):
        self.array = array

    def search(self, value):
        return self.search_value(0, len(self.array) - 1, value)

    def search_value(self, low, high, value):
        if low > high:
            return None
        mid = low + (high - low) // 2
        if abs(self.array[mid] - value) < 1e-9:
            return mid
        elif self.array[mid] > value:
            return self.search_value(low, mid - 1, value)
        elif self.array[mid] < value:
            return self.search_value(mid + 1, high, value)


if __name__ == '__main__':
    sorted_arr = [0, 1, 2, 3, 4, 5, 6]
    bs = BinarySearch(sorted_arr)
    print(bs.search(5))

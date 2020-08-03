from Sort.utils import Utils


class PriorityQueue:
    def __init__(self):
        self.items = [None]

    def pop_max(self):
        N = len(self.items)
        if N > 1:
            max_value = self.items[1]
            Utils.exchange(self.items, 1, N - 1)
            del self.items[N - 1]
            self.sink_down(1)
            return max_value
        else:
            return None

    def insert(self, value):
        self.items.append(value)
        N = len(self.items)
        self.swim_up(N - 1)

    def sink_down(self, key):
        N = len(self.items) - 1
        while 2 * key <= N:
            j = key * 2
            if j < N and Utils.is_lt(self.items, j, j + 1):
                j += 1
            if Utils.is_lt(self.items, j, key):
                break
            Utils.exchange(self.items, key, j)
            key = j

    def swim_up(self, key):
        while key > 1 and Utils.is_lt(self.items, key // 2, key):
            Utils.exchange(self.items, key // 2, key)
            key //= 2

    def sort(self):
        sorted_values = []
        while True:
            value = self.pop_max()
            if value is None:
                break
            else:
                sorted_values.append(value)
        return sorted_values


if __name__ == '__main__':
    test_array = [-13, 15, 10, 4, 5, 5]
    pq = PriorityQueue()
    for item in test_array:
        pq.insert(item)

    print(pq.sort())

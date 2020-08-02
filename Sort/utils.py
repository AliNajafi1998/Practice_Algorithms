class Utils:
    @staticmethod
    def exchange(array: list, index_1: int, index_2: int) -> None:
        array[index_1], array[index_2] = array[index_2], array[index_1]

    @staticmethod
    def is_lt(array: list, index_1: int, index_2: int) -> bool:
        return array[index_1] < array[index_2]

    @staticmethod
    def is_sorted(array: list) -> bool:
        for i in range(1, len(array)):
            if Utils.is_lt(array, i, i - 1):
                return False
        return True

class MinEditDistance:
    def __init__(self, source_str: str, target_str: str):
        self.source_str = source_str
        self.target_str = target_str

        self.remove_cost = 1
        self.insertion_cost = 1

        self.table = [[0 for _ in range(len(target_str) + 1)] for _ in range(len(source_str) + 1)]

        self.table[0][0] = 0
        for i in range(1, len(self.table)):
            self.table[i][0] = self.table[i - 1][0] + self.remove_cost

        for j in range(1, len(self.table[0])):
            self.table[0][j] = self.table[0][j - 1] + self.insertion_cost

        for i in range(1, len(self.table)):
            for j in range(1, len(self.table[0])):
                self.table[i][j] = min(self.table[i - 1][j] + self.remove_cost,
                                       self.table[i - 1][j - 1] + (0 if source_str[i - 1] == target_str[j - 1] else 2),
                                       self.table[i][j - 1] + self.insertion_cost
                                       )

        for i in range(len(self.table)):
            print(self.table[i])

        self.result = self.table[len(source_str)][len(target_str)]


if __name__ == '__main__':
    min_edit_distance = MinEditDistance("intention", "execution")
    print(min_edit_distance.result)

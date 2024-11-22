class DataStructure(): # A Datastructure that supports insert_first, insert_last, delete_first and delete_last
    def __init__(self, data=[]):
        self.data = data

    def insert_first(self, element):
        self.data.insert(0, element)

    def insert_last(self, element):
        self.data.append(element)

    def delete_first(self):
        return self.data.pop(0)

    def delete_last(self):
        return self.data.pop(len(self.data)-1)

    # ---- First Exercise, Swap both ends ----
    def swap_ends(self):
        first = self.delete_first()
        last = self.delete_last()
        self.insert_first(last)
        self.insert_last(first)

    # ---- Second Exercise, Swap first k elements ----
    def swap_first_k(self, k):
        temporary_list = []
        for _ in range(k):
            temporary_list.append(self.delete_first())
        for digit in temporary_list:
            self.insert_last(digit)


    def __str__(self):
        return " ".join(str(element) for element in self.data)

data = DataStructure([1, 5, 2, 5, 12, 6, 3, 5, 4])
data.swap_first_k(3)
print(data)
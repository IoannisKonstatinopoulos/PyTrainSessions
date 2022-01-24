""" Exercise #1 """


class List_Mean:

    def __init__(self, list_temp):
        self.list_temp = list_temp
        self.new_list = []

    def set_list(self):

        for item in self.list_temp:
            self.new_list.append(item)
        return self.new_list

    def get_list(self):
        return self.new_list

    def calc_avg(self):

        for item in self.new_list:
            if type(item) == str:
                self.new_list.remove(item)

        aver = sum(self.new_list) / len(self.new_list)
        return aver


list_1 = [1, 2, 17, 52.5, 43, 4.4, 10]

List_2 = [1, 2, 3, 4, 5, 6, 7, "dog"]

list_1C = List_Mean(list_1)

list_1C.set_list()
print(f"Test of 1st list : {list_1C.get_list()}")
print(f"Average of elements : {list_1C.calc_avg()}")

list_2C = List_Mean(List_2)

list_2C.set_list()
print(f"Test of 2nd list : {list_2C.get_list()}")
print(f"Average of elements : {list_2C.calc_avg()}")

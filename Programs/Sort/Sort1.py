class Sort1(object):
    def __init__(self):
        pass

    def quick_sort(self, list):

        if list == []:
            return []

        key = list[0]
        big_list = []
        small_list = []

        for i in list[1:]:
            if i < key:
                small_list.append(i)
            else:
                big_list.append(i)

        return self.quick_sort(small_list) + [key] + self.quick_sort(big_list)


    def bubble_sort(self, list):
        le = len(list)
        if le < 2:
            return list
        j = le - 1
        while j > 0:
            for i in range(le-1):
                if list[i] > list[i + 1]:
                    list[i],list[i + 1] = list[i + 1],list[i]
            j -= 1
        return list

    def insert_sort(self, list):
        le = len(list)
        if le < 2:
            return list
        for i in range(1,le):
            key = list[i]
            j = i - 1
            while j >= 0 and key < list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j+1] = key

        return list

    def selection_sort(self, list):
        le = len(list)
        if le < 2:
            return list

        for i in range(le):
            index = i
            for j in range(i+1,le):
                if list[index] > list[j]:
                    index = j

            list[i],list[index] = list[index],list[i]

        return list



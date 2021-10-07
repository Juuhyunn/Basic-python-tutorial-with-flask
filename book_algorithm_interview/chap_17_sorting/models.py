from dataclasses import dataclass

@dataclass
class Sorting(object):
    random_arr: []

    @property
    def random_arr(self): return self._random_arr
    @random_arr.setter
    def random_arr(self, random_arr): self._random_arr = random_arr

    def bubble_sort(self) -> []:
        arr = self._random_arr
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def merge_sort(param: []) -> []:
        arr = []
        if len(param) < 2 :
            return param
        mid = len(param) // 2
        arr_1 = Sorting.merge_sort(param[:mid])
        arr_2 = Sorting.merge_sort(param[mid:])
        i = j = 0
        while i < len(arr_1) and j < len(arr_2):
            if arr_1[i] < arr_2[j]:
                arr.append(arr_1[i])
                i += 1
            else:
                arr.append(arr_2[j])
                j += 1
        arr += arr_1[i:]
        arr += arr_2[j:]
        return arr

    @staticmethod
    def quick_sort(param: []) -> []:
        if len(param) < 2 :
            return param
        pivot = len(param)//2
        arr_1, arr_2, arr_3 = [], [], []
        for i in param:
            if i < param[pivot]:
                arr_1.append(i)
            elif i > param[pivot]:
                arr_3.append(i)
            else:
                arr_2.append(i)
        return Sorting.quick_sort(arr_1) + Sorting.quick_sort(arr_2) + Sorting.quick_sort(arr_3)
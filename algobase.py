import random

#example shuffled list
x = list(range(1, 101))
random.shuffle(x)

class Sort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def bubble_sort(self):
        for i in range(self.n):
            for j in range(self.n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr
    
    def selection_sort(self):
        for i in range(self.n):
            min_index = i
            for j in range(i+1, self.n):
                if self.arr[min_index] > self.arr[j]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
    
    def insertion_sort(self):
        for i in range(1, self.n):
            key = self.arr[i]
            j = i-1
            while j >= 0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
        return self.arr
    
    def merge_sort(self):
        if self.n > 1:
            mid = self.n // 2
            left = self.arr[:mid]
            right = self.arr[mid:]
            left = Sort(left).merge_sort()
            right = Sort(right).merge_sort()
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.arr[k] = left[i]
                    i += 1
                else:
                    self.arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                self.arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                self.arr[k] = right[j]
                j += 1
                k += 1
        return self.arr
    
    def quick_sort(self):
        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high]
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1
        def quick_sort_helper(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_helper(arr, low, pi-1)
                quick_sort_helper(arr, pi+1, high)
        quick_sort_helper(self.arr, 0, self.n-1)
        return self.arr
    
    def heap_sort(self):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        for i in range(self.n, -1, -1):
            heapify(self.arr, self.n, i)
        for i in range(self.n-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            heapify(self.arr, i, 0)
        return self.arr
    
    def counting_sort(self):
        max_element = int(max(self.arr))
        min_element = int(min(self.arr))
        range_of_elements = max_element - min_element + 1
        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(self.n)]
        for i in range(0, self.n):
            count_arr[self.arr[i]-min_element] += 1
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]
        for i in range(self.n-1, -1, -1):
            output_arr[count_arr[self.arr[i]-min_element]-1] = self.arr[i]
            count_arr[self.arr[i]-min_element] -= 1
        for i in range(0, self.n):
            self.arr[i] = output_arr[i]
        return self.arr

    def tim_sort(self):
        RUN = 32
        for i in range(0, self.n, RUN):
            self.arr[i:i+RUN] = Sort(self.arr[i:i+RUN]).insertion_sort()
        size = RUN
        while size < self.n:
            for left in range(0, self.n, 2*size):
                right = min((left + 2*size - 1), (self.n-1))
                self.arr[left:right+1] = Sort(self.arr[left:right+1]).merge_sort()
            size = 2*size
        return self.arr


#example
print(Sort(x).quick_sort())

    

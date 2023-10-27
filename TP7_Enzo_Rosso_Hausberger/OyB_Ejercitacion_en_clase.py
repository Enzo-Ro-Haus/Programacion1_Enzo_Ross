#Bubble Sort
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] > lst[i]:
                m = lst[i]
                lst[i] = lst[j]
                lst[j] = m

#Selection Sort
def selection_sort(lst):
    for i in range(len(lst)):
        temp = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[temp] :
                temp = j
        lst[i], lst[temp] = lst[temp], lst[i] 

#Insert Sort
def insert_sort(lst):
    for i in range(len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = temp

#Merge Sort
def merge_sort(lst):
    if len(lst) >  1:
        middle = len(lst)//2
        left = lst[:middle] 
        right = lst[middle:]
        
        merge_sort(left)
        merge_sort(right)
        l = 0
        r = 0
        m = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]: 
                lst[m] = left[l]
                l += 1
            else:
                lst[m] = right[r]
                r += 1
            m += 1
        
        while l < len(left):
            lst[m] = left[l]
            l += 1
            m += 1
        
        while r < len(right):
            lst[m] = right[r]
            r += 1
            m += 1

#Counting Sort
def counting_sort(lst):
    max_element =  max(lst)
    min_element = min(lst)
    count_arr = [0] * (max_element - min_element + 1)
    
    for i in lst:
        count_arr[i - min_element] += 1
    
    output_arr = 0
    for i in range(max_element):
        while count_arr[i] > 0:
            lst[output_arr] = i + min_element
            output_arr += 1
            count_arr[i] -= 1
    return lst

#Linear search
def linear_search(arr, item):
    for n in range(len(arr)):
        if arr[n] == item:
            return n
        return -1

#Binary search
def binary_search(arr, item):
    start = 0
    end = len(arr)-1
    while True:
        middle = (start + end) // 2
        middle_value = arr[middle]
        if middle_value == item:
            return middle
        elif middle_value < item:
            start  = middle + 1
        elif middle_value > item:
            end = middle - 1
    return -1

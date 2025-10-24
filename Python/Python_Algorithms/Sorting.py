# Insertion Sort is complexity Best: O(n), Worst: O(n^2), Average: 0(n^2)
# Best use for small arrays or almost sorted arrays
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0 :
            array[j - 1], array[j] = array[j], array[j - 1]
            j -=1
    return array

# Selection Sort is complexity Best: O(n^2), Worst: O(n^2), Average: 0(n^2)
# easy to implement
def selection_sort(array):
    for i in range(len(array)):
        min_ind = i
        for j in range(i + 1, len(array)):
            if array[min_ind] > array[j]:
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]
    return array

# Bubble Sort is complexity Best: O(n), Worst: O(n^2), Average: 0(n^2)
# considerably slower than insertion sort, very simple
def bubble_sort(array):
    for i in range(len(array)):
        has_swapped = False
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                has_swapped = True
        if not has_swapped:
            break
    return array

# Shell Sort is complexity varies on state of array from O(nlogn) to O(n^2)
# considerably slower than insertion sort, very simple
def shell_sort(array):
    gaps = [5, 3, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j + gap] < array[j] and j >= 0:
                array[j + gap], array[j] = array[j], array[j + gap]
                j -= gap
    return array

def shell_sort_2(arr):
    n = len(arr)
    gap = n // 2  # Initialize the gap, typically half the array size
    while gap > 0:
        for i in range(gap, n):
            current_value = arr[i]
            position = i
            while position >= gap and arr[position - gap] > current_value:
                arr[position] = arr[position - gap]
                position -= gap
            arr[position] = current_value
        gap //= 2  # Reduce the gap for the next pass
    return arr

# Heap Sort is complexity varies on state of array from O(nlogn) to O(n^2)
# improved selection sort
def heap_sort(array):
    heapify(array)
    for end_idx in range(len(array) - 1, 0, -1):
        array[0], array[end_idx] = array[end_idx], array[0]
        move_down(array, 0, end_idx - 1)
    return array

def heapify(array):
    last_parent_idx = len(array) // 2 - 1
    for idx in range(last_parent_idx, -1, -1):
        move_down(array, idx, len(array) - 1)
    return array

def move_down(array, start_idx, end_idx):
    child_idx = 2 * start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
            start_idx = child_idx
            child_idx = 2 * start_idx + 1
        else:
            child_idx = end_idx + 1

# Merge Sort is complexity varies on state of array from O(nlogn) for all cases but space is O(n)
# efficient for sorting algoriths slower on small arrays, but down side is the space complexity
def merge_sort(array):
    if len(array) < 2:
        return array
    first_half = merge_sort(array[:len(array) // 2])
    second_half = merge_sort(array[len(array) // 2:])
    return merge(first_half, second_half)

def merge(first_half, second_half):
    result = []
    i = j = 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1
    while i < len(first_half):
        result.append(first_half[i])
        i += 1
    while j < len(second_half):
        result.append(second_half[j])
        j += 1
    return result

# Quick Sort is complexity Best and Average O(nlogn) worst O(n^2)for all cases but space is O(logn)
# efficient for sorting algoriths slower on small arrays, but down side is the space complexity
def quick_sort(array):
    if len(array) < 2:
        return array
    return partition(array, 0, len(array) - 1)

def partition(array, start, end):
    if start >= end:
        return array
    pivot = end
    boundary = start
    for i in range(start, end):
        if array[i] <= array[pivot]:
            array[boundary], array[i] = array[i], array[boundary]
            boundary += 1
    array[boundary], array[end] = array[end], array[boundary]
    partition(array, start, boundary -1)
    partition(array, boundary+1, end)
    return array

# Radix Sort is complexity Best and Average O(nk) where k is the number of digits for all cases but space is O(n + k)
# efficient for sorting algoriths slower on small arrays, but down side is the space complexity
import math
def radix_sort(array):
    max_digits = get_max_number_of_digits(array)
    for i in range(max_digits + 1):
        buckets = [[] for _ in range(10)]
        for num in array:
            digit = get_digit_at_position(num, position = i)
            buckets[digit].append(num)
        array = flatten(buckets)
    return array

def get_max_number_of_digits(array):
    return max(int(math.log10(abs(num))) + 1 if num != 0 else 1 for num in array)

def get_digit_at_position(number, position):
    return(abs(number) // 10 ** position) % 10

def flatten(array):
    return [num for inner in array for num in inner]



x = [10034, 165, 52, 5433 ,11, 826, 32175, 3, 88, 4545]
sorted_ans = [3, 11, 52, 88, 165, 826, 4545, 5433, 10034, 32175]

print(x)
sorted = radix_sort(x)
print(sorted)
if sorted == sorted_ans:
    print("sorted")
else:
    print("unsorted")










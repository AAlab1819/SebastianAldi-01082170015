def max_heapify(array, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(array) and array[i] < array[left]:
        largest = left
    if right < len(array) and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)
def build_max_heap(array):
    for i in range(len(array)//2, -1, -1): max_heapify(array, i)
    return array
def min_heapify(array, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(array) and array[i] > array[left]:
        smallest = left
    if right < len(array) and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        max_heapify(array, smallest)
def build_min_heap(array):
    for i in range(len(array)//2, -1, -1): min_heapify(array, i)
    return array
min_heap = []
max_heap = []
median = 0
numbers = int(input())
for running in range(numbers):
    insert = int(input())
    if insert < median:
        max_heap.append(insert)
        max_heap = build_max_heap(max_heap)
    else:
        min_heap.append(insert)
        min_heap = build_min_heap(min_heap)
    if abs(len(max_heap) - len(min_heap)) > 1:
        if len(max_heap) > len(min_heap):
            min_heap.append(max_heap[0])
            min_heap = build_min_heap(min_heap)
            del max_heap[0]
        else:
            max_heap.append(min_heap[0])
            max_heap = build_max_heap(max_heap)
            del min_heap[0]
    if abs(len(max_heap) - len(min_heap)) == 1:
        if len(max_heap) > len(min_heap):
            median = max_heap[0]
        else:
            median = min_heap[0]
    else:
        median = (max_heap[0] + min_heap[0]) / 2
    print(median)
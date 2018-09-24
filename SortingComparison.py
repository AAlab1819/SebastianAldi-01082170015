# Dependencies
import time
import random
# Merge sort functions
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0 
    j = 0 
    k = l 
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)

# Driver code
arr = []
for i in range(10000):
    arr.append(random.randint(1,1000))
print("unsorted array:")
print(arr)
arr2 = arr

# Bubble sort
start = time.time()
for i in range(10000):
    for j in range(0, 9999-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
end = time.time()

print("sorted array (bubble):")
print(arr)
print("Time:",(end-start),"\n\n")

# Merge sort
start = time.time()
mergeSort(arr2,0,9999)
end = time.time()

print("sorted array (merge)")
print(arr2)
print("Time:",(end-start))

'''
Expected runtime of 10000 element sort:
Bubble sort: ~20 seconds
Merge sort: below 1 second

Credits:
https://www.geeksforgeeks.org/merge-sort/
https://www.geeksforgeeks.org/bubble-sort/
https://pythonhow.com/measure-execution-time-python-code/
'''

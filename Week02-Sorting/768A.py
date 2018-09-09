def nextGap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
def combSort(arr):
    n = len(arr)
    gap = n 
    swapped = True
    while gap !=1 or swapped:
        gap = nextGap(gap)
        swapped = False
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True
size = int(input())
arr = [int(x) for x in input().split()]
combSort(arr)
unsupportable = 0   
for x in arr:
    if x == arr[0]:
        unsupportable += 1
    else:
        break
for x in reversed(arr):
    if x == arr[len(arr)-1]:
        unsupportable += 1
    else:
        break
print(size-unsupportable if size-unsupportable >= 0 else 0)
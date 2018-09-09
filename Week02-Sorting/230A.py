def cocktailSort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range (start, end):
            if (arr[i][0] > arr[i + 1][0]):
                arr[i], arr[i + 1]= arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if (arr[i][0] > arr[i + 1][0]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True  
        start = start + 1
strength, n = map(int, input().split())
dragons = []
possible = True
for i in range(n):
    power, bonus = map(int, input().split())
    dragons.append([power, bonus])
cocktailSort(dragons)
for dragon in dragons:
    if dragon[0] >= strength:
        possible = False
        break
    else:
        strength += dragon[1]
print("YES" if possible else "NO")
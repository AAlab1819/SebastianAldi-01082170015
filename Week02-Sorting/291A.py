def shellSort(arr):
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
n = int(input())
arr = [int(x) for x in input().split()]
shellSort(arr)
ans = 0
if n == 1:
	print(0)
	quit()
else:
	for i in range(n-2):
		if arr[i] == 0: continue
		if arr[i] == arr[i+1]:
			if arr[i+1] == arr[i+2]:
	    			ans = -1
	    			break
			else:
				ans += 1
if ans == -1:
	print(ans)
else:
	print(ans if arr[n-2] != arr[n-1] or arr[n-2] == 0 else ans+1)
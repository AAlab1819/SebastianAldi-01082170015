n, k = map(int, input().split())
ratingArray = [int(x) for x in input().split()]
uniqueRating = []
index = []
for i in range(n):
    if ratingArray[i] not in uniqueRating:
        uniqueRating.append(ratingArray[i])
        index.append(i+1)
if len(uniqueRating) >= k:
    print("YES")
    for i in range(k):
        print(index[i], end=" ")
else: print("NO")

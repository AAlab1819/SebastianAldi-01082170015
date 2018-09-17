lanterns, streetLength = map(int, input().split())
lanternPositions = sorted([int(x) for x in input().split()])
maxDistance=0
for i in range (lanterns-1):
    maxDistance = max(maxDistance, lanternPositions[i+1] - lanternPositions[i])
answer = max(maxDistance/2, lanternPositions[0])
answer = max(answer, streetLength - lanternPositions[lanterns-1])
print(answer)
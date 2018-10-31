variants, volume = map(int, input().split())
cost = [int(x) for x in input().split()]
for i in range(1, variants):
    cost[i] = min(cost[i], 2*cost[i-1])
while len(cost) < 32:
    cost.append(cost[-1]*2)
ans = 0
binaryRepresentation = list(bin(volume)[2:])
while len(binaryRepresentation) < 32:
    binaryRepresentation = ['0'] + binaryRepresentation
binaryRepresentation.reverse()
for i in range(len(cost)):
    if binaryRepresentation[i] == '1':
        ans += cost[i]
    else:
        ans = min(ans, cost[i])
print(ans)
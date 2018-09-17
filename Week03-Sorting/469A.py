levels = int(input())
little_x = [int(x) for x in input().split()]
little_y = [int(x) for x in input().split()]
finishable = set()
for i in range(little_x[0]+1):
    if i == 0: continue
    finishable.add(little_x[i])
for i in range(little_y[0]+1):
    if i == 0: continue
    finishable.add(little_y[i])
if len(finishable) == levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
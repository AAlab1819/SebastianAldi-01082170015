k = int(input())
l = int(input())
m = int(input())
n = int(input())
totalDragons = int(input())
damaged = 0
for dragon in range(1,totalDragons+1):
    if dragon%k==0 or dragon%l==0 or dragon%m==0 or dragon%n==0:
        damaged += 1
print(damaged)
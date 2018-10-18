sessions = int(input())
teams = [int(x) for x in input().split()]
possible = True
for i in range(sessions - 1):
    if teams[i] < 0: possible = False
    teams[i+1] -= teams[i]%2
if teams[sessions - 1] % 2 == 1: possible = False
print("YES" if possible else "NO")
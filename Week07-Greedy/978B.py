length = int(input())
filename = input()
ans = 0
for i in range(2, length):
    if filename[i] == 'x' and filename[i-1] == 'x' and filename[i-2] == 'x':
        ans += 1
print(ans)
elements = int(input())
sequence = [int(x) for x in input().split()]
negative, positive = 0, 0
for number in sequence:
    if number >= 0:
        positive += number
    else:
        negative += number*(-1)
print(positive+negative)
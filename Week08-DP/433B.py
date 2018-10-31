import sys
stones = int(sys.stdin.readline())
arrayofStones = [int(x) for x in sys.stdin.readline().split()]
questions = int(sys.stdin.readline())
cumulative = arrayofStones.copy()
sortedCumulative = sorted(arrayofStones)
for i in range(1,stones):
    cumulative[i] += cumulative[i-1]
for i in range(1,stones):
    sortedCumulative[i] += sortedCumulative[i-1]
for question in range(questions):
    questionType, left, right = map(int, sys.stdin.readline().split())
    if questionType == 1:
        ans = cumulative[right-1]
        if left > 1:
            ans -= cumulative[left-2]
    else:
        ans = sortedCumulative[right-1]
        if left > 1:
            ans -= sortedCumulative[left-2]
    sys.stdout.write(str(ans)+'\n')
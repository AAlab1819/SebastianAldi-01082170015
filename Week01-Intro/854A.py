# the one and only input
n = int(input())
if n % 2 == 1:
    numerator = n//2
    denominator = n - numerator
else:
    numerator = (n//2) - 1
    while numerator % 2 == 0:
        numerator -= 1
    denominator = n - numerator
print(numerator, denominator)

# Recieving user input
yellowC, blueC = map(int, input().split())
yellowB, greenB, blueB = map(int, input().split())
# Counting the deficit
yellowC -= (2 * yellowB + greenB)
blueC -= (greenB + 3 * blueB)
# Totalling the amount required
requiredC = 0
if yellowC < 0:
    requiredC += yellowC * -1
if blueC < 0:
    requiredC += blueC * -1
print(requiredC)

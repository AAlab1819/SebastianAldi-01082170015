## 854A: Fraction  
[**Link**](http://codeforces.com/problemset/problem/854/A) | [**Solution**](http://codeforces.com/contest/854/submission/42278907)\
The problem here is simple: output the highest possible fraction that cannot be simplified.\
In order to achieve that, we need to determine the highest possible denominator and numerator.\
In order to do so, we must first divide n into half, then decrease it by 1. (For example, 20/10 - 1 = 9, 30/2 - 1 = 14, and so on).\
Why decrease it by 1? Because we need to avoid having the same denominator and numerator, resulting in a whole number.\
Then, we must turn the resulted numerator into an odd number by substracting it by 1 until it becomes an odd number.\
Finally, the denominator can be acquired from substracting n by the resulting numerator.\
\
Step by step process:\
n = 30\
30 / 15 - 1 = 14, which is an even number [meaning that 30 - 14 = 16 is also even, which can be simplified]\
14 - 1 = 13, which is an odd number, denominator becomes 30 - 13 = 17\
The answer is 13/17, which is then outputted as `13 17`.

## 912A: Tricky Alchemy
[**Link**](http://codeforces.com/problemset/problem/912/A) | [**Solution**](http://codeforces.com/contest/912/submission/42277918)\
The problem is as follows: output how many additional crystals does Grisha need in order to make the required yellow, green, and blue balls. In order to count how many crystals does Grisha need, subtract the stock of crystals Grisha has by the amount of balls that Grisha need to make. The calculation is as follows:\
`Yellow Crystals = Yellow Crystals - Yellow balls needed * 2 - Green balls needed`\
`Blue Crystals = Blue Crystals - Blue balls needed * 3 - Green balls needed`\
If the result of the yellow/blue crystals is negative, it signifies a deficit of crystals, which is added into a seperate variable\
`if YellowCrystals < 0: RequiredCrytals += YellowCrystals*-1`\
This is to make sure that a surplus of crystals will not cover the deficit, for example:\
`5 surplus of yellow crystals + 5 deficit of blue crystals = 0 crystals needed` (this is wrong)\
After the amount of required crystals is calculated, simply print the result.

## 988A: Diverse Team
[**Link**](http://codeforces.com/problemset/problem/988/A) | [**Solution**](http://codeforces.com/contest/988/submission/42279798)\
The problem here is possibly the hardest of the three weekly submissions, which is as follows: given the rating of the students, is it possible to create a team of size `k` where all of the students inside the team have different ratings? In order to solve this problem, we shall check how many distinct ratings are there in the given array.\
First, count the amount of distinct ratings, and store the first occurence into an array (because the output asked for the index, not the rating)\
We can count the amount of distinct ratings by creating an array which stores what rating has been scanned before, and we can check if the rating is distinct or not by doing a complete search every time we need to check if a rating is distinct (or use a dictionary/map). The pseudocode would look something like:\
```
For every element in array of ratings:
    If element is not inside of distinctRatings:
        Insert element into distinctRatings
        Insert index into indexesList
        Increment counter by 1 (optional, see below)
```
If the amount of distinct ratings (`use len(distinctRatings)` or use a counter which gets incremented every time a new element is inserted into distinctRatings) is greater than or equal to k, then the answer is `YES`, then print the first n indexes inside indexesList (to make sure that we don't print more than we needed). Else, the answer is `NO`.

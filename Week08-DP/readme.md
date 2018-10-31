## 433B: Kuriyama Mirai's Stones
[**Link**](http://codeforces.com/problemset/problem/433/B) | [**Solution**](http://codeforces.com/contest/433/submission/44820385)\
Abridged version: Given an array, Mirai will ask 2 types of question. The first type is the sum from the normal array from index l to r, while the second type is the sum of the sorted array from index l to r.
  
Taking O(n) to calculate the sum will take a long time (O(mn)), so we need to reduce the time it takes to answer a question. Create a cumulative array by adding the first element into the second element, and so on. For example:
```
1 2 3 4 5 will turn into
1 (1+2) (1+2+3) (1+2+3+4) (1+2+3+4+5)
which is 1 3 6 10 15
```
Create another array which is the sorted version of the original array, and turn it into a cumulative array as well. Now, answering the question will only take O(1). For example:
```
1 3 6 10 15 (this is already cumulative)
L = 2, R = 4 (2+3+4 = 9)
Answer = Array[R-1] - Array[L-1] = 10 - 1 = 9
Make sure that the left is not be out of bounds when L = 1
```
Worst Case: *O*(*n log n*), because we need to sort in order to find the cumulative sorted array. Changing array to cumulative takes O(n), and each query takes O(1).
  
## 931C: Party Lemonade
[**Link**](http://codeforces.com/problemset/problem/931/C) | [**Solution**](http://codeforces.com/contest/913/submission/45029261)\
Abridged version: Given the amount of volume needed and the price of each bottle, find the minimum cost to meet the requirements. The volume of the bottle depends on the index (`2^i, starting from 1, 2, 4, 8, etc`), and it is not required to buy the exact same amount as the volume needed.
  
First we need to take a greedy approach. If 2 one litre bottles cost less than a single two litre bottle, then change the cost of the two litre bottle to the cost of 2 one litre bottles. Do that for all the next bottles (if 4 costs more than 2 2L bottles, etc). Formally, if `2*cost_i < cost_(i+1)`, then set `cost_(i+1)` to `2*cost_i`. After doing that, extend the array of price by adding 2 times the last price to the end of the array. Logically, if there are no 16L bottles avaiable, 2 8L bottles will cost the least (after performing the greedy approach). Extend it until the array size is 32 (because of the constraint of the problem, `2^32 > 10^9`).
  
Since the volume of the bottles is in exponents (`2^0, 2^1, etc`), we can take a bitmask-DP approach. Turn the volume needed into the binary representation, then reverse it. Iterate through the bits starting from the first. If the bit is 1, then it is needed to satisfy the requirements. If it is 0, check if it is less expensive then what we have been counting. The reason is that:
```
011
100
if buying a 2^2 bottle is less expensive than buying a 2^1 bottle and a 2^0 bottle, then why not?
```
Worst Case: *O*(*n*). No sorting is needed, just a lot of linear searching, but ignoring coefficients will lead the complexity to O(n).

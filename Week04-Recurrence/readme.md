## 268B: Buttons
[**Link**](http://codeforces.com/contest/268/problem/B) | [**Solution**](http://codeforces.com/contest/268/submission/43352942)\
Imagine a lock with a certain button combination. Pressing the wrong button at the wrong sequence will reset the attempt immediately. Now imagine this person is going to try and brute force the lock. Our task here is to find how many buttons does the man need to press in the worst case.\
For this problem, my way of thinking is like this. Take for example there are 4 buttons, and the combination is 4, 3, 2, 1.\
The man would press 1 and fail, 2 and fail, 3 and fail. In total, the man fails 3 times.\
The man would press 4, 1 and fail, 4, 2 and fail. In total, the man fails 2 times.\
The man would press 4, 3, 1 and fail. In total, the man fails once.\
Finally, the man would press 4,3,2,1. In total, the buttons pressed is 1 * 3 + 2 * 2 + 3 * 1. The loop would look like: From 1 to n, add the answer by i * (n-i).\
Don't forget to add n in the end.\
  
Complexity:<br>
`O(1)` is possible by using a certain mathematical equation, but for this case, `O(n)` will do. Complexity is `O(n)` because we will always iterate from 1 to n.
Worst Case: *O*(*n*)<br>
  
## 598D: Igor in the Museum
[**Link**](http://codeforces.com/contest/598/problem/D) | [**Solution**](https://codeforces.com/contest/598/submission/43351881)\
Explain later ok\

Complexity:<br>
If we are going to traverse the whole museum as a whole, the worst complexity expected would be the row times the column.\
Worst Case: *O*(*nm*)<br>

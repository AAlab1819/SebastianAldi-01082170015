## 268B: Buttons
[**Link**](http://codeforces.com/contest/268/problem/B) | [**Solution**](http://codeforces.com/contest/268/submission/43352942)\
Imagine a lock with a certain button combination. Pressing the wrong button at the wrong sequence will reset the attempt immediately. Now imagine this person is going to try and brute force the lock. Our task here is to find how many buttons does the man need to press in the worst case.\
For this problem, my way of thinking is like this. Take for example there are 4 buttons, and the combination is 4, 3, 2, 1.\
The man would press 1 and fail, 2 and fail, 3 and fail. In total, the man fails 3 times.\
The man would press 4, 1 and fail, 4, 2 and fail. In total, the man fails 2 times.\
The man would press 4, 3, 1 and fail. In total, the man fails once.\
Finally, the man would press 4,3,2,1. In total, the buttons pressed is 1 * 3 + 2 * 2 + 3 * 1. The loop would look like:\
`From 1 to n, add the answer by i * (n-i)`.\
Don't forget to add n in the end.
  
Complexity:<br>
`O(1)` is possible by using a certain mathematical equation, but for this case, `O(n)` will do. Complexity is `O(n)` because we will always iterate from 1 to n.\
Worst Case: *O*(*n*)<br>
  
## 598D: Igor in the Museum
[**Link**](http://codeforces.com/contest/598/problem/D) | [**Solution**](https://codeforces.com/contest/598/submission/43351881)\
Igor is inside a museum. The walls are filled with paintings. Given a starting position, how many paintings can Igor see? Igor can only see paintings in four directions (north, south, east, west), and he can move to an empty space.\
To solve this problem, we shall use flood fill algorithm, where Igor will try to move to all directions at the same time, and stops only when Igor hits a wall or tries to return to a past square. However, simple flood fill is not enough (it is enough, but if we are going to perform flood fill for every query, it will end up having *O*(*nmk*) complexity, because we perform the flood fill algorithm `k` times. In order to avoid this, it can be shown that there are "rooms" which has the same answer if the query is inside the same room. Take for example:  
  
```
012345 X  
1*****  
2*...*  
3*****  
4*.***  
5*****  
Y
```  
  
Points (2,2), (3,2), and (4,2) would have the same answer (8), while point (2,4) has a different answer (4). To avoid querying in the same room, during flood fill we shall label points (2,2), (3,2), and (4,2) with a unique key, which would then correspond to the array of answers. If for example the key for points (2,2), (3,2), and (4,2) is 1, then `answer[1]` is equal to 6, while if point (2,4) has key 2, then `answer[2]` is equal to 4. After preprocessing all possible places (which is, all points that contains `.`) with the key->answer method, then each query would have a complexity of *O*(1), leading to a complexity of *O*(*nm*) plus k array access operations instead of performing flood fill k times, leading to a disastrous *O*(*nmk*) solution.
Complexity:<br>
If we are going to traverse the whole museum as a whole, the worst complexity expected would be the row times the column.\
Worst Case: *O*(*nm*)<br>
  
```
SWYgdGhpcyBwYXJ0IGlzIG5vdCByZW1vdmVkLCB0aGVuIGl0IGlzIGFwcGFyZW50IHRoYXQgc29tZW9uZSBpcyBjb3B5aW5nIGFuZCBwYXN0aW5nIG15IGZpbGVzIHdpdGhvdXQgYm90aGVyaW5nIHRvIG1vZGlmeSBpdC4=
```
**2^6**


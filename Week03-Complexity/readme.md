## 492B: Vanya and Lanterns
[**Link**](http://codeforces.com/contest/492/problem/B) | [**Solution**](http://codeforces.com/contest/492/submission/42973034)\
The problem here is to find the minimum possible radius in order to cover all of the street, if there are lanterns scattered all over the street. In order to do this, we take the distance between two lanterns and divide it by 2 in order to get the radius.\
**Why divide by 2?**\
We need to divide it by 2 because both lanterns will light up, so there is no need to take the distance as a whole. For example, if a and b has a distance of 4, we choose the radius 2 because:\
A2)(3B\
A will light point 1 and 2, while B will light the points 3 and 4. So there is no need to use 4 as a radius.\
**Watch out!**\
If there are no lanterns at point 0 or point `streetLength` (rightmost point), then make sure to account for the first lantern position - 0 as well as rightmost point - last lantern position. Why? Take for example a street length of 3, and a lantern at point 3:\
01(2A --> point 0 and 1 is not covered by the light, because there is no lantern at point 0 to cover the remaining points.  
  
Complexity:<br>
Worst Case: *O*(*nlogn*) = bottlenecked by `Timsort`<br>
Average Case: &theta;(*nlogn*) = bottlenecked by `Timsort`, even with good data<br> 
Best Case: &Omega;(*n*) = best case for `Timsort`, then perform a linear search to find greatest distance<br>
  
## 148A: Insomnia Cure
[**Link**](http://codeforces.com/contest/148/problem/A) | [**Solution**](http://codeforces.com/contest/148/submission/42973341)\
Simple problem, simple explanation: If there are *d* dragons, indexed from 1 to *d*, how many dragons are injured? Or mathematically, how many numbers from 1 to *d* is a multiple of *k* or *l* or *m* or *n*?\
There are two approaches to this: [mathematical](https://math.stackexchange.com/q/688272) or brute force, considering *d* has a maximum value of 100000. Since brute force is possible, let's do it! 🤣\
Perform a linear for loop from 1 to *d*, check if each number results in a whole number if divided by *k* or *l* or *m* or *n*, by using modulus by checking if the result of the modulus is 0.
  
Complexity:<br>
Since we are always going to perform a complete serach, the complexity is *O*(*n*) no matter what.\
Worst Case: *O*(*n*)<br>
Average Case: &theta;(*n*)<br> 
Best Case: &Omega;(*n*)<br>
## 469A: I Wanna Be the Guy
[**Link**](http://codeforces.com/contest/469/problem/A) | [**Solution**](http://codeforces.com/contest/469/submission/42975930)\
If there are *n* levels in a game, and if little X and little Y can solve certain levels only, can they beat the game with teamwork?\
To put it in other words, from numbers 1 to *n*, are all the numbers present if the first array (little x) and the second array (little y) is merged?\
To solve this problem, I used a *set* container, which only allows unique elements (so if the set contains 1, 2, 3, and I attempt to insert 2 again, nothing happens), insert both lists into the set, then check if the number of elements in the set matches the number of levels. If the number of elements is less than the number of levels, that means that some levels are unsolvable by both of them.
  
Complexity:<br>
We can make the solution run faster with break statements, but the complexity remains the same because it disregards the coefficient of *n*. Insertion of both lists take `little_x[0] + little_y[0]` operations, maybe even worse if the insertion is linear every time, but the complexity remains linear.\
Worst Case: *O*(*n*)<br>
Average Case: &theta;(*n*)<br> 
Best Case: &Omega;(*n*)<br>

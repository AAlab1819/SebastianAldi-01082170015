# FULL C++ TIME BOYS
## 4C: Registration System
[**Link**](http://codeforces.com/problemset/problem/4/C) | [**Solution**](http://codeforces.com/contest/4/submission/30821374)\
A classic world problem: Two people cannot use the same username! So instead, the system tries to give the user an alternative nickname if it is already taken. For example, if there are five people named john that wants to register as john, then the system will assign the first john as `john`, and the second john will be given an alternative of `john1`, which is john + a number which starts from one and continues to go up according to how many time will the name be requested. In case of five johns trying to register, the names provided will be `john`, `john1`, `john2`, `john3`, and `john4`. If the name is not taken yet, there is no need to print `john` or the new username, just print `OK`. In case of duplicates, print the alternative username.\
Now, for the actual solution:\
To solve this problem, I will be using a container called `map`, which is an implementation of BST in C++. First, check if the name has been used before. If the name has not been used, then two things happen:
-  The system prints `OK` to the console, and
-  The counter for that specific name starts, and is set to 1.
  
Then, whenever the same name gets called again, simply print the name + the current counter for that name.\
Complexity:\
Accessing an element in the map has a complexity of *log k*, and we need to perform that *n* times. Therefore, the complexity would depend on how many names are there. Worst case would be if all of them would be a unique name, therefore the map needs to find a nonexixsant entry through a lot of names.\
Worst Case: *O*(*n log n*)

## 115A: Party
[**Link**](http://codeforces.com/problemset/problem/115/A) | [**Solution**](http://codeforces.com/problemset/submission/115/43630708)\
In a company, there are employees who are managers of other employees. But said employee could also have a manager that manages them. Take for example A, B, C, and F. B is C's and F's manager, and A is B's manager. In this scenario, A is the superior of B (because A is B's direct manager), C, and F (because both C and F is managed by B, who is managed by A). Now, let's add D and E. D is the manager of E. D does not have a manager. In this scenario, D is the superior of E, but both D and E has no relations with A, B, C, and F, unless something connects them. Here is a picture for better explanation:
```
A         D
 \        |
  B       E
 / \
C   F
```
The company wants to have a party, and in order to prevent awkwardness, there shall be no superiority in group. In this case, a group cannot contain A and B at the same time, or B and C/F at the same time. A and C/F is also not allowed due to indirect superiority. For this case, the optimal grouping would be A and D, B and E, C and F. A group may contain more than two employees, so C,F,E or C,F,D being in a group is also acceptable. A group also may contain only one employee.\
The question is how many groups is needed to accomodate all employees without any superiority issues?\
The answer is to check the "depth" of the hierarchy. Based on the picture above, we can just make groups based on the row level. A and D would form a group, B and E would form a group, lastly C and F would form a group. There would be no problems. To find the maximum depth, take each employee and scan upwards (how many superiors to the top). The highest count would be the answer.\
Complexity:
We are going to perform a for loop from 1 to n, but for each of them, we also need to perform an upwards scan which goes upwards differently, depending on how many superiors are there above said employee. Accessing through a map takes *log n* and it is performed *depth* times (but we are ignoring coefficients, and the depth varies).\
Worst Case: *O*(*n log n*)<br>

## 913B: Christmas Spruce
[**Link**](http://codeforces.com/contest/913/problem/B) | [**Solution**](http://codeforces.com/contest/913/submission/43604759)\
The problem here is straightforward. If a vertex has children, make sure it has at least 3 children that are leaves (have no children). If the condition is not fulfilled, then the tree is not a spruce. For example:
```
    1
   /|\
  2 3 4
 /|\
5 6 7
```
This is not a spruce because `1` does not have 3 leaf children. `3` and `4` are both leaves, but `2` is not a leaf, so the condition is not fulfilled.
```
      1--
     /|\ \
    2 3 4 5 
   /|\
  6 7 8
```
This is a spruce because `1` have 3 leaf children (3, 4, 5) and 2 have 3 leaf children as well (6, 7, 8).
My way to solve this is to simulate the tree using `map <int, vector <int>>`, where the key represents the index and `vector<int>` represents how many child does the key have. Go to each index from 1 to `n`, then check if the index has children or not. If the index have children, count for each child, how many child does not have additional children. If the leaves have a total of less than 3, then the tree is not a spruce.
Complexity:<br>
Worst Case: *O*(*n log n*)<br>

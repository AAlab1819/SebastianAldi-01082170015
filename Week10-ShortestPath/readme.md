This week's code is going to be extra messy... and long.
## 601A: The Two Routes
[**Link**](http://codeforces.com/contest/601/problem/A) | [**Solution**](http://codeforces.com/contest/601/submission/45429473)  
There is a train and a bus. We are given the paths that the train can take, and if a road is not occupied by a railway, it is a road for the bus. Take the sample input:
```
4 2
1 3
3 4
```
This means that the road from 1 -> 3 and 3 -> 4 is a railway, while 1 -> 2, 1-> 4, 2 -> 3, 2 -> 4 is a road. Instead of having two adjacency lists (and suffering from making the adjacency list for the bus), an adjacency matrix is better (although time complexity wise, is worse). The matrix is represented as a two-dimensional array, and the sample input is turned into this:
```
  1 2 3 4
1 0 0 1 0
2 0 0 0 0
3 1 0 0 1
4 0 0 1 0
```
0 represents a road, while 1 represents a railway. And now, for the actual problem... Given that traveling from 1 road to any road is always 1 (unweighted graph), output the longer of the shortest path between those two. Instead of simulating both the train and bus, check element 1 -> N in the matrix. If it is the road (0), we need to simulate the shortest path for the train. If it is is a railway (1), we need to simulate the shortest path for the bus. Why? Because if there is a path from 1 to N, obviously the time taken is 1 hour, so no need to check if the bus or train is longer. In order to find the shortest path in an unweighted graph, I used Breadth-First Search (readme will be changed later if I need to actually explain how BFS works).
  
Worst Case: O(n²), because we used a n x n matrix, and BFS using an adjacency matrix needs to scan all possible paths this way. Worst case scenario we need to check 2 -> N for row 1, move to row 2, check from 3 - > N for row 2, move on to row 3... until check from N-1 -> N to row N, move on to N).
  
## 20C: Dijkstra?
[**Link**](http://codeforces.com/contest/20/problem/C) | [**Solution**](http://codeforces.com/contest/20/submission/45557115)  
Use Dijkstra's shortest path algorithm, but we need to find the path instead of the cost. Therefore, we need to use a tuple instead of a pair, because we need to store the running cost, the source, and the destination. Keep track of the path by using a source array, which the index stores the previous path before reaching the index. Initialize the values of the source array to -1 (there is a possibility that there are no paths leading to n). Perform Dijkstra's algorithm, but keep track of the source. We need to reverse iterate through the source array in order to find the path. For example, take the sample input:
```
5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1
```
Running the code will yield the contents of the source array as follows:
```
2 3 4 5
1 4 1 3
```
This shows that the shortest path to 5 is from 3, the shortest path to 3 is 4, the shortest path to 4 is 1. The reverse checking is done by `destination = source[destination]`. Keep track of the indexes, and print it.
  
Worst Case: O(E x log(V)), because Dijkstra. This problem is pretty much Dijkstra, except that we have to print the path instead of the minimum cost.

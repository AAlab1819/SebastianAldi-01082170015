## Roy and Trending Topics
What this problem wants is to get the five top topics, based on the growing popularity (new z-score - old z-score). In order to do this, we need to sort the topics based by their difference in popularity. For this case, the sorting method used is HeapSort (because this week's topic is heaps and I hate myself). After sorting the topics by difference in popularity, we also need to sort it by ID (if two topics have the same popularity growth, the topic with the bigger ID gets printed first). To do this, I used a dictionary to store the popularity difference, and then sort it by topic ID in descending order. The double sort here is really shooting myself in the foot, causing a really bad spike in complexity.\
Worst Case: *O(n² log n)*<br>

## Find the Running Median
If we are going to sort the list of numbers every time we insert a number, and then find the median, it is bound to take a long time, especially when the data starts getting very large. To prevent this, I used a min heap and a max heap. How it works is that whenever a number is added, it goes to the max heap if it is higher than the median, or it goes to the min heap if it is smaller or equal, then perform `build_min/max_heap` to make sure that the heap still follows the rules. If the difference in size of the two is more than one, it is unbalanced. When this happens, move the top of the largest (not maX) heap to the other. If the difference in size is one, print the top of the larger (not max) heap. If the difference is zero, print the average of the top of each heap.\
Worst Case: *O*(*n log n*)<br>

### Disclaimer
These solutions are made using python, therefore the solution may be correct but it has a high probability of resulting in *time limit exceeded* due to how slow python is. C++ has a better chance of getting an accepted verdict, but this week is a special week where I only need to implement the solution without submitting it.

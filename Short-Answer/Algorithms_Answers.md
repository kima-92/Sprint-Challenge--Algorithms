#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)	O(log n)		-	The algorithm doesn't do the same number of operations regardless the input size, but it's also not Linear, which would mean the num of operations grows at the same rate as the size of the input grows. This algorithm does grow, but at a very slow pace. Which it would make me assume that it's Logarithmic Time.


b)	O(n log n)		-	The algorithm runs one operation per input elements, but it also does some aditional work for each one. It doesn't grows in a quadratic pattern, cause the aditional work in not that much. Which leads me to assume the algorithm is Log-linear time


c) 	O(n)			-	The algorithm grows as the input grows, in a recuring way. That's why I believe it's Linear time.

## Exercise II


To minimize the amount of broken eggs we can use a binary search since it searches for a target dividing the mount of floors and starting to test from the middle of the amount of floors. the runtime complexity would be O(logn) because of the repited loops till we find the right floor.

While the egg breaks, I would divide the amount of floors and do a test from the middle. If the egg breaks, set a new high or low based on which half would be closer to the target we are trying to find (the floor from which the egg doesn't break). If it doesn't, return the floor in which the egg didn't break.

We can keep repeating the process till we reach the egg friendly floor.
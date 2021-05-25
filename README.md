# Breadth-first-search-find-goal

There's a grid of pixels and the task is to reach at all the four corners from a single pixel inside the grid, covering the minimum number of pixels. 
One is allowed to move in eight directions as is shown in Fig. 1, if a connection is available. Write an algorithm to generate all the four paths.

#### Fig.1 
![1](https://user-images.githubusercontent.com/59218287/119479932-6f2aab00-bd51-11eb-8faa-52302539adcc.jpg)

For example, let there be a 5×8 grid and we have to start from pixel number 20.<br> All the pixels are numbered in row-wise manner starting from '1', 
as is shown in Fig. 2. The required sequences of pixels to be followed so as to reach each of the four corners are marked in Fig. 2.

#### Fig.2
![2](https://user-images.githubusercontent.com/59218287/119479937-705bd800-bd51-11eb-89bf-896614191847.jpg)

## Input:
•	Line 1 contains three space integers M, N, and S, i.e. the size of the grid is M×N and starting pixel is S.<br>
•	Following M×N lines contains space separated 9 numbers. The first is an integer, say i, representing a pixel number followed by a sequence of eight bits (0/1) showing the directions one can move from pixel i. The order in which directions are considered in the given sequence of bits is same as shown in Fig. 1.<br>
## Output:
•	There will be four lines in the output. Each line contains space separated pixel numbers that are to be followed to reach a corner from the given starting pixel.<br>
•	First line contains path to corner 1 as shown in Fig. 2.<br>
•	Second line contains path to corner 2 as shown in Fig. 2.<br>
•	Third line contains path to corner 3 as shown in Fig. 2.<br>
•	Fourth line contains path to corner 4 as shown in Fig. 2.<br>
## Constraints
All values range in between 1 and 1000.
## Sample Input:
5 8 20<br>
1 0 0 1 1 1 0 0 0<br> 
2 0 0 1 0 1 1 1 0 <br>
3 0 0 1 1 0 1 1 0 <br>
4 0 0 0 0 1 1 1 0 <br>
5 0 0 1 1 1 0 0 0 <br>
6 0 0 1 1 1 1 1 0 <br>
7 0 0 1 1 0 1 1 0 <br>
8 0 0 0 0 1 0 1 0 <br>
9 1 1 1 0 1 0 0 0 <br>
10 1 1 0 0 0 1 1 1 <br>
11 0 1 1 1 0 0 0 0 <br>
12 1 0 0 0 1 1 1 1 <br>
13 1 1 0 0 1 0 0 0 <br>
14 1 1 1 1 0 0 0 1 <br>
15 0 0 0 0 1 1 1 1 <br>
16 1 0 0 0 1 0 0 1<br>
17 1 1 0 0 1 0 0 0 <br>
18 0 0 1 1 1 0 0 0 <br>
19 0 1 1 1 0 1 1 0 <br>
20 1 0 0 0 1 0 1 1 <br>
21 1 0 0 0 1 0 0 0 <br>
22 0 1 1 0 1 0 0 0 <br>
23 1 0 0 0 0 1 1 1 <br>
24 1 0 0 0 0 0 0 0<br>
25 1 0 0 1 1 0 0 0 <br>
26 1 1 1 1 0 0 0 0 <br>
27 0 0 0 0 1 0 1 1 <br>
28 1 0 0 1 1 0 0 1 <br>
29 1 0 0 0 1 1 0 0 <br>
30 1 1 0 1 1 0 0 0 <br>
31 0 0 1 1 1 1 0 0 <br>
32 0 0 0 0 1 1 1 0<br>
33 1 0 1 0 0 0 0 0 <br>
34 0 0 0 0 0 0 1 1 <br>
35 1 0 0 0 0 0 0 1 <br>
36 1 1 1 0 0 0 0 0 <br>
37 1 0 0 0 0 0 1 1 <br>
38 1 1 1 0 0 0 0 0 <br>
39 1 1 1 0 0 0 1 1 <br>
40 1 0 0 0 0 0 1 1<br>
## Sample Output:
20 12 3 2 1 <br>
20 28 36 29 21 13 6 7 8<br> 
20 12 3 10 17 25 33 <br>
20 28 36 29 21 13 6 15 22 30 39 40<br>

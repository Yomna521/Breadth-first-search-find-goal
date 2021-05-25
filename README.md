# Breadth-first-search-find-goal

There's a grid of pixels and the task is to reach at all the four corners from a single pixel inside the grid, covering the minimum number of pixels. 
One is allowed to move in eight directions as is shown in Fig. 1, if a connection is available. Write an algorithm to generate all the four paths.

#### Fig.1 
![1](https://user-images.githubusercontent.com/59218287/119479932-6f2aab00-bd51-11eb-8faa-52302539adcc.jpg)

For example, let there be a 5×85×8 grid and we have to start from pixel number 2020. All the pixels are numbered in row-wise manner starting from '1', 
as is shown in Fig. 2. The required sequences of pixels to be followed so as to reach each of the four corners are marked in Fig. 2.

#### Fig.2
![2](https://user-images.githubusercontent.com/59218287/119479937-705bd800-bd51-11eb-89bf-896614191847.jpg)

## Input:
•	Line 1 contains three space integers MM, NN and SS, i.e. the size of the grid is M×NM×N and starting pixel is SS.
•	Following M×NM×N lines contains space separated 9 numbers. The first is an integer, say ii, representing a pixel number followed by a sequence of eight bits (0/1) showing the directions one can move from pixel ii. The order in which directions are considered in the given sequence of bits is same as shown in Fig. 1.
Output:
•	There will be four lines in the output. Each line contains space separated pixel numbers that are to be followed to reach a corner from the given starting pixel.
•	First line contains path to corner 1 as shown in Fig. 2.
•	Second line contains path to corner 2 as shown in Fig. 2.
•	Third line contains path to corner 3 as shown in Fig. 2.
•	Fourth line contains path to corner 4 as shown in Fig. 2.
## Constraints
All values range in between 1 and 1000.
## Sample Input:
5 8 20
1 0 0 1 1 1 0 0 0 
2 0 0 1 0 1 1 1 0 
3 0 0 1 1 0 1 1 0 
4 0 0 0 0 1 1 1 0 
5 0 0 1 1 1 0 0 0 
6 0 0 1 1 1 1 1 0 
7 0 0 1 1 0 1 1 0 
8 0 0 0 0 1 0 1 0
9 1 1 1 0 1 0 0 0 
10 1 1 0 0 0 1 1 1 
11 0 1 1 1 0 0 0 0 
12 1 0 0 0 1 1 1 1 
13 1 1 0 0 1 0 0 0 
14 1 1 1 1 0 0 0 1 
15 0 0 0 0 1 1 1 1 
16 1 0 0 0 1 0 0 1
17 1 1 0 0 1 0 0 0 
18 0 0 1 1 1 0 0 0 
19 0 1 1 1 0 1 1 0 
20 1 0 0 0 1 0 1 1 
21 1 0 0 0 1 0 0 0 
22 0 1 1 0 1 0 0 0 
23 1 0 0 0 0 1 1 1 
24 1 0 0 0 0 0 0 0
25 1 0 0 1 1 0 0 0 
26 1 1 1 1 0 0 0 0 
27 0 0 0 0 1 0 1 1 
28 1 0 0 1 1 0 0 1 
29 1 0 0 0 1 1 0 0 
30 1 1 0 1 1 0 0 0 
31 0 0 1 1 1 1 0 0 
32 0 0 0 0 1 1 1 0
33 1 0 1 0 0 0 0 0 
34 0 0 0 0 0 0 1 1 
35 1 0 0 0 0 0 0 1 
36 1 1 1 0 0 0 0 0 
37 1 0 0 0 0 0 1 1 
38 1 1 1 0 0 0 0 0 
39 1 1 1 0 0 0 1 1 
40 1 0 0 0 0 0 1 1
## Sample Output:
20 12 3 2 1 
20 28 36 29 21 13 6 7 8 
20 12 3 10 17 25 33 
20 28 36 29 21 13 6 15 22 30 39 40

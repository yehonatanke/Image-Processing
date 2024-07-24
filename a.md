
### Image Processing Adjacency

In image processing, the terms **4-adjacency**, **8-adjacency**, and **m-adjacency** refer to different types of pixel connectivity:

#### 4-Adjacency
- Pixels are 4-adjacent if they share an edge.
- This includes the horizontal and vertical neighbors of a pixel.

Example:
```
0 1 0
1 P 1
0 1 0
```
Here, the pixel $\( P \)$ is 4-adjacent to the pixels marked as 1.

#### 8-Adjacency
- Pixels are 8-adjacent if they share an edge or a corner.
- This includes horizontal, vertical, and diagonal neighbors.

Example:
```
1 1 1
1 P 1
1 1 1
```
Here, the pixel $\( P \)$ is 8-adjacent to all the pixels marked as 1.

#### m-Adjacency (Mixed Adjacency)
- Mixed adjacency combines 4-adjacency and 8-adjacency.
- Pixels $\( P \)$ and $\( q \)$ are m-adjacent if:
  - $\( q \)$ is in the 8-neighborhood of $\( P \)$.
  - The intersection of the 4-neighborhoods of $\( P \)$ and $\( q \)$ is empty.

### Example Analysis
Given two subsets $\( S_1 \)$ and $\( S_1 \)$ and the following figure:

```
  0 0 0 1 0 0 0 0
  0 1 1 1 0 0 1 1
  0 1 P 1 0 1 0 1
  0 1 1 0 0 1 1 1
  0 0 0 0 0 0 0 0
```
- **4-Adjacency**: $\( S_1 \)$ and $\( S_1 \)$ are not 4-connected because $\( q \)$ is not in the 4-neighborhood of $\( P \)$.
- **8-Adjacency**: $\( S_1 \)$ and $\( S_1 \)$ are 8-connected because $\( q \)$ is in the 8-neighborhood of $\( P \)$.
- **m-Adjacency**: $\( S_1 \)$ and $\( S_1 \)$ are m-connected because $\( q \)$ is in the diagonal neighborhood $\( N_D(p) \)$, and the 4-neighborhoods of $\( P \)$ and $\( q \)$ do not overlap.

### $N_D(p)$
- $N_D(p)$ is the set of diagonal neighbors of pixel $p$.
- Diagonal neighbors are located at:
  - $(x-1, y-1)$
  - $(x-1, y+1)$
  - $(x+1, y-1)$
  - $(x+1, y+1)$



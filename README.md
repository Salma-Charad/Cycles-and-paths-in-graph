-- Salma Charad --

## Topic
Graph Theory

## What is it about? 

Given a graph, The code checks if it has only `cycles` and `paths` as components, and if so, The following details are given: 

- If the graph contains only cycles and paths or not
- The number of vertices in each of the found cycles and paths. 

## How does it work

First, we check if every vertex is of degree 1 or 2. If any other degree is encountered, the graph is rejected.

Finding the `paths` :

- We can start with a degree 1 vertex, and keep follwing next, next until we finish that path. 
We tore the number of vertices and separately keep track of whom you have visited.
- Now we check if there is another unvisited degree 1 vertex. We start there and follow, follow until done.
- This way we finish processing all the paths.
        
Finding the `cycles`: 

- Then, we process the cycles by starting at one place and following until we come back.
- Along the way we should have recorded sizes of all the paths and cycle.

## Sample Input 1
```json
enter number of vertices: 6
enter number of edges: 4
Enter edge: 1 2
Enter edge: 2 3
Enter edge: 4 5
Enter edge: 5 6
```

## Sample Output 1 
```json
This graph has only paths and cycles as components.
The graph contains 2 Path(s) of size 3
```

## Sample Input 2
```json
enter number of vertices: 8
enter number of edges: 7
Enter edge: 1 2
Enter edge: 2 3
Enter edge: 3 4
Enter edge: 4 1
Enter edge: 5 6
Enter edge: 6 7
Enter edge: 7 8
```

## Sample Output 2
```json
This graph has only paths and cycles as components.
The graph contains 1 Path(s) of size 4
The graph contains 1 Cycle(s) of size 4
```



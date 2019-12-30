# Graph

## DFS
1. prepare: 
    1. build the graph
    2. define seen set
2. main call
    1. traverse all possible start point
    2. expand to all possible direction
    3. call dfs function
3. dfs function
    1. expand to all possible direction
    2. recursive call dfs function

### DFS Template

1. DFS-LOOP(graph G)
    - mark all nodes unvisited
    - for each vertex v in G:
        - if v not yet visited
            - DFS(G,v)
2. DFS(graph G, start vertext S)
    - if s is visiting:
        - return there is a cycle
    - mark s visiting
    - for every edge (S,v)
        - if v not yet visited
            - DFS(G,v)
    - mark s visited


## BFS Template

1. BFS
    - add start point to Q
    - initialize visited matrix
    - when Q is not empty
        - pop vertex v from Q
        - for every edge (v,u)
            - if u not yet visited
                - add u to Q
                - label u is visited


## Dijkstra's Algorithm  (Shortest Path Algorithm)

### Description
1. An algorithm run on a weighted path
2. starts with an initial node and a goal node
3. Finds the least cost path to the goal node.

### O(N^2)
1. Build the graph
2. Create a set of unvisited node
3. Assigne to every a tentative distant value and assign to start node zero
4. Start from current node (it's the start node at the first time)
5. update its neighbours distance
6. mark current node visited
7. Select smallest distant in unvisited node and go to 3
8. there is no unvisited node, algorithm end

### O(Nlog(N)) with priority queue
1. Build the graph
2. Create a priority queue for start node.
3. Create empty set for distant,
    a. if unvisited, it's not in distant, we continue 3 to calcuate
    b. if visited, it's in  distant, and its neighbours must be the smallest distant. Dijstra algorithms' gurantee
4. Start from the node with smallest dist.
5. if neighbour not in dist, add neighbour to queue. if in, mean neigbour previous distant is smallest, do not need process.
6. mark current node visited
7. Select smallest distant in unvisited node and go to 3
8. there is no unvisited node, algorithm end

## Topological sort
### If a directed graph has a  cycle, no way to have a topological ordering
### DFS:

    1. constructed graph adjacent list
    2. visited 3 status, 0 not yet visited, 1 visited, -1 visiting.
    3. if the vertex not visited, start visiting, meet some visiting, there is a cycle, return false; 
    4. meet some visited, return true, since subproblem is successfully completed.
    5. When successfully visited all the subproblems. return True. make this source vertex visited

### BFS:
    1. construct indegree cnt
    2. construct outdegree graph using adjacent list
    3. construct a queue includes all the vertices without indegree .
    4. BFS visited new vertex, and remove this edge,  which mean the indegree of this new vertex -1, if new vertex has no indegree, add it into queue.
    5. if queue is empty, and the indegree of all vertex is zero. return true
    6. else return false

### BFS Topological Sort

1. BFS Topological Sort
    - L = empty list that will store the sorted elements
    - Set of all nodes with no incoming edge
    - While S in non-empty 
        - remove a node n from S
        - add n t tail of L
        - for node m with an edge from n to m 
            - remove edge  e from the graph
            - if m has no other incoming edges
                - insert m into s
    - if graph has edges
        - return False
    - else
        - return L

### Leetcode
1. Course Schedule (207, 210), Alien Dictionary (269), Graph Valid Tree
    1. how to build graph, directed or undirected 
        1. undirected, how to check the cycle: Graph valid tree
            1. need one more parameter, parent, des != parent
    2. undirected graph, one start, directed graph, more started, since there are nodes without indegree
    3. undirected graph, one start, and check whether has node don't connected

## Union-Find / Disjoint Set
#### make union

```
def makset(x):
    for x in the list:
        if x is not already present, add x to the disjoint-set tree:
            x.parent = x
            x.rank = 0
            x.size = 1
```

#### Path compression

```
def find(x):
    if x.parent ! = x:
        x.parent = find(x.parent)
    return x.parent
    
```

```
def find(self,x):
        while x!=self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
```

#### Union
1. By rank: 
    1. always attaches the shorter tree tot he root of the taller tree, thus, the result tree is no taller than the originals
    2. if they were of equal height, in the resulting tree is taller by one node.
    
    ```
    def union(x,y):
        xRoot = find(x)
        yRoot = find(y)
        # x and y are already in the same set
        if xRoot == yRoot: return
        
        # x and y are not in the same set, so we merge them
        if xRoot.rank < yRoot.rank:
            xRoot, yRoot = yRoot, xRoot
        
        #merge yRoot into xRoot
        yRoot.parent = xRoot
        if xRoot.rank == yRoot.rank:
            xRoot.rank += 1
    ```
2. bysize 
    1. union by size always attaches the tree with fewer elements to the root of the tree having more elements.
    
    ```
    def Union(x,y):
        xRoot = find(x)
        yRoot = find(y)
        
        if xRoot == yRoot: return
        
        if xRoot.size < yRoot.size:
            xRoot, yRoot = yRoot, xRoot
        
        yRoot.parent = xRoot
        xRoot.size += yRoot.size
        
    ```
    
#### Time complexity

#### Explanation
1. Usually, if a problem could be solved by union-find, if also could solved by DFS and BFS
2. Comparing

    DFS/BFS | Union-Find
    -------------|---------------
     | create UF class: <br> 1. typically, init; find; union <br> 2. some times, isConnected
     build graph <br> build visited set| convert all the element to id. <br>union all the elements
     DFS/BFS out loop for start point | group elements to different union
     
#### Examples

1. 721 Account Merge
    1. when union all the elements. just union with all others. Then all the elements are union.
2. 737 Sentence Similarity II
    1. when use union-find, build uf, should connect both pairs and words
    2. when use DFS, build graph, only connect pairs
        1. since in DFS, we will consider the situation that element == itself.
3. 684 Redundant connections in indirect graph
4. 685 Redundant connections in direct graph

## DFS + pruning == dp

#### 1066 campus bikes II

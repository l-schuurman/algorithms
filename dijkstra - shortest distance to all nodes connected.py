# This is an implementation of the common Dijkstra's algorithm for finding the shortest paths between nodes in a graph
# This code uses an adjacency list, created using nested lists
# Assumes the graph is weighted, undirected, and connected

# OUTPUT FORMAT
# A list where the ith integer is the shortest disance of the ith node from the source node

# Solution to GeeksforGeeks "Implmeneting Dijkstra Algorithm"
# https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1#

import sys

# Implements the greedy behaviour by determining the minimum node to be considered next
def minNode(dist, visited):
    min = sys.maxsize
    
    for node in range(len(dist)):
        if dist[node] < min and visited[node] == False:
            min = dist[node]
            index = node
            
    return index

# Performs the Dijkstra algorithm
def dijkstra(V, adj, S):
        
        dist = [sys.maxsize] * V
        visited = [False] * V
        
        dist[S] = 0

        # Keep iterating until all nodes are visited. 
        # The graph is assumed to be connected, so this condition is guaranteed to terminate.
        while not all(visited):

            # Determine the current node
            current = minNode(dist, visited)

            # Iterate through all edges connected to the current node
            for adjacent, weight in adj[current]:
                if visited[adjacent] == True:
                    continue
                
                # Update the distance if a shorter path exists
                newDist = dist[current] + weight
                if dist[adjacent] > newDist:
                    dist[adjacent] = newDist
            
            # Update visited status
            visited[current] = True
            
        return dist

# Driver code to accept input and output result
T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    adj = [[] for i in range(V)]

    for i in range(E):
        u, v, w = map(int, input().split())
        adj[u].append([v, w])
        adj[v].append([u, w])

    S = int(input())

    result = dijkstra(V, adj, S)

    print(*result)
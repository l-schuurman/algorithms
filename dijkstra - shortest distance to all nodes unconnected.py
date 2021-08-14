# This is an implementation of the common Dijkstra's algorithm for finding the shortest paths between nodes in a graph
# This code uses an adjacency list, created using defaultdict
# Assumes the graph is weighted, undirected, and unconnected

# OUTPUT FORMAT
# A list of integers denoting shortest distance to each node
# from the starting position, in increasing order of labels, excluding the source node

# Solution to HackerRank "Dijkstra: Shortest Reach 2"
# https://www.hackerrank.com/challenges/dijkstrashortreach/problem

import sys
from collections import defaultdict

# Use 
input = sys.stdin.readline

# Implements the greedy behaviour by determining the minimum node to be considered next
def minNode(dist, visited):
    min = sys.maxsize
    index = -1
    
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

            # Determine the current node, terminate early if no new node is possible
            current = minNode(dist, visited)
            if current == -1:
                break

            # Iterate through all edges connected to the current node            
            for adjacent, weight in adj[current].items():
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
    adj = defaultdict(lambda: defaultdict(lambda:sys.maxsize))

    for i in range(E):
        u, v, w = map(int, input().split())

        # The input nodes are not zero=based index, so decrement nodes by 1
        adj[u-1][v-1] = min(adj[u-1][v-1], w)
        adj[v-1][u-1] = min(adj[v-1][u-1], w)

    # Decrement source node by 1 as well
    S = int(input()) - 1

    result = dijkstra(V, adj, S)
    for node, dist in enumerate(result):
        if node == S:
            continue
        elif dist == sys.maxsize:
            print(-1, end=" ")
        else:
            print(dist, end=" ")
            
    print() # Print new line between each testcase
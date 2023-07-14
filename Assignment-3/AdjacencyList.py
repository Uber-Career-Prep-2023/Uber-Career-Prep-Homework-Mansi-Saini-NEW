# Question: Adjacency List
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 40+ min - took a lot of research to understand how adjacency lists/sets works

# import statements
from collections import defaultdict, deque   
import pdb

"""
    Goal: Build an Adjacency List/Set Representation of a Graph
    Params: edges
    Output: create an adjacency list/set
"""
def adjacencySet(edges):
    graph = {}
    for first_node, second_node in edges:
        # edge case: make sure that there exists a first node
        if first_node not in graph:
            graph[first_node] = []
        # edge case: make sure there exists a second node
        if second_node not in graph:
            graph[first_node] = []
        graph[first_node].append(second_node)

    return graph


"""
    Goal: BFS Algorithm - search for a target by finding a path from start to the target
    Params: starting point, target value, and neighbors
    Output: boolean if value was found
    time complexity O(V+E), space complexity: O(V) - source google
"""
def bfs(start, target, neighbors):
    # initialize queue and items to visit
    queue = deque([start])
    visited = set([start])
    # continue until all relevant nodes have not been processed
    while queue:
        curr = queue.popleft()
        # the current node is equal to our target node
        if curr == target:
            return True
        # add nodes that haven't been visited into the visited array
        for neighbor in neighbors[curr]:
            # make sure no duplicates exist
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    # all other cases, value wasn't present
    return False

"""
    Goal: DFS Algorithm - search for a target by finding a path from start to the target
    Params: starting point, target value, and neighbors
    Output: boolean if value was found
    time complexity O(V+E), space complexity: O(V) - source google
"""
def dfs(start, target, neighbors):
    to_process = [start]
    visited = set([start])
    # continue utnil all nodes have been processed
    while to_process:
        curr = to_process.pop() # pop the current node off to process
        # we have found our target value
        if curr == target:
            return True
        # update our visited array with nodes that we have visited
        for neighbor in neighbors[curr]:
            # make sure no duplicates are added in visited
            if neighbor not in visited:
                visited.add(neighbor)
                to_process.append(neighbor)
    # all other cases, value was not present
    return False

# method: first count the in-degree of each node, find the nodes with 0 in-degree and pop those nodes, then add the
# rest of the additional nodes in the correct topological ordering
# time complexity O(V+E), space complexity: O(V)

"""
    Goal: Calculate each node's in-degree; pop nodes with 0 in degree and reorder the remaining nodes in topological order
    Params: graph
    time complexity O(V+E), space complexity: O(V) - source google
"""
def topologicalSort(graph):
    # calculate each node's in degree
    in_degrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degrees[neighbor] += 1

    # figure out which nodes have a 0 in degree
    zero_in_degree = []
    for node in in_degrees:
        if in_degrees[node] == 0:
            zero_in_degree.append(node)

    # pop and update nodes from the zero-indegree list
    topological_order = []
    while len(zero_in_degree) > 0:
        node = zero_in_degree.pop()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return topological_order

if __name__ == "__main__":
    # TEST CASES
    in_edges = [(1, 2), (2, 3), (1, 3), (3, 2), (4, 5)]
    test_in_graph = adjacencySet(in_edges)
    print(test_in_graph) 
    # {1: [2, 3], 2: [3], 3: [2], 4: [5], 5: []}

    # BFS TEST CASES
    print("TESTING BFS: ", bfs(1, 2, test_in_graph)) # True
    # print("TESTING BFS: ", bfs(4, 3, test_in_graph)) # False
    print("TESTING BFS: ", bfs(1, 3, test_in_graph)) # True

    # DFS TEST CASES
    print("TESTING DFS: ", dfs(2, 2, test_in_graph)) # True
    print("TESTING DFS: ", dfs(2, 3, test_in_graph)) # True
    print("TESTING DFS: ", dfs(1, 4, test_in_graph)) # False

    # GRAPH - TOPOLOGICAL ORDERING TEST CASES
    test_graph_edges = [(1, 2), (2, 3), (1, 3), (3, 4), (3, 5), (4, 5), (2, 4)]
    test_graph_in = adjacencySet(test_graph_edges)
    # print("TESTING TOPO SORT: ", topologicalSort(test_graph_in)) # topological ordering output is [1,2,3,4,5] as expected
    more_edges = [(1, 5), (2, 3), (1, 3), (3, 4), (4, 5)]
    more_in = adjacencySet(more_edges)
    # print("TESTING TOPO SORT: ", topologicalSort(more_in)) # topological ordering output is [2,1,3,4,5] as expected
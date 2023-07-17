# Question: RoadNetworks
# Technique Used: Depth-first Search w/ Adjacency List
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 43 min

from collections import defaultdict, deque

"""
    Goal: Create an adjacency list of the road network so we don't have to search over and over again
    Params: roads
    Output: adjacency list
"""
def create_adjacency_list(network):
    adjacency_list = defaultdict(list) # init adjacency list
    for town_one, town_two in network: # split town pairs into individual towns
        # add them to adjacency list
        adjacency_list[town_one].append(town_two)
        adjacency_list[town_two].append(town_one)
    return adjacency_list

"""
    Goal: Go through all possible roads in a town
    Parameters: town, beginning point, and visited nodes
"""
def dfs(town, begin, visited_town):
    visited_town.add(begin) # add initial node to visited
    for road in town[begin]: # go through graph nodes
        if road not in visited_town: # ensure neighbor node has not been visited
            dfs(town, road, visited_town) # continue depth-first search


"""
    Goal: Given a list of towns and a list of pairs representing roads between towns, return the number of road networks.
    Parameters: town list, pairs list
    Output: number of road networks
"""
def RoadNetworks(towns_list, roads_list):
    # edge case check: empty network
    if (len(roads_list) == 0):
        return 0
    
    # create adjacency list so we don't have to keep searching over and over again
    adj_list = create_adjacency_list(roads_list)
    count_networks = 0 # init output counter
    visited_towns = set() # keep track of visited towns

    # go through towns and find networks
    for i in adj_list:
        if i not in visited_towns: # if we haven't visited the town yet
            # perform depth first search to go through all possible roads in a town
            dfs(adj_list, i, visited_towns)
            count_networks += 1 # increment number of networks
    
    return count_networks # output number of networks

# Test Cases
if __name__ == "__main__":
    in_towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy",
                   "Copper Center", "Healy"]
    in_roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"),
                   ("Anchorage", "Copper Center"),
                   ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    # print(RoadNetworks(test_one))
    assert RoadNetworks(in_towns, in_roads) == 2
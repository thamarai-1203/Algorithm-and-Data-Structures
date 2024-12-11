#imports libraries
import math
from heapq import heappop, heappush
from typing import Dict, List, Tuple
import itertools
#creates the clss Node
class Node:
    def __init__(self, label: str) -> None:
        self.label = label
        self.adjacentNodes = {}
        self.dist = math.inf
        self.parent = None
#function that adds connection using weight
    def add_connection(self, node: 'Node', weight: int) -> None:
        self.adjacentNodes[node] = weight

#function that adds connection using weight
    def remove_connection(self, node: 'Node') -> None:
        if node in self.adjacentNodes:
            del self.adjacentNodes[node]
#method 'It' compares the nodes
    def __lt__(self, other: 'Node') -> bool:
        return self.label < other.label

class Graph:
    def __init__(self):
        self.nodes = [] #creates list to store graphs
# function that adds nodes in graph
    def add_node(self, node: Node) -> None:
        if node not in self.nodes:
            self.nodes.append(node)
        pass
#function that removes nodes in graph
    def remove_node(self, node: Node) -> None:
        if node in self.nodes:
            self.nodes.remove(node)
            for n in self.nodes:
                n.remove_connection(node)
        pass
#function  which add nodes between the two nodes with given weight
    def add_edge(self, from_node: Node, to_node: Node, weight: int) -> None:
        if from_node in self.nodes and to_node in self.nodes:
            from_node.add_connection(to_node, weight)
            to_node.add_connection(from_node, weight)
        pass
#function defines dijkstra algorithm
    def dijkstra(self, source_node: Node) -> Dict[Node, int]: #weighted graph
        if source_node not in self.nodes:
            return {}
        for u in self.nodes:
            u.dist = math.inf # distance is infinity
            u.parent = None # parent is nil
        source_node.dist = 0
        S = set()#empty set stores nodes
        Q = [(0, source_node.label, source_node)]

        while Q:
            current_distance, _, u = heappop(Q)
            if u in S:
                continue
            S.add(u) #adding u to s

            for v, weight in u.adjacentNodes.items(): #checks possibility to reach nodes efficiently from u
                self.relax(u, v, weight, Q)

        return {node: node.dist for node in self.nodes}

#function relaxation
    def relax(self, u, v, weight, Q):
        if v.dist > u.dist + weight:
            v.dist = u.dist + weight
            v.parent = u
            heappush(Q, (v.dist, v.label, v))
        pass
#function defines kruskal algorithm
    def kruskal(self) -> List[Tuple[int, Node, Node]]:
        A = []
        parent = {node: node for node in self.nodes}
        rank = {node: 0 for node in self.nodes}
#creates the edge list and sorts from node to node using weights
        edges = sorted(
            (weight, from_node, to_node)
            for from_node, to_node in itertools.combinations(self.nodes, 2)
            if to_node in from_node.adjacentNodes
            for weight in [from_node.adjacentNodes[to_node]]
        )

        for weight, u, v in edges:
            if self.find(parent, u) != self.find(parent, v):# checks u an v in same set
                A.append((weight, u, v)) #adds edges to the minimum spanning tree
                self.union(parent, rank, u, v)#unions the set of u and v

        return A #returns the edges of minimum spanning tree
#function find
    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]
# function defines union of sets u and v
    def union(self, parent, rank, u, v):
        root_u = self.find(parent, u) #finds the root in set u
        root_v = self.find(parent, v) #finds the root in set v

        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u #chooses the root
                rank[root_u] = rank[root_u]+1 #increments the root
        pass

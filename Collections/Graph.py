# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:18:29 2020

@author: nitin
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        
class Edge(object):
    def __init__(self, node_from, node_to, value):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to
        
class Graph(object):
    
    def __init__(self, Nodes = None, Edges = None):
        
        self.nodes = Nodes or []
        self.edges = Edges or []
        
    def insert_node(self, nodeValue):
        node = Node(nodeValue)
        self.nodes.append(node)
        
    def insert_edge(self, node_from_value, node_to_value, edgeValue):
        node_from = None
        node_to = None
        for node in self.nodes:
            if node.value == node_from_value:
                node_from = node
            if node.value == node_to_value:
                node_to = node
            if node_from and node_to:
                break
        
        if not node_from:
            node_from = Node(node_from_value)
            self.nodes.append(node_from)
            
        if not node_to:
            node_to = Node(node_to_value)
            self.nodes.append(node_to)
            
        newEdge = Edge(node_from, node_to, edgeValue)
        self.edges.append(newEdge)
        
        node_from.edges.append(newEdge)
        node_to.edges.append(newEdge)
        
    def getEdgeList(self):
        # Returns (Edge Value, From Node Value, To Node Value) 
        edgeList = [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]
        
        return edgeList
    
    def getAdjacencyList(self):
        # For each node and corresponding outbound edge, returns (To Node, Edge Value)
        adj_list = []
        
        for node in self.nodes:
            out_edges = [edge for edge in self.edges if node.value != edge.node_to.value and node.value == edge.node_from.value]
            adj_list.append([(edge.node_to.value, edge.value) for edge in out_edges])
            
        adj_list = [node_adj_list if node_adj_list else None for node_adj_list in adj_list]
            
        return adj_list
    
    def getAdjacencyMatrix(self):
        """Return a 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        adj_matrix = []
        
        allNodes = [(nodeFrom.value, nodeTo.value) for nodeFrom in self.nodes for nodeTo in self.nodes]
        
        allEdges = {(edge.node_from.value, edge.node_to.value): edge.value for edge in self.edges}
        
        adj_matrix = [allEdges[nodeCombination] if nodeCombination in allEdges else 0 for nodeCombination in allNodes ]
        
        num_nodes = len(self.nodes)
        
        adj_matrix = [adj_matrix[i:i+num_nodes] for i in range(0, num_nodes**2, num_nodes)]
            
        return adj_matrix
    
    
graph = Graph()

graph.insert_edge(1, 2, 10)
graph.insert_edge(1, 3, 20)
graph.insert_edge(1, 4, 30)
graph.insert_edge(2, 3, 40)
graph.insert_edge(4, 5, 50)

print("\nEdge List:")
print(graph.getEdgeList())

print("\nAdjacency List:")
print(graph.getAdjacencyList())

print("\nAdjacency Matrix:")
print(graph.getAdjacencyMatrix())
                
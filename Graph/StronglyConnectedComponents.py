# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 23:52:45 2020

@author: nitin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:18:29 2020

@author: nitin
"""

# Strongly Connected Components for a directed graph using Kosaraju's Algorithm

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        
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
    
  
    def _clearVisited(self):
        for node in self.nodes:
            node.visited = False
            
    def findNode(self, nodeValue):
        for node in self.nodes:
            if nodeValue == node.value:
                return node
        return None
    
    def dfsHelper(self, start, stack):
        # Outgoing Edges Only
        start.visited = True
        out_edges = [e for e in start.edges if e.node_to.value != start.value]
        for edge in out_edges:
            if not edge.node_to.visited:
                self.dfsHelper(edge.node_to, stack)
        
        stack = stack.append(start)    
        
    def SCCHelper(self, stack, current, currentSCC, SCC):
        
        current.visited = True
        out_edges = [e for e in current.edges if e.node_from.value != current.value]
        currentSCC.append(current.value)
        
        for edge in out_edges:
            if not edge.node_from.visited: # Transpose of the Graph
                self.SCCHelper(stack, edge.node_from, currentSCC, SCC)
        
        if currentSCC not in SCC:
            SCC.append(currentSCC) # Append the SCC sub graph
        
        while stack and stack[-1].visited:
            stack.pop().value
        
        if not stack:
            return
    
        
        currentSCC = []
        current = stack.pop()
        self.SCCHelper(stack, current, currentSCC, SCC)
        
         
    def StronglyConnectedComponents(self, startNodeValue):
        self._clearVisited()
        stack = []
        start  = self.findNode(startNodeValue)
        # Build a Stack of Vertices using their Finish Time when doing DFS
        self.dfsHelper(start, stack)
        
        self._clearVisited()
        current = stack.pop()
        # Do a DFS again on the traspose of the Graph
        SCC = [] # All the Strongly Connected Component subgraph
        currentSCC = [] # Current Strongly Connected Component Subgraph values
        self.SCCHelper(stack, current, currentSCC, SCC)
        return SCC
        
        
    
    
graph = Graph()


'''
graph.insert_edge(0, 1, 40)
graph.insert_edge(1, 2, 20)
graph.insert_edge(2, 3, 20)
graph.insert_edge(3, 0, 10)
graph.insert_edge(2, 4, 30)
graph.insert_edge(4, 5, 20)
graph.insert_edge(5, 6, 10)
graph.insert_edge(6, 7, 30)
graph.insert_edge(6, 4, 30)
'''
# Graph: https://en.wikipedia.org/wiki/Strongly_connected_component#/media/File:Scc.png
graph.insert_edge(0, 1, 40)
graph.insert_edge(1, 2, 20)
graph.insert_edge(2, 3, 20)
graph.insert_edge(3, 2, 10)
graph.insert_edge(3, 7, 30)
graph.insert_edge(7, 3, 30)
graph.insert_edge(7, 6, 30)
graph.insert_edge(6, 5, 30)
graph.insert_edge(5, 6, 30)
graph.insert_edge(4, 5, 30)
graph.insert_edge(4, 0, 30)
graph.insert_edge(1, 4, 30)
graph.insert_edge(1, 5, 30)
graph.insert_edge(2, 6, 30)

print("\nStrongly Connected Components:")
print(graph.StronglyConnectedComponents(0))
                
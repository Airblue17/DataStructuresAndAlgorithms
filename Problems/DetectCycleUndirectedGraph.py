# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:20:21 2020

@author: nitin
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, node_from, node_to, edgeValue):
        self.node_from = node_from
        self.node_to = node_to
        self.value = edgeValue
        
class Graph(object):
    
    def __init__(self, Nodes = None, Edges = None):
        self.nodes = Nodes or []
        self.edges = Edges or []
        
    def insert_node(self, nodeValue):
        node = Node(nodeValue)
        self.nodes.append(node)
        
    def insert_edge(self, node_from_value, node_to_value, edge_value):
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
            
        newEdge = Edge(node_from, node_to, edge_value)
        node_from.edges.append(newEdge)
        node_to.edges.append(newEdge)
        
        self.edges.append(newEdge)
        
    def _clearVisited(self):
        for node in self.nodes:
            node.visited = False
            
    def findStartNode(self, startNodeValue):
        for node in self.nodes:
            if node.value == startNodeValue:
                start = node
        return start
    
    def dfsHelper(self, start):
        ret_list = [start.value]
        start.visited = True
        out_edges = [e for e in start.edges if e.node_to.value != start.value]
        
        for edge in out_edges:
            if not edge.node_to.visited:
                edge.node_to.parent = start
                edge.node_to.ancestor  = start.ancestor.copy()
                edge.node_to.ancestor.append(start.value)
                ret_list.extend(self.dfsHelper(edge.node_to))
            else:
                if edge.node_to.value in start.ancestor and edge.node_to.value != start.parent.value:
                    #print((start.value, edge.node_to.value, edge.node_to.parent.value))
                    print("Cycle in Graph")
        return ret_list
    
    
    def dfsRecursive(self, startNodeValue):
        self._clearVisited()
        start = self.findStartNode(startNodeValue)
        start.parent = Node(-1)
        start.ancestor = []
        return self.dfsHelper(start)

            
        
        
 
graph = Graph()

graph.insert_edge(1, 2, 10)
graph.insert_edge(2, 1, 10)

graph.insert_edge(1, 3, 20)
graph.insert_edge(3, 1, 20)

graph.insert_edge(1, 4, 30)
graph.insert_edge(4, 1, 30)

graph.insert_edge(2, 3, 40)
graph.insert_edge(3, 2, 40)

graph.insert_edge(4, 5, 50)
graph.insert_edge(5, 4, 50)

graph.insert_edge(2, 6, 25)
graph.insert_edge(6, 2, 25)

#graph.insert_edge(3, 6, 55)
#graph.insert_edge(6, 3, 55)
 
print("\nRecursive Depth First Search")
print(graph.dfsRecursive(1))
    

print("\nDFS with 4 as start value")
print(graph.dfsRecursive(4))

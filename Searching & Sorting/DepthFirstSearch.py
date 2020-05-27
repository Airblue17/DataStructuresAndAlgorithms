# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:31:52 2020

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
    
    def dfsR_helper(self, startNode):
        ret_list = [startNode.value]
        startNode.visited = True
        out_edges = [edge for edge in startNode.edges if startNode.value != edge.node_to] #Outbound Edges
        
        for edge in out_edges:
            if not edge.node_to.visited:
                ret_list.extend(self.dfsR_helper(edge.node_to))
            
        return ret_list

    def dfsRecursive(self, startNodeValue):
        self._clearVisited()
        start = self.findStartNode(startNodeValue)
        return self.dfsR_helper(start)
    
    def dfsIterative(self, startNodeValue):
        self._clearVisited()
        start = self.findStartNode(startNodeValue)
        
        ret_list = []
        ret_list.append(startNodeValue)
        start.visited = True
        
        current = start
        nodeStack = []
        nodeStack.append(start)

        while nodeStack:
            out_edges = [edge for edge in current.edges if current.value != edge.node_to and edge.node_to.visited == False]
            for edge in out_edges:
                nodeStack.append(edge.node_to)
                edge.node_to.visited = True
                ret_list.append(edge.node_to.value)
                current = edge.node_to
                break
            
            if not out_edges:
                nodeStack.pop()
                
            if len(nodeStack) != 0:
                current = nodeStack[-1]
                
        return ret_list
            
 
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

graph.insert_edge(3, 6, 55)
graph.insert_edge(6, 3, 55)
        
print("\nRecursive Depth First Search")
print(graph.dfsRecursive(1))
        
print("\nIterative Depth First Search")
print(graph.dfsIterative(1))
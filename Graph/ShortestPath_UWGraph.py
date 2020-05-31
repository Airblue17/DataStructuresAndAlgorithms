# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:25:09 2020

@author: nitin
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, node_from, node_to):
        self.node_from = node_from
        self.node_to = node_to
        
class Graph(object):
    
    def __init__(self, Nodes = None, Edges = None):
        self.nodes = Nodes or []
        self.edges = Edges or []
        
    def insert_node(self, nodeValue):
        node = Node(nodeValue)
        self.nodes.append(node)
        
    def insert_edge(self, node_from_value, node_to_value):
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
            
        newEdge = Edge(node_from, node_to)
        node_from.edges.append(newEdge)
        node_to.edges.append(newEdge)
        
        self.edges.append(newEdge)
        
    def _clearVisited(self):
        for node in self.nodes:
            node.visited = False
            
    def findNode(self, startNodeValue):
        for node in self.nodes:
            if node.value == startNodeValue:
                start = node
        return start

    def dist_init(self, start):
        dist = {}
        shortest_path = {}
        dist[start.value] = 0
        for node in self.nodes:
            if node.value != start.value:
                dist[node.value] = float('inf')
            shortest_path[node.value] = [node.value]
        return dist, shortest_path
        
    
    def shortestPath(self, startNodeValue):
        self._clearVisited()
        
        current = self.findNode(startNodeValue)
        dist, shortest_path = self.dist_init(current)
        ret_list = []
        
        def enqueue(queue, node):
            node.visited = True
            queue.append(node)
            
        def outgoing_unvisited_edge(node, edge):
            return ((node.value == edge.node_from.value) and (not edge.node_to.visited))
        
        nodes_queue = []
        enqueue(nodes_queue, current)
        
        while nodes_queue:
            current = nodes_queue.pop(0)
            ret_list.append(current.value)
            for edge in current.edges:
                dist_update_cond =  dist[edge.node_to.value] > (dist[edge.node_from.value] + 1)
                if dist_update_cond and current.value == edge.node_from.value:
                    shortest_path[edge.node_to.value] = []
                    shortest_path[edge.node_to.value].extend(shortest_path[edge.node_from.value])
                    
                    shortest_path[edge.node_to.value].append(edge.node_to.value)
                    
                    dist[edge.node_to.value] = dist[edge.node_from.value] + 1
                    
                if outgoing_unvisited_edge(current, edge):
                    enqueue(nodes_queue, edge.node_to)
                    
        shortest_path = {k:[val for val in v if val != k] for k,v in shortest_path.items()}
        
        return ret_list, dist, shortest_path
    
        
        
        
            
 
graph = Graph()

graph.insert_edge(1, 2)
graph.insert_edge(2, 1)

graph.insert_edge(1, 3)
graph.insert_edge(3, 1)

graph.insert_edge(2, 3)
graph.insert_edge(3, 3)

graph.insert_edge(2, 4)
graph.insert_edge(4, 2)


graph.insert_edge(3, 4)
graph.insert_edge(4, 3)

graph.insert_edge(3, 5)
graph.insert_edge(5, 3)

graph.insert_edge(4, 5)
graph.insert_edge(5, 4)

graph.insert_edge(4, 6)
graph.insert_edge(6, 4)

graph.insert_edge(5, 6)
graph.insert_edge(6, 5)


_, dist, shortest_path = graph.shortestPath(1)
print("Distance:",dist)
print("Shortest Path:", shortest_path)
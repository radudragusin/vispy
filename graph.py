##
## Authors: Kim Lundsteen Juncher and Brian Soborg Mathiasen
## Insitute of Computer Science, Copenhagen University, Denmark
##
##
##
## graph.py
##
## LICENSED UNDER: GNU General Public License v2
##

import matplotlib.pyplot as plt
import networkx as nx
import random as r
import datastructure as abstract

class Graph(abstract.GraphDatastructure):
    def __init__ (self):
        self.nodes = []
        self.edges = []
        self.last_added_node = -1
        self.last_added_edge = -1
        self.edgeIdCount = 0
        plt.ion()
        self.G = nx.Graph()
        self.oldGNodes = []
        self.oldGEdges = []
        self.pos = {}

    def addNode(self, node_id):
        if node_id == self.last_added_node: return
        for node in self.nodes:
            if node.getId() == node_id:
                return
        self.nodes.append(Node(node_id))
        self.last_added_id = node_id
        
    def addEdge(self, (node_id_1, node_id_2), weight=0): 
#        if edge_id == self.last_added_edge: return False
#        for edge in self.edges:
#            if edge.getId() == edge_id:
#                return False
        if self.nodeExists(node_id_1) or self.nodeExists(node_id_2):
            edge_id = self.edgeIdCount
            self.edgeIdCount += 1
            newedge = Edge(edge_id, (node_id_1, node_id_2), weight)
            self.edges.append(newedge)
            return
        return False
    
    def removeNode(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                self.nodes.remove(node)
                adjEdges = self.getAdjEdges(node_id)
                self.removeEdges(adjEdges)
                return True
        return False

    def nodeExists(self, node_id):
        for node in self.nodes:
            if node.getId() == node_id:
                return True
        return False

    def edgeExists(self, (node_id_1, node_id_2)):
        for edge in self.edges:
            if ((edge.start_node, edge.end_node) == (node_id_1, node_id_2)):
                return True
        return False
    
    def removeEdge(self, (node_id_1, node_id_2)):
        for edge in self.edges:
            if ((edge.start_node, edge.end_node) == (node_id_1, node_id_2)) or ((edge.start_node, edge.end_node) == (node_id_2, node_id_1)):
                self.edges.remove(edge)
                return True
        return False

    def removeEdges(self, edge_list):
        # suppose edge_list is list of sets
        for edge in edge_list:
            self.removeEdge(edge)
        return True

    def getNodes(self):
        return [n.getId() for n in self.nodes]
    
    def getEdges(self): 
        return [(e.start_node, e.end_node) for e in self.edges]
    
    def degreeList(self): 
        return False
    
    def getAdjEdges(self, node_id):
        buf = []
        for edge in self.edges:
            if edge.start_node == node_id or edge.end_node == node_id:
                buf.append((edge.start_node, edge.end_node))
        return buf

    def getAdjNodes(self, node_id):
        buf = []
        adjEdges = self.getAdjEdges(self, node_id)
        for edge in adjEdges:
            if edge.start_node == node_id:
                buf.append(edge.end_node)
            elif edge.end_node == node_id:
                buf.append(edge.start_node)
        return buf
        
    def isEdge(self, (node_id_1, node_id_2)):
        return self.edgeExists((node_id_1, node_id_2))
    
    def getNode(self, node_id): 
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return False
    
    def vizMe(self, figNum=1, markEdges=[], markNodes=[], savefig=None, savefig_format='png', nodeLabels=None):
        plt.figure(figNum, facecolor='white')
        plt.clf()
        plt.axis('off')
        self.G.clear()
        for node in self.nodes:
            self.G.add_node(node.id)

        for edge in self.edges:
            self.G.add_edge(edge.start_node,edge.end_node)
            
        if (not self.oldGNodes and not self.oldGEdges) or (not self.oldGNodes == self.G.nodes() or not self.oldGEdges == self.G.edges()):
            self.pos = nx.spring_layout(self.G)

        self.oldGNodes = self.G.nodes()
        self.oldGEdges = self.G.edges()

        if not markNodes and not markEdges:
            nx.draw_networkx_nodes(self.G, self.pos, node_color='#557A66')#, edge_color='#272E2E')
            nx.draw_networkx_edges(self.G, self.pos)#, edge_color='#272E2E')
            nx.draw_networkx_labels(self.G, self.pos, labels=nodeLabels)
#            nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=nodeLabels)
# drawing edge labels are only avaliable from networkX 1.1 and beyond
        else:
            unmarkedNodes = list(set(self.G.nodes()).difference(markNodes))
            unmarkedEdges = list(set(self.G.edges()).difference(markEdges))

            nx.draw_networkx_nodes(self.G, self.pos, nodelist=unmarkedNodes, node_color='#557A66')#, node_size=700)
            nx.draw_networkx_nodes(self.G, self.pos, nodelist=markNodes, node_size=700, node_color='#9ed95e')
            # E82B1E <- roed sort trae
            nx.draw_networkx_edges(self.G, self.pos, edgelist=unmarkedEdges)#, edge_color='#272E2E')#, width=6)
            nx.draw_networkx_edges(self.G, self.pos, edgelist=markEdges,width=6)#, edge_color='#272E2E')

            nx.draw_networkx_labels(self.G, self.pos, labels=nodeLabels)

        if savefig:
            plt.savefig(savefig, format=savefig_format)

    def vizMeNot(self):
        self.pos = {}
        plt.close()
        
    def random(self, n):
        self.clear()
        nodeId = 0
        self.addNode(nodeId)
        for i in range(1,n):
            neighbor = r.randint(0,len(self.nodes)-1)
            nodeId += 1
            self.addNode(i)
            self.addEdge((i, neighbor))
                
    def __str__(self):
        return
#        G = nx.graph()
#        for node in self.nodes:
#            G.add_node()
    
    def empty(self): 
        self.clear()
    
    def clear(self): 
        self.nodes = []
        self.edges = []



class Node:
    def __init__(self, node_id, label=None):
        self.id = node_id
        self.label = label
        
    def getId(self):
        return self.id
        
    def getLabel(self):
        if not self.label:
            return self.getId()
        return self.label
    
class Edge:
    def __init__(self, edge_id, (start_node_id, end_node_id), weight):
        self.id = edge_id
        self.weight = weight
        self.start_node = start_node_id
        self.end_node = end_node_id
            
    def getId(self):
        return self.id
    def getWeight(self):
        return self.weight
    
    

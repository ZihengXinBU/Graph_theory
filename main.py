# Python program to create an undirected
# graph and add nodes and edges to a graph

# To import package
import networkx as nx
import sympy
import matplotlib.pyplot as plt
from sympy import *

# To create an empty undirected graph
G = nx.Graph()
G.clear()

# To add a node
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(7)
G.add_node(9)

# To add an edge
# Note graph is undirected
# Hence order of nodes in edge doesn't matter
G.add_edge(1, 2)
G.add_edge(3, 1)
G.add_edge(2, 4)
G.add_edge(4, 1)
G.add_edge(9, 1)
G.add_edge(1, 7)
G.add_edge(2, 9)

# To get all the nodes of a graph
node_list = G.nodes()
print("#1")
print(node_list)

# To get all the edges of a graph
edge_list = G.edges()
print("#2")
print(edge_list)

# To remove a node of a graph
#G.remove_node(3)
#node_list = G.nodes()
#print("#3")
#print(node_list)

# To remove an edge of a graph
G.remove_edge(1, 2)
edge_list = G.edges()
print("#4")
print(type(edge_list))
print(edge_list)

# To find number of nodes
n = G.number_of_nodes()
print("#5")
print(n)

# To find number of edges
m = G.number_of_edges()
print("#6")
print(m)

# To find degree of a node
# d will store degree of node 2
d = G.degree(2)
print("#7")
print(d)

# To find all the neighbor of a node
neighbor_list = G.neighbors(2)
print("#8")
print(neighbor_list)

# To delete all the nodes and edges
#G.clear()

#G: It refers to the Tutte graph object
#node_size: It refers to the size of nodes.
#node_color: It refers to color of the nodes.
#nx.draw(G)#, node_size=15, node_color='green')
#plt.show()


#networkx.tutte_polynomial(G)

#P = nx.complete_graph(5)
#n = 1
#P.neighbors(n)
#list(P.neighbors(n))
#nx.draw(P)
#plt.show()


# calculation with unknown x y
#x = Symbol('x')
#y = Symbol('y')
#print((x+1)+(y+1))

#T_G = nx.tutte_graph(G)
#nx.draw(T_G)
#plt.show()

T_G = nx.tutte_polynomial(G)
print(T_G)
#nx.draw(T_G)
#plt.show()

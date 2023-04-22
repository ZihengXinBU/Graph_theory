import networkx as nx
import matplotlib.pyplot as plt
from sympy.abc import x, y

# create an undirected graph
G = nx.Graph()

# read the CSV file
#with open('AIDS_A.txt', 'r') as f:
with open('input.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        column1, column2 = line.strip().split(",")
        if G.has_node(column1):
            pass
        else:
            G.add_node(column1)
        if G.has_node(column2):
            pass
        else:
            G.add_node(column2)
        G.add_edge(column1, column2)

# define the node labels as a dictionary
node_labels = {node: node for node in G.nodes()}

# draw the graph with labels and a spring layout
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)

# remove axis labels and ticks
plt.axis('off')

print("edges:", list(G.edges))

T_G = nx.tutte_polynomial(G)
print(T_G)

# find cycles in the graph
cycles = nx.cycle_basis(G)
# nx.cycle_basis() function because it finds only simple cycles (i.e., cycles that do not repeat edges).

# T_G(1, 1) counts the number of spanning trees of G
print("spanning trees:", T_G.subs({x: 1, y: 1}).as_coefficients_dict()[1])
# T_G(1, 2) counts the number of connected spanning subgraphs of G
print("connected spanning subgraphs:", T_G.subs({x: 1, y: 2}).as_coefficients_dict()[1])
# T_G(2, 1) counts the number of spanning forests in G
print("spanning forests:", T_G.subs({x: 2, y: 1}).as_coefficients_dict()[1])
# T_G(0, 2) counts the number of strong orientations of G
print("strong orientations:", T_G.subs({x: 0, y: 2}).as_coefficients_dict()[1])
# T_G(2, 0) counts the number of acyclic orientations of G
print("acyclic orientations:", T_G.subs({x: 2, y: 0}).as_coefficients_dict()[1])


def group_cycles(cycles):
    # Initialize a list to store groups of cycles
    cycle_groups = []

    # Iterate over each cycle in the list of cycles
    for cycle in cycles:
        # Check if the cycle shares edges with any existing cycle group
        group_found = False
        for group in cycle_groups:
            if set(cycle).intersection(group):
                group_found = True
                group.update(cycle)
                break

        # If the cycle does not share edges with any existing group, create a new group
        if not group_found:
            cycle_groups.append(set(cycle))

    # Convert the set of edges in each group to a sorted list and return the list of groups
    return [sorted(list(group)) for group in cycle_groups]

cycle_component = group_cycles(cycles)
k = 0
for cycle in cycle_component:
    k += 1

print("number of cycle components: " + str(k))
#print(cycle_component)

# Print the Tutte polynomial for each cycle component
for component in cycle_component:
    component_G = G.subgraph(component)
    T_component_G = nx.tutte_polynomial(component_G)
    print("Tutte polynomial for component {}: {}".format(component, T_component_G))

plt.show()

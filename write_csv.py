import csv

# Define the edges of the graph
edges = [(8, 2), (1, 3), (3, 4), (3, 6), (6, 4), (1, 6), (5, 2),
         (8, 5), (6, 7), (1, 8), (4, 3), (7, 4), (7, 9), (9, 1),
         (2, 10), (10, 11), (11, 12), (12, 10)]
print(len(edges))
# Write the edges to a CSV file
with open('input.csv', 'w', newline='') as csvfile:
    fieldnames = ['source', 'target']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    for edge in edges:
        writer.writerow({'source': edge[0], 'target': edge[1]})

# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Búsqueda en anchura:")
print(search.breadth_first_graph_search(ab).path())
print("\nBúsqueda en profundidad:")
print(search.depth_first_graph_search(ab).path())
print("\n\n===== Práctica 1b =====")
print("\nBúsqueda con la heurística discutida en clase (pathcost+straight-line distance):")
print(search.practica_1b(ab).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

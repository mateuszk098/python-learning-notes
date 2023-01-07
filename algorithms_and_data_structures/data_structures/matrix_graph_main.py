"""
Matrix Graph naive test. I propose to draw example graphs on a sheet of paper first.
"""

from my_types import matrix_graph as mg


def main():

    mg1 = mg.MatrixGraph(5)
    for x, y in ((0, 2), (1, 0), (1, 3), (1, 4), (3, 2), (3, 3), (4, 2), (4, 3)):
        mg1.add_new_edge(x, y)

    mg2 = mg.MatrixGraph(5)
    for x, y in ((0, 1), (2, 1), (4, 0)):
        mg2.add_new_edge(x, y)

    mg3 = mg.composition(mg1, mg2)
    mg3.print_graph("graph", "Composition of mg1 and mg2:")

    mg4 = mg.MatrixGraph(6)
    for x, y in ((0, 3), (0, 5), (1, 2), (2, 4), (3, 1), (3, 4), (5, 4), (4, 5), (5, 2)):
        mg4.add_new_edge(x, y)
    mg4.print_graph("graph", "Initial graph:")

    mg4.warshall()
    mg4.print_graph("warshall", "Warshall:")

    mg4.create_paths()
    mg4.print_graph("routing", "Routing matrix:")

    for x in range(mg4.size):
        for y in range(mg4.size):
            try:
                print(f"Path from {x} to {y}:", end=" ")
                mg4.print_path(x, y)
            except Exception as e:
                print(e)
    print()

    mg5 = mg.MatrixGraph(7)
    for x, y in ((0, 3), (0, 1), (1, 2), (1, 4), (2, 3), (2, 4), (4, 5), (4, 6), (5, 6), (6, 3)):
        mg5.add_new_edge(x, y)
    mg5.print_graph("graph", "Floyd")

    mg5.floyd_warshall()

    for i in range(mg5.size):
        for j in range(mg5.size):
            if mg5.floyd_warshall_matrix[i][j] == float("inf"):
                print(f"{i} -> {j}: There is no path.")
            else:
                if i != j:
                    print(f"{i} -> {j}: ", end="")
                    mg5.floyd_warshall_path(i, j)
                    print()
    print()

    mg5.dfs_search()


if __name__ == "__main__":
    main()

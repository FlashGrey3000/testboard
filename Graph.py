class Graph:
    def __init__(self):
        self.nodes = dict()

    def add_node(self, node: Node):
        self.nodes[node.val] = node

    def add_edge(self, from_val, to_val):
        self.nodes[from_val].add_neighbour(self.nodes[to_val])


    def print_graph(self):
        for node in self.nodes.values():
            print(f"Node: {node.val} -> {[n.val for n in node.neighbours]}")

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []
    
    def add_neighbour(self, node: Node):
        self.neighbours.append(node)


if __name__ == '__main__':
    g = Graph()
    n1 = Node(10)
    n2 = Node(100)
    n3 = Node(3)
    n4 = Node(30)
    n5 = Node(7)
    n6 = Node(70)
    n7 = Node(700)

    n1.add_neighbour(n2)

    n3.add_neighbour(n4)
    n3.add_neighbour(n7)

    n5.add_neighbour(n6)
    n6.add_neighbour(n7)

    n7.add_neighbour(n1)
    n5.add_neighbour(n2)

    n2.add_neighbour(n4)

    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)
    g.add_node(n5)
    g.add_node(n6)
    g.add_node(n7)

    g.print_graph()

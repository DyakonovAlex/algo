class Edge:
    __slots__ = ('weight', 'v1', 'v2')

    def __init__(self, weight: int, v1: str, v2: str):
        self.weight = weight
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return f"{self.v1} --- {self.v2} (weight = {self.weight})"

    def __repr__(self):
        return str(self)


class Graph:
    __slots__ = ('edges', 'vertex')

    def __init__(self, edges: list = None):
        self.edges = edges
        self.vertex = set()
        for e in self.edges:
            self.vertex.add(e.v1)
            self.vertex.add(e.v2)

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)
        self.vertex.add(edge.v1)
        self.vertex.add(edge.v2)

    def get_edges(self) -> list:
        return self.edges

    def get_vertex(self) -> set:
        return self.vertex

    def display(self, caption: str) -> None:
        print()
        print("=" * 10, caption, "=" * 10)
        for g in self.edges:
            print(g)
        print("=" * 25)


def main():
    # Граф задан массивом ребер
    count_edge = 11
    edges = [object for _ in range(count_edge)]

    edges[0] = Edge(weight=7, v1='A', v2='B')
    edges[1] = Edge(weight=8, v1='B', v2='C')
    edges[2] = Edge(weight=5, v1='C', v2='E')
    edges[3] = Edge(weight=7, v1='B', v2='E')
    edges[4] = Edge(weight=5, v1='A', v2='D')
    edges[5] = Edge(weight=15, v1='D', v2='E')
    edges[6] = Edge(weight=6, v1='D', v2='F')
    edges[7] = Edge(weight=8, v1='F', v2='E')
    edges[8] = Edge(weight=11, v1='F', v2='G')
    edges[9] = Edge(weight=9, v1='E', v2='G')
    edges[10] = Edge(weight=9, v1='D', v2='B')

    graph = Graph(edges)
    graph.display("GRAPH")
    print()

    print("=" * 10, "Set vertex", "=" * 10)
    for v in graph.get_vertex():
        print(v)
    print("=" * 25)
    print()

    # Сортируем ребра
    sort_edges = sorted(graph.get_edges(), key=lambda edge: edge.weight)
    print("=" * 10, "sorted edges", "=" * 10)
    for e in sort_edges:
        print(e)
    print("=" * 25)
    print()

    # Для каждой вершины будем хранить номер дерева, к которому она принадлежит
    vertex_tree = {v: i for i, v in enumerate(graph.get_vertex())}

    skeleton = []
    for e in sort_edges:
        new_id = vertex_tree.get(e.v1)
        old_id = vertex_tree.get(e.v2)
        if new_id != old_id:
            skeleton.append(e)
            for k, v in vertex_tree.items():
                if v == old_id:
                    vertex_tree[k] = new_id

    # Минимальное остовное дерево
    print("=" * 10, "Skeleton", "=" * 10)
    for s in skeleton:
        print(s)
    print("=" * 25)


if __name__ == '__main__':
    main()

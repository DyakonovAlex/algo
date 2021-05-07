import math


def get_vertex(min_dist, used_vertex) -> int:
    amin = -1
    m = math.inf
    for v, d in enumerate(min_dist):
        if d[0] < m and v not in used_vertex:
            m = d[0]
            amin = v
    return amin


def main():
    # Граф задан матрицей смежности
    graph = ((0, 2, 3, 6, math.inf, math.inf, math.inf),         # A
             (2, 0, 4, math.inf, 9, math.inf, math.inf),         # B
             (3, 4, 0, 1, 7, 6, math.inf),                       # C
             (6, math.inf, 1, 0, math.inf, 4, math.inf),         # D
             (math.inf, 9, 7, math.inf, 0, 1, 5),                # E
             (math.inf, math.inf, 6, 4, 1, 0, 8),                # F
             (math.inf, math.inf, math.inf, math.inf, 5, 8, 0))  # G

    # Число вершин в графе
    vertex_cnt = len(graph)

    v_start = 0  # A
    v_end = 6    # G

    # Минимальное расстояние от начальной до остальных вершин (расстояние, откуда_пришли)
    min_dist = [(math.inf, -1)] * vertex_cnt

    v = v_start

    # Обработанные вершины
    used_vertex = {v}
    min_dist[v] = (0, 0)

    while v != -1:
        for next_vertex, next_dist in enumerate(graph[v]):
            if next_vertex not in used_vertex:
                dist = min_dist[v][0] + next_dist
                if dist < min_dist[next_vertex][0]:
                    min_dist[next_vertex] = (dist, v)

        v = get_vertex(min_dist, used_vertex)
        if v >= 0:
            used_vertex.add(v)

    # Расстояние от начальной до остальных вершин
    for d in min_dist:
        print(d)
    print()

    # Путь от начальной до конечной вершин
    path = [v_end]
    while v_end != v_start:
        v_end = min_dist[path[-1]][1]
        path.append(v_end)

    print(path[::-1])


if __name__ == '__main__':
    main()

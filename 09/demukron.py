
def print_matrix(matrix):
    for rows in matrix:
        for vi in rows:
            print(vi, end=' ')
        print()


def sum_col(matrix, col):
    return sum(rows[col] for rows in matrix)


def main():
    # Граф задан матрицей смежности
    print()
    print('=' * 100)
    print()

    num_vertex = 14
    adj_matrix = [[0] * num_vertex for _ in range(num_vertex)]

    # 1 -> 3, 1 -> 13
    adj_matrix[0][2] = 1
    adj_matrix[0][12] = 1

    # 2 -> 13
    adj_matrix[1][12] = 1

    # 3 -> None

    # 4 -> 3
    adj_matrix[3][2] = 1

    # 5 -> 3, 5 -> 9, 5 -> 10
    adj_matrix[4][2] = 1
    adj_matrix[4][8] = 1
    adj_matrix[4][9] = 1

    # 6 -> 4, 6 -> 11, 6 -> 12, 6 -> 13
    adj_matrix[5][3] = 1
    adj_matrix[5][10] = 1
    adj_matrix[5][11] = 1
    adj_matrix[5][12] = 1

    # 7 -> 6
    adj_matrix[6][5] = 1

    # 8 -> 2, 8 -> 4, 8 -> 6, 8 -> 14
    adj_matrix[7][1] = 1
    adj_matrix[7][3] = 1
    adj_matrix[7][5] = 1
    adj_matrix[7][13] = 1

    # 9 -> 1, 9 -> 7
    adj_matrix[8][0] = 1
    adj_matrix[8][6] = 1

    # 10 -> 1, 10 -> 12, 10 -> 14
    adj_matrix[9][0] = 1
    adj_matrix[9][11] = 1
    adj_matrix[9][13] = 1

    # 11 -> 3
    adj_matrix[10][2] = 1

    # 12 -> None

    # 13 -> 3
    adj_matrix[12][2] = 1

    # 14 -> 11
    adj_matrix[13][10] = 1

    print_matrix(adj_matrix)

    print()
    print('=' * 100)
    print()

    # Сумма колонок
    sum_cols = [sum_col(adj_matrix, i) for i in range(num_vertex)]

    vertex_levels = []
    while True:
        # Вершины с полустепенью захода 0
        zeros = []
        for i, v in enumerate(sum_cols):
            if v == 0:
                sum_cols[i] = -1 # Обработали
                zeros.append(i)

        if len(zeros) == 0:
            break

        # Распределение вершин по уровням
        vertex_levels.append(zeros)

        for i in zeros:
            row = adj_matrix[i]
            for n in range(num_vertex):
                sum_cols[n] -= row[n]

    for i, v in enumerate(vertex_levels):
        print(f"{i}) {v}")


if __name__ == '__main__':
    main()

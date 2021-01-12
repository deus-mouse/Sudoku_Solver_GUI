# solver.py

# Expert
board = [
    [4, 0, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 0, 1, 0, 0, 4, 0, 9],
    [0, 0, 2, 3, 0, 0, 0, 0, 0],
    [1, 0, 0, 4, 0, 6, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 5, 3, 1, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [8, 1, 3, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 2, 0, 0, 0, 0]
]

# Medium
# board = [
#     [7, 0, 0, 0, 1, 0, 9, 0, 0],
#     [2, 0, 9, 7, 0, 3, 0, 8, 5],
#     [0, 0, 0, 9, 0, 8, 0, 0, 0],
#     [8, 9, 4, 0, 0, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 9],
#     [0, 6, 0, 5, 4, 0, 0, 2, 7],
#     [0, 0, 0, 0, 0, 0, 7, 5, 3],
#     [0, 7, 0, 3, 0, 0, 2, 0, 0],
#     [3, 8, 0, 0, 0, 0, 0, 0, 0],
# ]


def solve(bo):
    """
    Решает заданную таблицу судоку поиском через возврат.
    :param bo: 2d list of ints
    :return: solution
    """
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, pos, num):
    """
    Выдает значение если попытка подбора успешна
    :param bo: 2d list of ints
    :param pos: (row, col) / (линия, столбец)
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check сol
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(bo):
    """
    Ищет пустые клетки в таблице
    :param bo: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def print_board(bo):
    """
    Печатает таблицу в консоль
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


print(len(board))
print('Дано:')
print_board(board)
print('Запуск поиска решения...')
solve(board)
print('Решено!')
print_board(board)



from typing import List, Tuple, Iterable, Optional, Dict
from copy import deepcopy

Board = List[List[str]]
Path = List[Tuple[int, int]]
board_1 = [
    ["A", "D", "O", "B"],
    ["D", "S", "U", "R"],
    ["O", "T", "A", "N"],
    ["O", "R", "I", "W"],
]
words = []
POSSIBLE_MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """this function returns None if the path is not valid or it is creating a not valid word,
        otherwise it returns the word created"""
    if len(path) == 0:
        return

    board_points = all_points_in_board(board)
    word = ""
    twice_same_point = sorted(path) != sorted(list(set(path)))
    possible_coordinates = [path[0]]

    if twice_same_point:
        return None

    # Starting point
    if path[0] not in board_points:
        return None

    for point in path:
        if point not in possible_coordinates:
            return None

        possible_coordinates = list(
            map(
                lambda tuple: (point[0] + tuple[0], point[1] + tuple[1]), POSSIBLE_MOVES
            )
        )
        temp_list = [value for value in board_points if value in possible_coordinates]
        possible_coordinates = deepcopy(temp_list)

        # Concatenate word
        word += board[point[0]][point[1]]

    if word not in words:
        return None
    return word


# def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
#     points_in_board_list = all_points_in_board(board)
#     path_list = []
#     for point in points_in_board_list:
#         _helper_find_length_n_path(board, [point], n, path_list)
#     return path_list

# def _helper_find_length_n_path(board: Board, path: Path, n: int, paths_list: List) -> None:
#     if len(path) == n:
#         valid = is_valid_path(board, path, words)
#         if valid != None:
#             paths_list.append(deepcopy(path))
#             return
#         else:
#             return

# if not is_in_board(path, board):
#     return

# for move in POSSIBLE_MOVES:
#     last_point = path[-1]
#     path.append((last_point[0] + move[0], last_point[1] + move[1]))
#     _helper_find_length_n_path(board, path, n, paths_list)
#     path = path[: len(path) - 1]


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    points_in_board_list = all_points_in_board(board)
    path_list = []
    for point in points_in_board_list:
        _helper_find_length_n_path(board, [point], n, path_list, words)
    return path_list


def _helper_find_length_n_path(
    board: Board, path: Path, n: int, paths_list: List, words: Iterable[str]
) -> None:
    if len(path) == n:
        valid = is_valid_path(board, path, words)
        if valid != None:
            paths_list.append(deepcopy(path))
            return
        else:
            return

    if not is_in_board(path, board):
        return

    for move in POSSIBLE_MOVES:
        last_point = path[-1]
        new_point = (last_point[0] + move[0], last_point[1] + move[1])
        if is_in_board([new_point], board):
            path.append(new_point)
            _helper_find_length_n_path(board, path, n, paths_list, words)
            path.pop()


def is_in_board(path: Path, board: Board) -> bool:
    i, j = path[-1]
    return (
        0 <= i < len(board)
        and 0 <= j < len(board[0])
        and path[-1] not in path[: len(path) - 1]
    )


# def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
#     path_list = []
#     points_in_board_list = all_points_in_board(board)
#     for point in points_in_board_list:
#         _helper_find_length_n_words(board, [point], n, path_list, board[point[0]][point[1]])
#     return path_list


# def _helper_find_length_n_words(board: Board, path: Path, n: int, paths_list: List, word: str):
#     points_in_board_list = all_points_in_board(board)
#     if len(word) == n:
#         if is_valid_path(board, path, words) != None:
#             paths_list.append(deepcopy(path))
#         return

#     if not is_in_board(path, board):
#         return

#     for move in POSSIBLE_MOVES:
#         last_point = path[-1]
#         new_point = (last_point[0] + move[0], last_point[1] + move[1])
#         if new_point in points_in_board_list:
#             path.append(new_point)
#             word = word + board[new_point[0]][new_point[1]]
#             _helper_find_length_n_words(board, path, n, paths_list, word)
#             path.pop()
#             word = word[:-1]


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    path_list = []
    points_in_board_list = all_points_in_board(board)
    for point in points_in_board_list:
        _helper_find_length_n_words(
            board, [point], n, path_list, board[point[0]][point[1]], words
        )
    return path_list


def _helper_find_length_n_words(
    board: Board, path: Path, n: int, paths_list: List, word: str, words: Iterable[str]
):
    if len(word) == n:
        if is_valid_path(board, path, words) != None:
            paths_list.append(deepcopy(path))
        return

    if not is_in_board(path, board):
        return

    new_words = [sub for sub in words if word in sub]
    if len(new_words) == 0:
        return

    for move in POSSIBLE_MOVES:
        last_point = path[-1]
        new_point = (last_point[0] + move[0], last_point[1] + move[1])
        if new_point in all_points_in_board(board):
            path.append(new_point)
            word = word + board[new_point[0]][new_point[1]]
            _helper_find_length_n_words(board, path, n, paths_list, word, new_words)
            path.pop()
            word = word[:-1]


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    word_dict = dict()
    all_points = all_points_in_board(board)
    path_list = []

    for point in all_points:
        _helper_max_score_path(board, words, [point], word_dict)

    for path in word_dict.values():
        path_list.append(path)

    return path_list


def _helper_max_score_path(
    board: Board, words: Iterable[str], path: Path, word_dict: Dict
):
    cur_word = is_valid_path(board, path, words)
    if cur_word != None:
        if cur_word not in word_dict:
            word_dict[cur_word] = deepcopy(path)
        else:
            if len(path) > len(word_dict[cur_word]):
                word_dict[cur_word] = deepcopy(path)

    if len(path) == 16:
        return

    if not is_in_board(path, board):
        return

    cur_path_string = find_word_with_path(board, path)
    new_words = [sub for sub in words if cur_path_string in sub]
    if len(new_words) == 0:
        return

    for move in POSSIBLE_MOVES:
        last_point = path[-1]
        new_move = (last_point[0] + move[0], last_point[1] + move[1])
        path.append(new_move)
        _helper_max_score_path(board, new_words, path, word_dict)
        path.pop()


def find_word_with_path(board: Board, path: Path) -> str:
    word = ""
    for i, j in path:
        word = word + board[i][j]
    return word


def all_points_in_board(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board[0]))]


def open_words_file(file_name):
    with open(file_name) as Words_dict:
        for word in Words_dict:
            words.append(word.split()[0])


open_words_file("boggle_dict.txt")
# print(is_valid_path(board_1, [(0, 2), (1, 2), (1, 3)], words))
# find_length_n_paths(3, board_1, words)
# print("--------------------------")
# find_length_n_words(3, board_1, words)
# print(find_length_n_words(3, board_1, words))
# print(find_length_n_words(4, board_1, words))
#
# print(find_length_n_words(8, board_1, words))
# print(len(max_score_paths(board_1, words)))


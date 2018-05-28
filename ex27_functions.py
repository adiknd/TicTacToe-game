import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def change_player(player):
    if player == 1:
        return 2
    else:
        return 1


def change_character(character):
    if character == 'X':
        return 'O'
    else:
        return 'X'


def check_result_by_line(board_list):

    for i in range(3):
        set_line = set(board_list[i])
        if len(set_line) == 1 and board_list[i][0] != 0:
            return board_list[i][0]
    return 0


def check_result_diagonal(board_list):
    if board_list[1][1] != 0:
        if board_list[0][0] == board_list[1][1] == board_list[2][2]:
            return board_list[1][1]
        elif board_list[0][2] == board_list[1][1] == board_list[2][0]:
            return board_list[1][1]
    else:
        return 0


def reverse_list(board_list):
    reversed_list =[]
    for i in range(3):
        sublist = []
        for j in range(3):
            sublist.append(board_list[j][i])
        reversed_list.append(sublist)
    return reversed_list


def check_draw(board_list):
    for i in board_list:
        if ' ' in i:
            return False
    return True


def check_result_all_in_one(board_list):
    if check_result_by_line(board_list) != 0:
        result = check_result_by_line(board_list)
        return result
    elif check_result_by_line(reverse_list(board_list)) != 0:
        result = check_result_by_line(reverse_list(board_list))
        return result
    elif check_result_diagonal(board_list) != 0:
        result = check_result_diagonal(board_list)
        return result


def draw_gameboard(board):
    print(" --- --- --- ")
    print("| %s | %s | %s |" % (board[0][0], board[0][1], board[0][2]))
    print(" --- --- --- ")
    print("| %s | %s | %s |" % (board[1][0], board[1][1], board[1][2]))
    print(" --- --- --- ")
    print("| %s | %s | %s |" % (board[2][0], board[2][1], board[2][2]))
    print(" --- --- --- ")


def insert_to_board(board, character, place):
        board[int(place[0]) - 1][int(place[1]) - 1] = character
        return board
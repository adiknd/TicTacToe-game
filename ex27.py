from ex27_functions import *


active_player = 1
player_character = "X"
running = True
is_empty = True
game_board = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]


if __name__ == '__main__':
    for i in game_board:
        print(i)
    print("################")
    print("TIC TAC TOE GAME")
    print("################")
    while running:
        draw_gameboard(game_board)
        is_empty = True
        while True:
            try:
                while is_empty:
                    player_choose = input("Player%s, enter your move (row,col): " % active_player).split(",")
                    if game_board[int(player_choose[0]) - 1][int(player_choose[1]) - 1] == ' ':
                        game_board = insert_to_board(game_board, player_character, player_choose)
                        is_empty = False
                    else:
                        print("This place is occupied! Try again.")
                break
            except Exception:
                print("Wrong value ! Try again ...")
        if check_result_all_in_one(game_board) == 'X' or check_result_all_in_one(game_board) == 'O':
            cls()
            draw_gameboard(game_board)
            print("Player%s wins !" % active_player)
            running = False
            break
        elif check_draw(game_board):
            cls()
            draw_gameboard(game_board)
            print("Draw !")
            running = False
            break
        active_player = change_player(active_player)
        player_character = change_character(player_character)
        cls()
    input("The game is over...")

    



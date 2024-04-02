#kartes izveidošana.
board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [6, 4, 2]]

def print_board():
    print(board[0], end=" | ")
    print(board[1], end=" | ")
    print(board[2])
    print("---------")
    print(board[3], end=" | ")
    print(board[4], end=" | ")
    print(board[5])
    print("---------")
    print(board[6], end=" | ")
    print(board[7], end=" | ")
    print(board[8])

#uzvaras pārbaude.
def parbaude(symbol):
    for combo in victory:
        if all(board[index] == symbol for index in combo):
            return True
    return False
#kartes pārbaude, lai tā ir pilna vai ne.
def board_full():
    return all(isinstance(cell, str) for cell in board)

#spēlētāju saraksts.
def tic_tac_toe():
    player1 = "X"
    player2 = "O"
    tagadejais_player = player1

#galvenais spēles cikls.
    #spēles sākums.
    print("Laipni lūdzam Tic-Tac-Toe spēlē!")
    print_board()

    while True:
        try:
            move = int(input(f"Spēlētājs {tagadejais_player}, ievadi jūsu koordinātas(1-9): "))
            if board[move - 1] != "X" and board[move - 1] != "O":
                board[move - 1] = tagadejais_player
            else:
                print("Šis laukums jau ir aizņemts, mēģinet vēlreiz.")
                continue
            #parbauda, lai laukums nebija aizņemts.
        except ValueError:
            print("Nepareiza ievade! Lūdzu, ievadiet numuru no 1 līdz 9.")
            continue
        #parbauda, vai spēlētajs ievadīja cipari vai burtus.
        except IndexError:
            print("Nepareizs solis! Lūdzu, ievadiet numuru no 1 līdz 9.")
            continue
        #parbauda, vai spēlētājs ievadīja pareizo koordinatu.

        print_board()

        if parbaude(tagadejais_player):
            print(f"Spēlētājs {tagadejais_player} uzvarēja!")
            break

        if board_full():
            print("Neviens neuzvarēja!")
            break

        tagadejais_player = player2 if tagadejais_player == player1 else player1

tic_tac_toe()

#automātiska konsoles aizvēršana, izpildīta tikai konsolei, Visual Studio Code nav jēgas.
print("Jums ir 15 sekundes lai uzzinātu, kurš uzvarēja pirms automātiskās konsoles aizvēršanas.")
import time
time.sleep(15)
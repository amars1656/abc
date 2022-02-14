def tictable(board):
    print(board[7]+ "|"+board[8]+"|"+board[9])
    print(board[4]+ "|"+board[5]+"|"+board[6])
    print(board[1]+ "|"+board[2]+"|"+board[3])

def playerinput():
    marker=""
    while marker not in ("x","0"):
        marker=input("enter either x or 0:")
    if marker=="x":
        return ("x","0")
    else:
        return ("0","x")

def wicncheck(board,marker):
    return((board[7]==marker and board[8]==marker and board[9]==marker)or
    (board[7]==marker and board[8]==marker and board[9]==marker)or(board[1]==marker and board[2]==marker and board[3]==marker)or
    (board[4]==marker and board[5]==marker and board[6]==marker)or(board[1]==marker and board[4]==marker and board[7]==marker)or
    (board[2]==marker and board[5]==marker and board[8]==marker)or(board[3]==marker and board[6]==marker and board[9]==marker)or
    (board[7]==marker and board[5]==marker and board[3]==marker)or(board[9]==marker and board[5]==marker and board[1]==marker))  

import random
def choicefirst():
    flip=random.randint(1,0)
    if flip==0:
        return "player1"
    else:
        return "player2"        

def spacecheck(board,position):
    return board[position]==" "

def fullboardcheck(board):
       for i in range(1,10):
           if spacecheck(board,position):
               return False
           else:
               return True     

def palyerchoice(board):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9] or not  spacecheck(board,i):
        psoition=int(input("player1 choice(1-9):"))
    return position

def replay():
    choice=input("play again! enter yes or no:")
    return choice=="yes"

print("welcome to tic toe game")
while True:
    board=[""]*10
    player1marker,player2marker=playerinput()
    turn=choicefirst()
    print(tunr+"will play first")
    playgame=input("ready to play? y or n")
    if playgame=="y":
        gameon=True
    else:
        gameon=False

    while gameon:
        if turn=="player1":
            tictable(board)
            position=playerchoice(board)
            placemarker(board,player1marker,position)
            if wincheck(board,player1marker):
                tictable(board)
                print("player1 has won!")
                gameon=False
            else:
                if fullcheckboard(board):
                    tictable(board)
                    print("tie game")
                    break
        else:
            turn=="player2"
            tictable(board)
            position=playerchoice(board)
            placemarker(board,player2marker,position)
            if wincheck(board,player2marker):
                tictable(board)
                print("player2 has won!")
                gameon=False
            else:
                if fullcheckboard(board):
                    tictable(board)
                    print("tie game")
                    break
    if not reply():
        break





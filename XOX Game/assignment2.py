import sys
n = input("What size game GoPY?")
board = []
for j in range(0,int(n)**2):
    board.append(j)
def table():
    a = 0
    while a < int(n):
        for i in range(int(n)*a,int(n)*(a+1)):
            if i< 10:
                print(" " + str(board[i]), end=" ")
            elif board[i] == "X":
                print(" " + str(board[i]), end=" ")
            elif board[i] == "O":
                print(" " + str(board[i]), end=" ")
            else:
                print(board[i], end=" ")
        print("")
        a+=1
table()
def hori():
    b = 0
    while b < int(n):
        if board[int(n)*b:(int(n)*(b+1))].count(board[int(n)*b]) == int(n):
            print("Winner: " + board[int(n)*b])
            sys.exit()
        b+=1
def vert():
    c = 0
    while c < int(n):
        if board[c:int(n)**2:int(n)].count(board[c]) == int(n):
            print("Winner: " + board[c])
            sys.exit()
        c+=1
def diag1():
    if board[0:int(n)**2:int(n)+1].count(board[0]) == int(n):
        print("Winner: " + board[0] )
        sys.exit()
def diag2():
    if board[int(n)-1:int(n)**2:int(n)-1].count(board[int(n)-1]) == int(n):
        print("Winner: " + board[int(n)-1] )
        sys.exit()
move_count = 0
go = 0
gopy = 1
while gopy ==1:
    while go != 1:
        move = int(input("Player 1 turn --> "))
        if len(board)-1 < move:
            print("Please enter a valid number")
            go = 1
        elif board[move] == move :
            board[move] = "X"
            go = 1
            move_count = move_count + 1
        elif board[move] == "X":
            print("You have made this choice before")
            go = 1
        elif board[move] == "O":
            print("The other player select this cell before")
            go = 1
    table()
    hori()
    vert()
    diag1()
    diag2()
    if move_count == int(n)**2:
        print("No winner")
        sys.exit()
    go = 0
    while go != 1:
        move = int(input("Player 2 turn --> "))
        if len(board)-1 < move:
            print("Please enter a valid number")
            go = 1
        elif board[move] == move :
            board[move] = "O"
            go = 1
            move_count = move_count + 1
        elif board[move] == "O":
            print("You have made this choice before")
            go = 1
        elif board[move] == "X":
            go = 1
            print("The other player select this cell before")
    go = 0
    table()
    vert()
    hori()
    diag1()
    diag2()
    if move_count == int(n)**2:
        print("No winner")
        sys.exit()

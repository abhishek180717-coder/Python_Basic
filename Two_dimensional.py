board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
# print(board)    
for index in board:
    print(index)
print(len(board))

print(board[0][0])

board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
# print(board)    
for index in board:
    print(index)
# print(len(board))
# print(board[0][0])
board[0][0] = "ROOKS"
board[0][7] = "ROOKS"
board[7][0] = "ROOKS"
board[7][7] = "ROOKS"
print("**********")
for index in board:
    print(index)
    
board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
# print(board)    
for index in board:
    print(index)
# print(len(board))
# print(board[0][0])
board[0][0] = "ROOKS"
board[0][7] = "ROOKS"
board[7][0] = "ROOKS"
board[7][7] = "ROOKS"

board[0][2] = "BISHOP"
board[0][5] = "BISHOP"
board[7][2] = "BISHOP"
board[7][5] = "BISHOP"

board[0][3] = "QUEEN"
board[0][4] = "KING"
board[7][3] = "QUEEN"
board[7][4] = "KING"

board[1] = ["PAWN" for i in range(8)]
board[6] = ["PAWN" for i in range(8)]

print("**********")
for index in board:
    print(index)
    
temp = [[0.0 for h in range(24)] for d in range(24)]        
for index in temp:
    print(index)


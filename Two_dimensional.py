# board = []
# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)
# # print(board)    
# for index in board:
#     print(index)
# print(len(board))

# print(board[0][0])

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



board = [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
h = 0
w = 1
color = board[h][w]
dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0
for i in range(4):
    nh, nw = h + dij[i][0], w + dij[i][1]
    if 0 <= nh < len(board) and 0 <= nw < len(board[0]) and board[nh][nw] == color:
        answer += 1

print(answer)




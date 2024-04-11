n, m, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        arr[i][j].append(li[j])

player = dict()
gun = dict()
coor = [0] * (m+1)
for j in range(1, m+1):
    x, y, d, s = map(int, input().split())
    player[j] = [(x-1, y-1), d, s]
    coor[j] = (x-1, y-1)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

point = [0] * (m+1)


def choice(num, i, j):    #내가 가진 총과 바닥에 있는 총 중에 고르기
    can = []
    if num in gun:
        can.append(gun[num])
    for g in arr[i][j]:
        can.append(g)

    lc = len(can)
    mx, idx = 0, lc
    for k in range(lc):
        if can[k] >= mx:
            mx = can[k]
            idx = k

    if lc > 1:
        can.pop(idx)
        arr[i][j] = can
    else:
        arr[i][j] = [0]

    gun[num] = mx


def fight(player1, player2, i, j, d1, d2):

    p1 = player[player1][2]
    if player1 in gun:
        p1 += gun[player1]

    p2 = player[player2][2]
    if player2 in gun:
        p2 += gun[player2]

    (winner, looser, d) = (player1, player2, d2) if p1 > p2 else (player2, player1, d1)

    diff = abs(p1 - p2)
    point[winner] += diff
    choice(winner, i, j)
    player[winner][0] = (i, j)
    coor[winner] = (i, j)

    #진사람 총 내려놓기
    if looser in gun:
        arr[i][j].append(gun[looser])
    #90도 돌려가면서
    for k in range(4):
        ni, nj = i+di[(d+k)%4], j+dj[(d+k)%4]
        if ni < 0 or ni >= n or nj <0 or nj >= n or (ni, nj) in coor:  continue

        choice(looser, ni, nj)
        player[looser][0] = (ni, nj)
        coor[looser] = (ni, nj)
        break


for _ in range(k):
    # 1-1플레이어마다 한 칸 움직일 수 있음 / 막히면 반대방향 1만큼
    for num in range(1, m+1):
        (ci, cj), d, hp = player[num]
        ni, nj = ci + di[d], cj + dj[d]
        if 0<=ni<n and 0<=nj<n:
            pass
        else:
            ni, nj = ci - di[d], cj - dj[d]

        if arr[ni][nj] == 0:
            player[num][0] = (ni, nj)
            coor[num] = (ni, nj)
            continue
        # 다른 플레이어가 있는지? -> 싸움
        for idx in player:
            pi, pj = player[idx][0]
            if (ni, nj) == (pi, pj):
                #싸워라
                fight(num, idx, ni, nj, d, player[idx][1])
        # 다른 플레이어가 없다면? -> 총 획득/내려놓기
        else:
            choice(num, ni, nj)

            player[num][0] = (ni, nj)
            coor[num] = (ni, nj)

    print(point)

print(*point[1:])
from collections import deque
L, N, Q = map(int, input().split())
board = [[2]*(L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2]*(L+2)]
knight = {}
# v = [[0]*(L+2) for _ in range(L+2)]
init = [0]*(N+1)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for m in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    knight[m] = [r, c, h, w, k]
    init[m] = k

    # for i in range(r, r+h):
    #     v[i][c:c+w] = [m]*w

def knight_push(idx, dr):
    q = []
    k_set = set()
    damage = [0]*(N+1)

    q.append(idx)
    k_set.add(idx)

    while q:
        s = q.pop(0)
        si, sj, h, w, k = knight[s]

        ni = si + di[dr]
        nj = sj + dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if board[i][j] == 2:
                    return
                if board[i][j] == 1:
                    damage[s] += 1

        for u in knight:
            if u in k_set: continue

            ti, tj, th, tw, tk = knight[u]
            if ni+h-1>=ti and ni<=ti+th-1 and tj<=nj+w-1 and nj<=tj+tw-1:
                q.append(u)
                k_set.add(u)


    damage[idx] = 0

    # for x in k_set:
    #     xi, xj, xh, xw, xk = knight[x]
    #     for i in range(xi, xi+xh):
    #         v[i][xj:xj+xw] = [0]*xw

    for x in k_set:
        xi, xj, xh, xw, xk = knight[x]
        if xk <= damage[x]:
            knight.pop(x)
        else:
            ni, nj = xi+di[dr], xj+dj[dr]
            nk = xk-damage[x]
            knight[x] = [ni, nj, xh, xw, nk]

            # for i in range(ni, ni+xh):
            #     v[i][nj:nj + xw] = [x] * xw


for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in knight:
        knight_push(idx, dr)


answer = 0
for i in knight:
    answer += init[i] - knight[i][4]

print(answer)

from collections import deque
L, N, Q = map(int, input().split())
arr = [[2] * (L + 2)] +[[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2] * (L + 2)]
knight = dict()
init = [0] * (N+1)
alive = [0] * (N+1)
for n in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    knight[n] = [r, c, h, w, k]
    init[n] = k
    alive[n] = 1


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def after(damage, q_set, d):

    for idx in q_set:
        s, r, h, w, k = knight[idx]
        knight[idx] = [s+di[d], r+dj[d], h, w, k-damage[idx]]
        if damage[idx] >= k:
            alive[idx] = 0


def bfs(n, d):
    q = deque()
    q_set = set()
    damage = [0]*(N+1)

    q.append(n)
    q_set.add(n)

    while q:
        idx = q.popleft()
        r, c, h, w, k = knight[idx]


        for i in range(r, r+h):
            for j in range(c, c+w):
                ni, nj = i+di[d], j+dj[d]
                if arr[ni][nj] == 2:
                    return False
                if arr[ni][nj] == 1:
                    damage[idx] += 1


                for x in knight:
                    if alive[x] ==0 or x in q_set:  continue
                    xr, xc, xh, xw, xk = knight[x]
                    if xr <= ni < xr + xh and xc <= nj < xc + xw:
                        q.append(x)
                        q_set.add(x)

    damage[n] = 0
    after(damage, q_set, d)


for _ in range(Q):
    if alive.count(0) == len(alive):
        print(0)
        break

    n, d = map(int, input().split())
    if alive[n] == 0:   continue
    bfs(n, d)

ans = 0
for i in range(1, N+1):
    if alive[i] == 0:   continue

    ans += init[i] - knight[i][4]

print(ans)

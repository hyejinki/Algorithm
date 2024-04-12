from collections import deque

N, M, H, K = map(int, input().split())
tree = [[0]*N for _ in range(N)]
runner = dict()
alive = [0] * (M+1)
for m in range(1, M+1):
    x, y, d = map(int, input().split())
    runner[m] = [(x-1, y-1), d]
    alive[m] = 1

for h in range(H):
    x, y = map(int, input().split())
    tree[x-1][y-1] = 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

map = [[0] * N for _ in range(N)]

def find(i, j, d):

    q = deque()
    q.append((i, j))
    cnt = 0
    for _ in range(3):
        ci, cj = q.popleft()
        if 0<= ci<N and 0<=cj<N and tree[ci][cj] == 0:        #잡았다 요놈
            for idx in runner:
                if alive[idx] == 0:     continue
                (pi, pj) = runner[idx][0]
                if (pi, pj) == (ci, cj):
                    cnt += 1
                    alive[idx] = 0

        q.append((ci + di[d], cj + dj[d]))

    return cnt



mx_cnt, cnt, flag, val  = 1, 0, 0, 1
ti, tj = N//2, N//2
d = 0

dri = [0, 0, 1]
drj = [0, 1, 0]
x, y = (N//2, N//2)
ans = 0
for k in range(1, K+1):

    for idx in runner:
        if alive[idx] == 0:     continue
        [(ci, cj), dd] = runner[idx]
        if abs(x-ci) + abs(y-cj) <= 3:
            nci, ncj = ci + dri[dd], cj + drj[dd]
            if (nci, ncj) == (x, y):
                continue
            elif 0 > nci or nci >=N or ncj < 0 or ncj >= N:
                nci, ncj = ci - dri[dd], cj - drj[dd]
            runner[idx][0] = (nci, ncj)

    # 술래
    cnt += 1
    ni, nj = ti + di[d], tj + dj[d]
    if 0<=ni<N and 0<=nj<N:
        map[ti][tj] = k
        ti, tj = ni, nj
        if (ti, tj) == (0, 0):
            mx_cnt, cnt, flag, val = N, 1, 1, -1
            d = 2
        elif (ti, tj) == (N//2, N//2):
            mx_cnt, cnt, flag, val = 1, 0, 0, 1
            d = 0

    if mx_cnt == cnt:
        d = (d+val)%4
        cnt = 0
        if flag == 0:
            flag = 1

        else:
            flag = 0
            mx_cnt += val

    point = find(ti, tj, d)
    ans += point*k

print(ans)

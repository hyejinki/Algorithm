from collections import deque
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
attack = [[0]*M for _ in range(N)]


def repair(qset):
    for i in range(N):
        for j in range(M):
            if (i, j) not in qset and arr[i][j] != 0:
                arr[i][j] += 1


def bfs(si, sj, ei, ej, p):

    flag = 0
    q = deque()
    v = [[[] for _ in range(M)] for _ in range(N)]
    q_set = set()

    q.append((si, sj))
    v[si][sj] = (si, sj)
    q_set.add((si, sj))
    q_set.add((ei, ej))

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            flag = 1
            arr[ci][cj] = max(0, arr[ci][cj] - p)
            while True:
                ci, cj = v[ci][cj]
                if (ci, cj) == (si, sj):
                    repair(q_set)
                    return True
                q_set.add((ci, cj))
                arr[ci][cj] = max(0, arr[ci][cj] - p//2)

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = (ci + di)%N, (cj + dj)%M
            if arr[ni][nj] != 0 and len(v[ni][nj]) == 0:
                q.append((ni, nj))
                v[ni][nj] = (ci, cj)


    if flag == 0:
        return False



def bomb(si, sj, ei, ej, p):

    q_set = set()
    q_set.add((si, sj))
    q_set.add((ei, ej))
    arr[ei][ej] = max(0, arr[ei][ej] - p)

    for di, dj in ((-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)):
        ni, nj = (ei+di) % N, (ej+dj) % M
        if arr[ni][nj] != 0 and (ni, nj) != (si, sj):
            q_set.add((ni, nj))
            arr[ni][nj] = max(0, arr[ni][nj] - p//2)

    repair(q_set)


for turn in range(1, K+1): #턴 수 챙겨야함


    # 공격자 선정
    minV = 5001
    mi, mj = [0, 0]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                if arr[i][j] < minV or (arr[i][j] == minV and attack[i][j] > attack[mi][mj]) or \
                        (arr[i][j] == minV and attack[i][j] == attack[mi][mj] and (i+j) > (mi+mj)) or \
                        (arr[i][j] == minV and attack[i][j] == attack[mi][mj] and (i+j) == (mi+mj) and j > mj):
                    minV = arr[i][j]
                    mi, mj = i, j


    # 공격대상자
    maxV = 0
    mxi, mxj = [0, 0]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                if arr[i][j] > maxV or (arr[i][j] == maxV and attack[i][j] < attack[mxi][mxj]) or \
                        (arr[i][j] == maxV and attack[i][j] == attack[mxi][mxj] and (i + j) < (mxi + mxj)) or \
                        (arr[i][j] == maxV and attack[i][j] == attack[mxi][mxj] and (i + j) == (mxi + mxj) and j < mxj):
                    maxV = arr[i][j]
                    mxi, mxj = i, j

    arr[mi][mj] += N + M
    if bfs(mi, mj, mxi, mxj, arr[mi][mj]) == False: #레이저
        bomb(mi, mj, mxi, mxj, arr[mi][mj])

    attack[mi][mj] = turn

    cnt = N * M
    for row in arr:
        cnt -= row.count(0)

    if cnt == 1:
        break


print(max(max(x) for x in arr))


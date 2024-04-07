from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
attack_arr = [[0] * M for _ in range(N)]


def bfs(si, sj, ei, ej):
    q = deque()
    visited = [[[] for _ in range(M)] for _ in range(N)]
    visited[si][sj] = (si, sj)
    q.append((si, sj))
    d = arr[si][sj]

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            arr[ei][ej] = max(0, arr[ci][cj]-d)
            while True:
                ci, cj = visited[ci][cj]
                if (ci, cj) == (si, sj):
                    return True
                arr[ci][cj] = max(0, arr[ci][cj]-d//2)
                f_set.add((ci, cj))

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = (ci + di) % N, (cj + dj) % M
            if len(visited[ni][nj]) == 0 and arr[ni][nj] > 0:
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)

    return False


def bomb(si, sj, ei, ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0, arr[ei][ej] - d)
    for di, dj in ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)):
        ni, nj = (ei+di)%N, (ej+dj)%M
        if (ni, nj) != (si, sj):
            arr[ni][nj] = max(0, arr[ni][nj] - d//2)
            f_set.add((ni, nj))


for T in range(1, K+1):
    minV, mx_attack, si, sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0: continue
            if arr[i][j] < minV or (arr[i][j] == minV and attack_arr[i][j] > mx_attack) or\
                (arr[i][j] == minV and attack_arr[i][j] == mx_attack and i+j>si+sj) or \
                (arr[i][j] == minV and attack_arr[i][j] == mx_attack and i+j==si+sj and j>sj):
                minV, mx_attack, si, sj = arr[i][j], attack_arr[i][j], i, j

    maxV, mn_attack, ei, ej = 0, T, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0: continue
            if arr[i][j] > maxV or (arr[i][j] == maxV and attack_arr[i][j] < mn_attack) or\
            (arr[i][j] == maxV and attack_arr[i][j] == mn_attack and i+j<ei+ej) or \
            (arr[i][j] == maxV and attack_arr[i][j] == mn_attack and i+j==ei+ej and j<ej):
                maxV, mn_attack, ei, ej = arr[i][j], attack_arr[i][j], i, j

    #레이저 공격
    arr[si][sj] += (M+N)
    attack_arr[si][sj] = T
    f_set = set()
    f_set.add((si, sj))
    f_set.add((ei, ej))

    if bfs(si, sj, ei, ej) == False:
    #포탄 공격
        bomb(si, sj, ei, ej)


    #포탑 정비
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and (i, j) not in f_set:
                arr[i][j] += 1

    # 종료
    cnt = N*M
    for row in arr:
        cnt -=row.count(0)
    if cnt<= 1:
        break


print(max(max(row) for row in arr))


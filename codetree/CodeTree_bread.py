from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
p = [0] * (m+1)
inside = [0] * (m+1)
cur = [[] for _ in range(m+1)]
for i in range(1, m+1):
    r, c = list(map(lambda x:int(x)-1, input().split()))
    arr[r][c] = -i
    p[i] = [r, c]
    inside[i] = 1

basecamp = set()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            basecamp.add((i, j))

def bfs(si, sj, dset):
    q = deque()
    visited = [[[] for _ in range(n)] for _ in range(n)]
    q.append([si, sj])
    visited[si][sj] = (si, sj)
    while q:
        ci, cj = q.popleft()
        if (ci, cj) in dset:
            li = [(ci, cj)]
            while True:
                ci, cj = visited[ci][cj]
                if (ci, cj) != (si, sj):
                    li.append((ci, cj))
                else:
                    return li[-1]

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and len(visited[ni][nj]) == 0 and arr[ni][nj] > -31:       # 범위 내, 방문 안 한 곳, 갈 수 있는 곳
                q.append([ni, nj])
                visited[ni][nj] = [ci, cj]

T = 0
while True:
    if inside.count(1) == 0:
        break
    T += 1
    for t in range(1, m+1):           # 1. 격자 내 이동
        if t < T:
            if inside[t] == 0:  continue
            ei, ej = p[t]
            si, sj = cur[t]

            ci, cj = bfs(si, sj, set(ei, ej))
            cur[t] = [ci, cj]         # 이동

    # 금지 구역 일괄 처리

    for i in range(1, m+1):
        if inside[i] == 0:  continue
        if len(cur[i]) == 0:    continue
        si, sj = cur[i]
        if arr[si][sj] == 1: # 베이스캠프
            arr[si][sj] = -31
        elif arr[si][sj] == -i:
            arr[si][sj] = -31
            inside[i] = 0

    # 2. T번 베이스 캠프 가기
    if T <= m:
        si, sj = p[T]
        minv = 2*n + 1
        mn = []
        bfs(si, sj, basecamp)

        if len(mn) == 0:    continue
        mi, mj = mn[-1]     # 가장 가까운 베캠
        cur[T] = [mi, mj]
        arr[mi][mj] = -31

print(T)


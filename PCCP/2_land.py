land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]
raw = len(land)
col = len(land[0])
visited = [[[0, 0, 0]] * col for _ in range(raw)]  #[이미 방문한, 같은 덩어리, 사이즈]
need_visit = []
cnt = 0  # 같은 덩어리인지 판별

for i in range(raw):
    for j in range(col):
        size = 0  # 크기 측정
        if not need_visit:  # 처음 시작
            if land[i][j] == 1 and visited[i][j][0] == 0:  # 1이고 방문하지 않았으면
                need_visit.append((i, j))
                cnt += 1
                size += 1
                visited[i][j] = [1, cnt, size]

        else:
            while need_visit:
                ci, cj = need_visit.pop()
                for k in range(4):
                    ni, nj = ci + dij[k][0], cj + dij[k][1]
                    if (0 <= ni < raw) and (0 <= nj < col) and land[ni][nj] == 1 and visited[ni][nj][0] == 0:
                        need_visit.append((ni, nj))
                        visited[ni][nj] = visited[ci][cj]
                        visited[ni][nj][2] += 1  # 크기 바로 갱신
            # visited[i][j][2] = size   # 얕은 복사로 크기 갱신

answer = 0
for j in range(col):
    total = 0
    check = []
    for i in range(raw):
        if visited[i][j][0] == 1 and visited[i][j][1] not in check:
            check.append(visited[i][j][1])
            total += visited[i][j][2]
    if answer < total:
        answer = total

print(answer)
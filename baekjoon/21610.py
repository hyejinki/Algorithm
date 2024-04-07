N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

# 8개 방향
eight_ij = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 4개 방향
four_ij = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

answer = 0

for d, s in move:
    moved_cloud = []
    for i, j in cloud:
        ni = (i + eight_ij[d][0] * s) % N
        nj = (j + eight_ij[d][1] * s) % N
        arr[ni][nj] += 1
        moved_cloud.append((ni, nj))

#         구름 비내리기, 사라져

    for i, j in moved_cloud:
        cnt = 0
        for k in range(4):
            ni = i + four_ij[k][0]
            nj = j + four_ij[k][1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                cnt += 1
        arr[i][j] += cnt

#     구름이 있던 칸 제외 / 2개 이상 구름 /물의 양-= 2
    cloud = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in moved_cloud and arr[i][j] >= 2:
                arr[i][j] -= 2
                cloud.append((i, j))

answer = sum(sum(row) for row in arr)
print(answer)






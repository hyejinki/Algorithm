from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
M = n//2

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    groups[-1].add((i, j))

    while q:
        ci, cj = q.popleft()
        for (ni, nj) in ((ci - 1, cj), (ci, cj+1), (ci+1, cj), (ci, cj-1)):
            if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0 and arr[ni][nj] == arr[ci][cj]:
                q.append((ni, nj))
                groups[-1].add((ni, nj))
                visited[ni][nj] = 1


def cal(i, j):
    cnt = 0
    for ci, cj in groups[i]:
        for (ni, nj) in ((ci - 1, cj), (ci, cj+1), (ci+1, cj), (ci, cj-1)):
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) in groups[j]:
                cnt += 1

    return (len(groups[i]) + len(groups[j])) * nums[i] * nums[j] * cnt


ans = 0
for _ in range(4):
    groups = []
    nums = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):      #그룹화
        for j in range(n):
            if visited[i][j] == 0:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i, j)

    # 예술성 계산
    score = 0
    l = len(nums)
    for i in range(l-1):
        for j in range(i+1, l):
            score += cal(i, j)
    ans += score

    # 회전1 : 십자
    narr = [x[:] for x in arr]
    for i in range(n):
        narr[i][M] = arr[M][n-i-1]
        narr[M][i] = arr[i][M]

    arr = narr
    # 회전2 : 4 구역
    narr = [x[:] for x in arr]
    for (si, sj) in ((0, 0), (0, M+1), (M+1, 0), (M+1, M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+M - j - 1][sj+ i]

    arr = narr

print(ans)

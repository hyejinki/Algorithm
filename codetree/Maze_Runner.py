N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
runner = []
for _ in range(1, M+1):
    r, c = map(lambda x:int(x)-1, input().split())
    arr[r][c] -= 1
ei, ej = map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11
ans = 0 #이동할 때마다 +1
cnt = M # 탈출 할 때마다 마이너스!


def find_eij():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j


def find_box():
    mn = N * N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                length = max(abs(ei - i), abs(ej - j))
                if mn > length:
                    mn = length

    for si in range(N - mn):
        for sj in range(N - mn):  # 가능한 모든 시작위치
            if si <= ei <= si + mn and sj <= ej <= sj + mn:  # 비상구가 포함된 사각형!
                for i in range(si, si + mn + 1):
                    for j in range(sj, sj + mn + 1):
                        if -11 < arr[i][j] < 0:  # 사람인 경우 리턴!
                            return si, sj, mn+1



for k in range(K):
    # 참가자 이동 -> 거리가 짧아져야 이동(아니면 가만히) / 이동하면 arr,runner좌표 바꾸고 ans++ / 탈출하면 cnt-- , arr,runner에서 지우기 /  상하 우선 / 참가자 겹치면 -1
    narr = [x[:] for x in arr]
    for si in range(N):
        for sj in range(N):
            if -11 < arr[si][sj] < 0:
                diff = abs(ei-si) + abs(sj-ej)
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ni, nj = si + di, sj + dj
                    ndiff = abs(ei-ni) + abs(ej-nj)
                    if 0<=ni<N and 0<=nj<N and diff > ndiff and (arr[ni][nj] < 1):
                        ans -= arr[si][sj]
                        narr[si][sj] -= arr[si][sj]
                        # 탈출구라면?
                        if arr[ni][nj] == -11:
                            cnt += arr[si][sj]
                            break
                        # 이동하기
                        narr[ni][nj] += arr[si][sj]
                        break
    arr = narr
    if cnt == 0:
        break

    # 미로 회전 -> 0,0에 가까운 가장 작은 정사각형 / 시계방향 90도 / 회전하면 모든 벽 내구도-- / runner 좌표 바꾸고 / ei, ej 좌표 바꾸고
    si, sj, mn = find_box()
    narr = [x[:] for x in arr]
    for i in range(mn):
        for j in range(mn):
            narr[si + i][sj + j] = arr[si + mn - j - 1][sj + i]
            if 0 < arr[si+mn-j-1][sj+i] < 10:
                narr[si + i][sj + j] -= 1

    arr = narr
    ei, ej = find_eij()


print(ans)
print(ei+1, ej+1)

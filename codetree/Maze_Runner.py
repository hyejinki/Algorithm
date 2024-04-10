N, M, K = map(int, input().split())
arr=[list(map(int, input().split()))for _ in range(N)]
for _ in range(M):
    r, c = map(lambda x:int(x)-1, input().split())
    arr[r][c] = -1              # 사람은 -1

ei, ej = map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11               # 출구 -11


def find_box(arr):
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                mn = min(mn, max(abs(ei - i), abs(ej - j)))

    for i in range(N - mn):
        for j in range(N - mn):
            if i <= ei <= i + mn and j <= ej <= j + mn:
                for si in range(i, i+mn + 1):
                    for sj in range(j, j+mn + 1):
                        if -11 < arr[si][sj] < 0:
                            return i, j, mn + 1


def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j


answer = 0
cnt = M
for _ in range(K):      #턴

    # 1. 사람 이동
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0:
                dist = abs(ei - i) + abs(ej - j)
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ni, nj = i+di, j+dj
                    nd = abs(ei-ni) + abs(ej-nj)
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]<1 and dist > nd:
                        answer += arr[i][j]
                        narr[i][j] -= arr[i][j]
                        if arr[ni][nj] == -11:  #출구
                            cnt += arr[i][j]
                        else:
                            narr[ni][nj] += arr[i][j]
                        break

    arr = narr
    if cnt == 0:
        break

    # 2. 회전
    # 박스 크기 정하고 / 찾기
    si, sj, L = find_box(arr)

    # 회전하면 내구도 -1
    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[i+si][j+sj] = arr[L-j-1+si][i+sj]
            if 0<narr[i+si][j+sj]:
                narr[i+si][j+sj] -= 1


    arr = narr
    ei, ej = find_exit(arr)

print(-answer)
print(ei+1, ej+1)



N, M, P, C, D = map(int, input().split())
ri, rj = map(lambda x:int(x) - 1, input().split())
point = [0] * (P+1)
alive = [1] * (P+1)
alive[0] = 0
sleep = [1] * (P+1)
santa = [[N]*2 for _ in range(P+1)]
for _ in range(P):
    n, i, j = map(int, input().split())
    santa[n] = [i-1, j-1]


def push_santa(r1, c1, dr, dc, p, idx):
    # 만났어
    q = []
    q.append((r1, c1, dr, dc, p, idx))
    sleep[idx] = turn + 2

    while q:
        ci, cj, dr, dc, p, idx = q.pop(0)
        ni, nj = ci + dr*p, cj + dc*p
        index = idx
        if 0<=ni<N and 0<=nj<N and [ni, nj] in santa:
            for i in range(1, P+1):
                if alive[i] == 1 and santa[i] == [ni, nj]:
                    index = i
                    break
            q.append((ni, nj, dr, dc, 1, index))
            santa[idx] = [ni, nj]

        elif 0<=ni<N and 0<=nj<N:
            santa[idx] = [ni, nj]


        else:
            print(idx)
            alive[idx] = 0

for turn in range(1, M+1):
    if alive.count(1) == 0:
        break

    # 루돌푸 움직임
    minx = []
    minV = N*N*2
    for idx in range(1, P+1):
        if alive[idx]==0 : continue
        si, sj = santa[idx]
        dist = (ri - si)**2 + (rj - sj)**2
        if dist < minV:
            minx = [(si, sj, idx)]
            minV = dist
        elif dist == minV:
            minx.append((si, sj, idx))
    minx.sort(reverse=True)

    si, sj, mnidx = minx[0]

    # 방향
    di, dj = 0, 0
    if ri - si > 0:
        di = -1
    elif ri - si < 0:
        di = 1

    if rj - sj > 0:
        dj = -1
    elif rj - sj <0:
        dj = 1

    ni, nj = ri + di, rj + dj

    if (ni, nj) == (si, sj):
        point[mnidx] += C
        push_santa(ni, nj, di, dj,C, mnidx)

    else:
        ri, rj = ni, nj


    # 산타 움직임
    for idx in range(1, P+1):
        if alive[idx] == 0:    continue
        if sleep[idx] > turn:   continue
        si, sj = santa[idx]
        dist = (ri - si)**2 + (rj - sj)**2

        can = []
        for dsi, dsj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nsi, nsj = si + dsi, sj + dsj
            new_dist = (ri - nsi)**2 + (rj - nsj)**2
            if 0<=nsi<N and 0<=nsj<N and new_dist < dist and [nsi, nsj] not in santa:
                can.append([nsi, nsj, dsi, dsj])
                dist = new_dist

        if len(can) == 0:   continue
        sr, sc, dr, dc = can[-1]

        if (ri, rj) == (sr, sc):
            point[idx] += D
            push_santa(sr, sc, -dr, -dc, D, idx)
        else:
            santa[idx] = [sr, sc]

    for i in range(1, P+1):
        if alive[i] == 1:
            point[i] += 1

print(*point[1:])
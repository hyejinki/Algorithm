N, M, P, C, D = map(int, input().split())
ei, ej = map(lambda x:int(x)-1, input().split())
santa = [[] for _ in range(P)]
alive = [0] * (P)
sleep = [0] * (P)
point = [0] * (P)
for _ in range(P):
    pn, sr, sc = map(lambda x:int(x)-1, input().split())
    santa[pn] = [sr, sc]
    alive[pn] = 1
    sleep[pn] = -1


def push(ei, ej, di, dj, p, idx):   #점수, 튕기기, 상호작용, 탈락
    print(turn,"!!!!!!!!")
    q = [(ei, ej, p, idx)]

    while q:
        ci, cj, p, idx = q.pop(0)
        ni, nj = ci + di*p, cj + dj*p
        # 탈락
        if ni<0 or nj<0 or ni>=N or nj>=N:
            alive[idx] = 0
            return

        for i in range(P):
            if alive[i] != 0 and santa[i] == [ni, nj]:
                q.append((ni, nj, 1, i))
        else:
            santa[idx] = [ni, nj]
            return



for turn in range(1, M+1):
    if alive.count(0) == len(alive):
        break

    minV = 5001
    mi, mj = N, N
    idx = 31
    for i in range(P):
        if alive[i] == 0:   continue
        si, sj = santa[i]
        diff = (ei - si)**2 + (ej - sj)**2
        if minV > diff or (minV == diff and si > mi) or (minV==diff and si>mi and sj>mj):
            minV, mi, mj, idx = diff, si, sj, i

    di, dj = (0, 0)
    if ei>mi:
        di = -1
    elif ei<mi:
        di = 1
    if ej>mj:
        dj = -1
    elif ej<mj:
        dj = 1

    ei += di
    ej += dj

    if (ei, ej) == (di, dj):    # 잡았다 요놈
        sleep[idx] = turn
        push(ei, ej, di, dj,C, idx)
        point[idx] += C



    for i in range(P):      #기절 처리해야돼
        if alive[i] == 0:   continue
        if sleep[i] + 2 > turn: continue
        ci, cj = santa[i]
        mni, mnj = ci, cj
        ndi, ndj = 0, 0
        diff = (ei-ci)**2 + (ej-cj)**2
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            nd = (ei-ni)**2 + (ej-nj)**2
            if 0<=ni<N and 0<=nj<N and (ni, nj) not in santa and diff > nd:
                mni, mnj = ni, nj
                ndi, ndj = di, dj
                diff = nd

        if (mni, mnj) == (ei, ej):     #잡았다
            sleep[i] = turn
            point[idx] += D
            push(ei, ej, -ndi, -ndj, D, i)
        else:
            santa[i] = [mni, mnj]


    for s in range(P):
        if alive[s] == 0:   continue
        point[s] += 1

    print("turn", turn)
    print("point", point)
    print("alive", alive)
print(point)
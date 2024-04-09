N, M, P, C, D = map(int, input().split())
x, y = map(int, input().split())
ru = [x, y]
santa_dict = dict()

for _ in range(P):
    n, i, j = map(int, input().split())
    santa_dict[n] = [(i, j), -1, 1]
point = [0] * (P+1)


# 거리 구하기
def cal_distance(r1, c1, r2, c2):
    return (r1 - r2)**2 + (c1 - c2)**2


def comp(x, y):
    if x - y > 0:
        return -1
    elif x - y < 0:
        return 1
    else:
        return 0



def push(ci, cj, oi, oj):

     for k in santa_dict:
         if (ci, cj) == santa_dict[k][0]:
             if 1 <= ci + oi <= N and 1 <= cj + oj <= N:
                 santa_dict[k][0] = (ci + oi, cj + oj)
                 santa_dict[k][1] = turn
             else:
                 santa_dict[k][2] = 0


def move_ru(ri, rj, si, sj, C, idx):
    di, dj = comp(ri, si), comp(rj, sj)
    ni, nj = ri + di, rj + dj

    ru[0], ru[1] = ni, nj
    if (ni, nj) == (si, sj):
        # 점수
        point[idx] += C
        #밀기
        pi, pj = si + di*C, sj + dj*C
        if 1 <= pi <= N and 1<= pj<=N:
            santa_dict[idx][0] = (pi, pj)
            santa_dict[idx][1] = turn
        else:
            santa_dict[idx][2] = 0

        push(pi, pj, di, dj)




def move_santa(ri, rj, si, sj, D, idx):
    minx = cal_distance(ri, rj, si, sj)
    cij = (si, sj)
    ij = (0, 0)
    for (di, dj) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = si+di, sj + dj
        if 1<=ni<=N and 1<=nj<=N:
            for s in santa_dict:
                if santa_dict[s][0] == (ni, nj):
                    continue
                x = cal_distance(ri, rj, ni, nj)
                if x<minx:
                    minx = x
                    cij = (ni, nj)
                    ij = (di, dj)

    if cij == (ri, rj):
        # 점수
        point[idx] += D
        #밀기
        pi, pj = cij[0] - ij[0]*D, cij[1] - ij[1]*d

        if 1 <= pi <= N and 1<= pj<=N:
            santa_dict[idx][0] = (pi, pj)
            santa_dict[idx][1] = turn
        else:
            santa_dict[idx][2] = 0

        push(cij[0], cij[1], ij[0], ij[1])

        if santa_dict[idx]:
            santa_dict[idx][0] = (cij[0], cij[1])



for turn in range(1, M+1):
    flag = 0
    for idx in santa_dict:
        if santa_dict[idx][2] == 1:
            flag = 1
    if flag == 0:
        break

    ri, rj = ru[0], ru[1]
    minV = N*N*2
    mi, mj = N+1, N+1
    for idx in santa_dict:
        if santa_dict[idx][2] == 1:
            if turn - santa_dict[idx][1] >= 2:
                (si, sj) = santa_dict[idx][0]
                d = cal_distance(ri, rj, si, sj)
                if d < minV or (d == minV and (si, sj) > (mi, mj)):
                    minV, mi, mj, i = d, si, sj, idx

    move_ru(ri, rj, mi, mj, C, i) #루돌푸 움직임

    for idx in santa_dict:
        if santa_dict[idx][2] == 1:
            if turn - santa_dict[idx][1] >= 2:
                (si, sj) = santa_dict[idx][0]
                move_santa(ru[0], ru[1], si, sj, D, idx)


    for idx in santa_dict:
        if santa_dict[idx][2] == 1:
            point[idx] += 1

print(point)

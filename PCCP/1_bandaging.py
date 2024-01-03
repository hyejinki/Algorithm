bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]
cnt = 0
heart = health
for i in range(len(attacks)):
    add = 0
    # 회복
    diff = attacks[i][0] - cnt - 1  # 연속 회복 시간
    if diff >= bandage[0]:
        add = diff // bandage[0]
    diff = diff * bandage[1] + add * bandage[2]
    heart = heart + diff if health >= heart + diff else health

    # 공격
    heart = heart - attacks[i][1] if heart > attacks[i][1] else -1
    if heart == -1:
        break
    ## cnt 갱신
    cnt = attacks[i][0]

print(heart)
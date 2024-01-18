friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
split_gifts = [gift.split() for gift in gifts]  #공백 기준으로 쪼갬
maxValue = 0
# 선물 지수
gift_score = {}


def get_received(gift_li, score, target):
    count = 0
    for i in range(len(gift_li)):
        if (gift_li[i][1] > gift_li[i][2] or
                (gift_li[i][1] == gift_li[i][2] and score[target] > score[gift_li[i][0]])): # 보낸 게 더 많으면 ++
            count += 1
    return count


total_list = []
for i in range(len(friends)):
    receive = 0
    send = 0
    gift_list = [[name, 0, 0] for name in friends if name != friends[i]]
    for j in range(len(gifts)):
        if split_gifts[j][0] == friends[i]: #보낸 선물
            send += 1
            for friend in gift_list:    #누구에게 보낸 선물인가?
                if friend[0] == split_gifts[j][1]:
                    friend[1] += 1

        elif split_gifts[j][1] == friends[i]: #받은 선물
            receive += 1
            for friend in gift_list:    #누구에게 받은 선물인가?
                if friend[0] == split_gifts[j][0]:
                    friend[2] += 1

    gift_score[friends[i]] = send - receive
    total_list.append(gift_list)

for i in range(len(friends)):
    cnt = get_received(total_list[i], gift_score, friends[i])
    if maxValue < cnt:
        maxValue = cnt

print(maxValue)


targets = [[4, 5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
sorted_targets = sorted(targets, key=lambda x:x[1])      # 정렬하기
answer = 0
n = 0
for s, e in sorted_targets:
    if s >= n:          # 여기서 끊김 -> 새로운 미사일
        answer += 1
        n = e


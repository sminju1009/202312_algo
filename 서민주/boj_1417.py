'''
문제 링크: https://www.acmicpc.net/problem/1417
풀이 일자: 2023년 11월 28일
'''

n = int(input())
dasom = int(input())
vote = []
cnt = 0
for _ in range(n-1):
    vote.append(int(input()))
vote.sort(reverse=True)
if n==1:
    print(0)
else:
    while vote[0]>=dasom:
        dasom += 1
        vote[0] -= 1
        cnt += 1
        vote.sort(reverse=True)
    print(cnt)
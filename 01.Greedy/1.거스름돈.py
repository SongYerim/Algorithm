#그리디 알고리즘의 가장 대표적인 문제
#가장 큰 화폐 단위부터 돈을 거슬러 주기!!

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)
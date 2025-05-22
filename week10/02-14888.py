#연산자 끼워넣기 - 백트랙킹
n = int(input())
data = list(map(int, input().split())) #수열
add, sub, mul, div = map(int, input().split()) #연산자

min_value = 1e9 #최솟값 초기화
max_value = -1e9

def dfs(i, now):    
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)         
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1
dfs(1, data[0])

print(max_value)
print(min_value)



#n개 수로 이루어진 수열 / n-1개 연산자
#계산=앞에서부터 / 정수나눗셈// 사용
# 음수%양수 -> 양수%양수 후 몫을 음수로

# 중복순열 라이브러리 product 사용가능

n = int(input())
road = map(str, input().split())
x, y = 1, 1

#L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in road:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
    
#굳이 2차원 배열을 만들지 않아도 풀이가능
#4가지 상황에 대한 이동을 배열로 만들어 저장해놓고 대입만 해주기
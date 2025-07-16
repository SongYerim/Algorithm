n = input()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    #해당 위치로 이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
        result += 1
        
print(result)
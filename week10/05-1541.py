# 잃어버린 괄호 - 그리디
# import sys
# input = sys.stdin.readline

list = input().split('-')
num = []
for i in list:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)

#홀수자리는 숫자 - 짝수자리는 문자
#뒤에서 큰수로 빼야 최솟값이 됨
#-를 기준으로 split -> split후 +가 남음
#+연산 진행해서 배열에 넣어줌
#순서대로 - 진행
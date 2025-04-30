# 28278-스택2-자료구조
import sys

stack = []     
N = int(input())
for i in range(N):
    n = list(map(int, sys.stdin.readline().split())) #
    if n[0] == 1: #스택 추가
        stack.append(n[1])
    elif n[0] == 2: #맨위 정수 빼고 출력, 없으면 -1
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif n[0] == 3: #스택의 정수 개수
        print(len(stack))
    elif n[0] == 4: #비어있음1, 아님 0
        if stack:
            print(0)
        else:
            print(1)
    else: #맨위 정수 출력, 없으면 -1
        if stack:
            print(stack[-1])
        else:
            print(-1)
            
#TypeError: 
# sys.stdin.readline().split() 은 문자열을 공백 기준으로 나눈 리스트를 반환
# int(...) 는 리스트를 인자로 받을 수 없음, 문자열 하나만 받아야함함
#4949 균형잡힌 세상 - 자료구조
#주어진 문자열의 괄호 균형이 잘 맞춰져 있는지 판단
#종료조건: . 하나
#스택에 넣어서 pop하며 체크
#마지막에 스택이 비어있으면 yes 아니면 no

while(True):
    x = input()
    if(x == "."):
        break
    stack = []
    
    for i in x:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else: #비어있거나 짝 맞지X 경우에는 추가
                stack.append(x)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(x)
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
#12789 도키도키 간식드리미 - 자료구조 스택
# n = input()
# num = list(map(int, input().split()))
# stack = []

# max = 1
# for i in range(len(num)):
#     if num[i] == max:
#         max += 1
#         continue
#     else:
#         stack.append(num[i])

# for i in range(len(stack)):
#     if stack[-1] == max:
#         max += 1
#         stack.pop()
#     else:
#         break
    
# if len(stack) == 0:
#     print("Nice")
# else:
#     print("Sad")
        
n = input()
num = list(map(int, input().split()))
stack = []

max = 1
for i in num:
    stack.append(i)
    while stack and stack[-1] == max: #스택에 비어있지 않으면 마지막 요소와 비교
        stack.pop()
        max += 1        
    
if stack:
    print("Sad")
else:
    print("Nice")
        
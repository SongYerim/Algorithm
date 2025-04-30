# 10773-제로-자료구조

stack = []
K = int(input())
for i in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
        
print(sum(stack))
from collections import deque

for _ in range(int(input())):
    s = input().strip()
    stack = deque()
    for i in s:
        if len(s)%2 or s[0]==')' or s[-1]=='(':
            stack.append(')')
            break
        # print(stack, i)
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack)==0:
                stack.append(')')
                break
            stack.pop()
        else:
            if len(stack)==0:
                stack.append('(')
            else:
                stack.pop()
    # print(stack)
    if len(stack)==0:
        print("YES")
    else:
        print('NO')

import sys

for line in sys.stdin:
    line = line.strip()
    stack = []
    n=len(line)
    list=[' ']*n
    for i in range(n):
        if line[i]== '(':
            stack.append(i)
        elif line[i]==')':
            if stack:
                stack.pop()
            else:
                list[i]='?'
    while(stack):
        top_element = stack.pop()
        list[top_element]='x'
    print(line)
    print(''.join(list))
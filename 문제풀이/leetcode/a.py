path = "/a/./b/../../c/"
a = path.split('/')
level = 0
stack = []

print(a)
print('--------------------')
for i in a:
    if i != '' and i not in ['.','..']:
      level +=1
      stack.append('/'+ i)
    if i == '..':
        level -= 1
        if len(stack) != 0:
            stack.pop(0)

if len(stack) == 0:
    stack.append('/')

print(''.join(stack))   
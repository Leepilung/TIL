new_id = "=.="
answer = ''
step2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','0','-','_','.']
#step 1
new_id = new_id.lower()
print(new_id)

#setp 2
for i in new_id:
    if i in step2:
        answer += i
new_id = answer
print('step2',answer)

#step 3
while '..' in answer:
    answer = answer.replace('..','.')
print('step3',answer)

#step 4
if answer[0] == '.':
    if len(answer) > 1:
        answer = answer[1:]
    else:
        '.'
if answer[-1] == '.':
    answer = answer[:-1]
print('step4',answer)

#step 5
if len(answer) == 0:
    answer = answer + 'a'
print('step5',answer)
#step 6 
if len(answer) >= 16:
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
print('setp6',answer)
#step 7
if len(answer) <= 2:
    while len(answer) < 3:
        answer = answer + answer[-1]
print('step7',answer)

print('-----')
print(answer)
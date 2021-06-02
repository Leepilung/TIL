letter = {
    '2' : ['a','b','c'],
    '3' : ['d','e','f'],
    '4' : ['g','h','i'],
    '5' : ['j','k','l'],
    '6' : ['m','n','o'],
    '7' : ['p','q','r','s'],
    '8' : ['t','u','v'],
    '9' : ['w','x','y','z']
}

print(letter['2'][0])

print(len(letter['2']))

string = '23'

for i in string:
    lst = letter[string]
    result = []
    for j in lst:
        for m in lst:
            result.append(j+m)
            print(result)
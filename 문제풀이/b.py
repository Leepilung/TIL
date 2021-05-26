for i in range(7):
    for j in range(8):
        print(f'{i}  ',end ='')
        print(f'{j}  ',end = '')
        if j == 7:
            print()

print('-----------------------------------------------')

weight = 10
bridge_lenth = 2
truck_weights = [7,4,5,6]
total = 0
bridge= [0]*bridge_lenth

temp2 = truck_weights.pop(0)
print(temp2)
total += temp2
print(total)
bridge.append(truck_weights.pop(0))
print(bridge)
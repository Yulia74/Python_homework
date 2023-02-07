"""
    Задача №15: Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий
и самый тяжелый арбуз? Помогите ему!
     Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.

Input: 5 -> 5 1 6 5 9

Output: 1 9
"""

watermelon = int(input('Введите количество арбузов: '))
max, min = 0, 999
for i in range(watermelon):
    weight = int(input())
    if weight > max:
        max = weight
    if weight < min:
        min = weight
print(f'Самый тяжелый арбуз весит {max} кг')
print(f'Самый легкий арбуз весит {min} кг')

'''
2-ой вариант решения (через список для веса арбузов)
count = int(input('Введите количество арбузов: '))
weqgth = []

for i in range(count):
    weight.append(int(input('Введите вес выбранного арбуза: ')))

weight_min = weight[0]
weight_max = weight[1]

for i in range(len(weight)):
    if weight[i] > weight_max:
        weight_max = weight[i]
    elif weight[i] < weight_min:
            weight_min = weight[i]

print(weight_min)
print(weight_max)
'''

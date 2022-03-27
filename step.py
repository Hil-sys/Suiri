#for i in range(0,10):
     # print('Я программист' + ' ' + str(i), sep='', end=' ')
# bollean = True
# print('Tyt` ' + str(2))

# list = [5, 2, 1, 'qq', 1.5, [1, 'q']]
# list2 = [1, 1, 100, 50]
# list[0] = 50
# list[3] = 'ne qq'
#
# list.insert(0, 2)
#
# list.extend([1, 5, 'sii'])
#
# list2.sort()
#
# list2.reverse()
#
# list2.pop(1)
#
# x = list2.count(1)
#
# list2.remove(100)
#
# print(list[-1][-1])
# print(list)
# print(list2)
# print(x)

# list3 = [1, 2, '40', False]
#
# for i in list3:
#     i *= 2
#     print(i)

# s = int(input('long S: '))
#
# i = 0
# s1 = []
# while i < s:
#     s1.append(input())
#     i += 1
# print(s1)

# word = 'go, to, rush'
# # print(word.count('o'))
# print(word.isupper()) # bool
# # print(word.upper())
# # print(word.lower())
# # print(word.capitalize()) # s big bukvii
# # print(word.find('or'))
# words = word.split(', ')
# print(words[1])
#
# for i in range(len(words)):
#     words[i] = words[i].capitalize()
#
# res = ', '.join(words)
#
# print(res)
#
# word1 = 'gotorush'
#
# print(word1[5:8:2])
#
# print(word1.find('t'))
#
# list3 = [1, 2 , 'sdda', 24]
# print(list3[1:3])

# cor = (1, 2, 'jj', 51, 21, 103) # кортеж = cor = 1, 2, 'TR'
# print(cor[:4])

# print(cor.count(1))
# print(len(cor))

# cor = (1, 2, 'jj', 51, 21, 103)
#
# for i in cor:
#     print(i)
#
# s = [5, 10, 6]
# ncor = tuple(s)
# word4 = tuple('gonorush')
# print(ncor)
# print(word4)

# slovar = {(5, 6):4}
# print(slovar[(5, 6)])
#
# slovar2 = {'st': 'RU', 'name':'Russian', 'popula':144000000}
# print(slovar2['popula'])
#
# slovar3 = dict(code='RU', name='Russian', populat=21)
# print(slovar3['code'])
# print(slovar2)
#
# print(slovar2.items())
# # slovar2.pop('name')
# # slovar2.popitem()
# slovar2['st'] = 'UA'
# for i, val in slovar2.items():
#     print(i, ' ', val)
#
# print(slovar2.get('st'))
#
# print(slovar2.keys())
# print(slovar2.values())
#
# polz = {
#     'user1':{
#         'first_name':'Slava',
#         'last_name':'ST',
#         'age':15,
#         'addres':['г. Нижний Новгород', 'ул. Аркадия Гайдара', 'д.26'],
#         'grades':{'math':5, 'ruslan':4}
#     },
#     'user2':{
#         'first_name':'qq'
#     }
# }
# print(polz['user1']['first_name'], polz['user1']['last_name'])
# print(polz['user2']['first_name'])

# mnoz = set('gggyes')
# print(mnoz)
#
# mnoz2 = {1, 2, 10, 25, 2}
# mnoz2.add(24)
# mnoz2.update([1, 25, 100, 'qq'])
# mnoz2.remove('qq')
# mnoz2.pop()
# print(mnoz2)
#
# s3 = [1, 5, 2, 5, 100]
# s3 = set(s3)
#
# x = frozenset([1, 2, 5, 5, 100, 24, 100, 3])
# print(x)
# print(s3)

# def func():
#     print('hi', end='')
#     print('!')
# func()
# func()
# func()

# def func1(a):
#     print(a,end='')
#     print('!')
# func1('hi')
# func1(5)

# def func2(a1,b1):
#     return a1 + b1
# sum = func2(2, 9)
# print(sum)
# print(func2('HII','!'))

# s4 = [1, 5, 6, 70, 10]
# print(min(s4))
#
# func3 = lambda x2, y2: x2 ** y2
# res4 = func3(2, 3)
# print(res4)

# апогея начальной теории
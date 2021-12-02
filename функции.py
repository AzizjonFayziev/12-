# v1 = 100 
# v2 = 70
# t = 2
# s = (v1 + v2) * t
# print(s)

# v3 = 60
# v4 = 90
# t2 = 3 

# s2 = (v3 + v4) * t2
# print(s2)

# def calculateDistance(v1, v2, t):
#     return (v1 + v2 ) * t 
# d = calculateDistance(70, 10, 2)
# print(d)
# print(calculateDistance(70, 10, 2))

# vel1 = int(input('Enter vel1:'))
# vel2 = int(input('Enter vel2:'))
# time = int(input('Enter time:'))
# print(calculateDistance(vel1, vel2, time))



# def calculateSquare(x):
#     return (x * x)
# print(calculateSquare(50))

# def calcPower(base, exp):
#     return base ** exp

# print(calcPower(3, 4))

# def reverseList(list):
#     return list[::-1]
# print(reverseList([1, 2 , 3]))

# def calculate(x ):
#     return (x ** -1)
# print(calculate(5))

# def calculate (x, y):
#     return (x + y)
# print(calculate(5,4))

from typing import AsyncContextManager


# def calculate (x, y, *c):
#     acc = 0
#     for num in c:
#         acc+= num
#     return x + y + acc
        
# print(calculate(3,4,5,6,7 ))


# mentor = {
#     'name': 'Elbek',
#     'surname':  'Khakimbekov',
#     'age': 22,
#     'isMarried': False
# }
# print(mentor['age'])

# mentor = {
#     'name': 'Elbek',
#     'surname':  'Khakimbekov',
#     'age': 22,
#     'isMarried': False
# }
# for key in mentor:
#     print(key, mentor[key])


# def abc(**args):
#     acc = 0
#     for key in args:
#         acc+= args[key]
#     return acc
# print(abc(a = 4, b = 6, c = 10))

# def min(a, b):
#     if a < b: return a
#     elif a == b: return'Equal'
#     else: return b
    
# print(min(50,20))
# print(min(50,50))


# print(eval('1+2'))

def calculator(a, b, action):
    if action == 'add': return eval(f'{a}-{b}')
    elif action == 'add': return eval(f'{a}-{b})
print(calculator('1', '3', 'plus'))

print(calculator('10', '6', 'subtract'))
print(calculator('10', '6', 'multiply'))
print(calculator('10', '6', 'divide'))





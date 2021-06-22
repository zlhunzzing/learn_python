# # 수
# print(5)
# print(10)
# print(3.14)

# # 문자열
# print("ㅋ" * 10)

# # 참거짓 불린
# print(True)
# print(False)
# print(not True)

# # 변수
# animal = "뽀삐"
# name = "뽀미"
# age = 1
# is_adult = age == 3

# print("우리집 강아지의 이름은 " + name + "에요")
# name = animal
# print(name, "의 나이는 " + str(age), "살이에요")
# print("뽀미는 3살인가요?" + str(is_adult))

# '''
# 주석이다
# '''

# 연산자
print(1+1-1)
print(3*2/3)

# 나누기, 같다 같지않다 % == !=

# 몫 구하기
print(5//3)

# 제곱
print(2**4)

# not and or
print (not(1 == 3)) # True
print ((3 > 0) and (3 < 5)) # True
print ((3 > 0) or (3 < 5)) # True
print (5 > 4 > 7) # False

# 숫자처리함수 abs pow max min round

from math import *
print(floor(4.99)) # 내림
print(ceil(3.99)) # 올림
print(sqrt(16)) # 제곱근

from random import *

print(random()) # 0.0 ~ 1.0
print(random() * 10 ) # 0.0 ~ 10.0
print(int(random() * 10)) # 0 ~ 10
print(randrange(1, 50)) # 1 ~ 50 미만
print(randint(1, 50)) # 1 ~ 50 이하
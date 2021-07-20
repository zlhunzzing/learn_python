## try

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0}".format(int(nums[2])))
# except ValueError:
#     print("에러떴뜨")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알수없는에러")
#     print(err)

## 에러 발생

# try:
#     print("에러 ㄱㄱ")
#     raise ValueError
# except Exception:
#     print("에러")

## 사용자 정의 에러

# class custonError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("에러 ㄱㄱ")
#     raise custonError("입력값 : {0}".format(input("인풋")))
# except custonError as err:
#     print("에러", err)

## finally


try:
    print("에러 ㄱㄱ")
    raise Exception
finally:
    print("무적권법")
## try

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0}".format(int(nums[2])))
except ValueError:
    print("에러떴뜨")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알수없는에러")
    print(err)
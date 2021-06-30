## if
# weather = input("오늘 날씨는?")
# if weather == "맑음":
#     print("우산을 챙기지마세요")
# elif weather == "비" or weather == "눈":
#     print("우산을챙기세요")
# else: print("hi")

# temp = int(input("기온은 어때요? "))
# if 10 <= temp and temp < 30: # and 생략가능
#     print("괜찮은 날씨에요")

## for
# for waiting_no in [0, 1, 2, 3, 4]:
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

## while
customer = "토르",
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

## continue, break        
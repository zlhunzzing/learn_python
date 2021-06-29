## if
weather = input("오늘 날씨는?")
if weather == "맑음":
    print("우산을 챙기지마세요")
elif weather == "비" or weather == "눈":
    print("우산을챙기세요")
else: print("hi")

temp = int(input("기온은 어때요? "))
if 10 <= temp and temp < 30: # and 생략가능
    print("괜찮은 날씨에요")
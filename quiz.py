## 월 4회, 3번은 온라인 1번은 오프라인 모임 날짜 정하기

# # 조건 1: 랜덤
# # 조건 2: 월별 날짜는 최소 28일
# # 조건 3: 매월 1-3일은 제외

# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

## 사이트 별 비밀번호 생성

# 규칙1: http:// 제외
# 규칙2: 처음만나는 점 (.) 이후부분 제외
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 갯수 + ! 로 구성

url = "http://naver.com"

my_str = url.replace("http://", "")

my_str = my_str[:my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1} 입니다".format(url, password))
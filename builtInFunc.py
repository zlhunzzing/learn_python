## input : 사용자 입력을 받는 함수
# languaage = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())

# lst = [1] # 배열 혹은 문자열 내장 함수 확인 가능
# print(dir(lst))

## 외장함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후
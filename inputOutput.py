### 표준입출력

## import sys 따로 에러 처리

# print("지훈", "뽀미", sep=" with ", end="좋아!")

# 시험 성적
# scores = {"수학": 0, "영어": 50}
# for subject, score in scores.items():
    # print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill  3개 공간, input은 string

## 다양한 출력포맷

# 빈자리 우측정렬
# print("{0: >10}".format(500))
# # # 양수 음수
# print("{0: >+10}".format(500))
# # # 왼측정렬
# print("{0:_<-10}".format(-500))
# # # 3자리 콤마
# print("{0:,}".format(10000000))
# # # to much smile
# print("{0:^<+30,}".format(10000000))
# # # 소수점
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))

## 파일입출력

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# 이어서 쓰기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# print(score_file.readline(), end="")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# 여러 줄출력
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# # score_file.close()
# lines = score_file.readlines() # list
# for line in lines:
#     print(line, end="")

## pickle
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"김지훈", "나이":17, "직업":"여고생"}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

## with
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
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
print("{0: >10}".format(500))
# # 양수 음수
print("{0: >+10}".format(500))
# # 왼측정렬
print("{0:_<-10}".format(-500))
# # 3자리 콤마
print("{0:,}".format(10000000))
# # to much smile
print("{0:^<+30,}".format(10000000))
# # 소수점
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
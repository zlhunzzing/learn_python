### 입출력

## import sys 따로 에러 처리

print("지훈", "뽀미", sep=" with ", end="좋아!")

# 시험 성적
scores = {"수학": 0, "영어": 50}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill  3개 공간, input은 string
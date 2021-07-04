## 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

## 파라미터, default parameter

## 파라미터 키워드 

def profile(name, age, main_lang):
    print(name, age, main_lang)

# profile(name="뽀미", main_lang="한글", age=1)

## 가변인자
# def profile(name, age, lang1, lang2):
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

# profile("김지훈", 17, "JS", "C", "SDSD")

## 지역변수 전역변수

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun
    gun = gun - soldiers
    print("남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
# ## 리스트 []

# list = [10, 20, 30]

# # index

# print("인덱스", list.index(10))

# # append insert pop

# list.append(40)

# list.insert(2, 25)

# print("내보냄", list.pop())

# # count sort reverse

# list.append(10)

# print("카운트", list.count(10))

# list.sort()

# list.reverse

# print(list)

# # clear extend

# # 리스트는 배열과 다르게 크기가 정해져 있지않다 타입 여러개 사용가능

## 사전

# cabinet = {
#     1: "사전",
#     2: "사전@"
# }
# print(cabinet[1], cabinet.get(3, "가능")) # [], get

# # key in cabinet, 재할당, del, clear

# print(cabinet.keys(), cabinet.values(), cabinet.items())

## 튜플

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# (name, age) = ("지훈", 17)
# print(name, age)

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

# 교집합
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python, java.intersection(python))

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java | python, java.union(python))

# 차집합
print(java - python, java.difference(python))

# 추가 제거
python.add("김태호")
java.remove("김태호")
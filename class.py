# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# demage = 5

# print("{} 유닛이 생성되었습니다.".format(name))

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)

## 클래스 확장

# 레이스 : 공중 유닛
wraith1 = Unit("레이스", 80, 5)

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
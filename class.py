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
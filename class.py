# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# demage = 5

# print("{} 유닛이 생성되었습니다.".format(name))

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)

## 클래스 확장

# 레이스 : 공중 유닛
# wraith1 = Unit("레이스", 80, 5)

# # # 마인드 컨트롤 : 상대방 유닛을 내 것으로
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

## 메소드

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        # self.damage = damage
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        # self.name = name
        # self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 파뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

## 상속

## 다중 상속

# 드랍쉽 : 공중 유닛, 공격 x

# 날 수 있는 기능을 가진 클래스

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리 : 공중 공격 유닛

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

## 메소드 오버라이딩

# 벌쳐 : 지상 유닛
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

## 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 서플라이 디폿 : 건물, 1개 건물 = 8개 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()
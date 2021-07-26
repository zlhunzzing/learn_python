## 모듈

# import setModule

# setModule.price(4)

# as 별명, import * - 다 쓰기, import 함수 1, 함수 2 (as 별명)

## 패키지

# import fruit.apple # 클래스나 함수는 직접 import X

# name = fruit.apple.ApplePackage()
# name.detail()

# from fruit.apple import ApplePackage // from은 클래스 import 가능

## __all__ 

# from fruit import *
# name = apple.ApplePackage()
# name.detail()

## 모듈 위치
import inspect
import random

print(inspect.getfile(random))

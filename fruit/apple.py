class ApplePackage:
    def detail(self):
        print("애플")

if __name__ == "__main__":
    print("Apple 모듈을 직접 실행")
    excute = ApplePackage()
    excute()
else:
    print("Aplle 모듈을 외부에서 오출")
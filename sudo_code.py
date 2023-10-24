import copy
# branch testing
# 전역 변수
foodFilePath, stockFilePath = 'files/food.txt', 'files/stock.txt'
foodType = {0: '메인메뉴', 1: '사이드메뉴', 2: '음료수'}
foodList = []
stockDict = {}


class FileIntegrityChecker:
    def __init__(self, filePath):
        self.filePath = filePath

    def checkIntegrity(self):
        # 여기에 파일 무결성을 확인하는 코드를 추가
        pass


def getFoodList():
    # 여기에 food 역직렬화 코드를 추가
    pass


def getStockDict():
    # 여기에 stock 역직렬화 코드를 추가
    pass


class ShoppingBasket:
    # 여기에 ShoppingBasket 클래스 정의
    pass


def chooseMode():
    # 여기에 모드 선택 코드 추가
    pass


def chooseMenu():
    # 여기에 메뉴 선택 코드 추가
    pass


def updateFoodList():
    # 여기에 주문 가능 음식 개수 수정 코드 추가
    pass


def insertBasket(choice, basket):
    # 여기에 장바구니에 추가하는 코드를 추가
    pass


def payment(basket):
    # 여기에 결제 코드를 추가
    pass


def updateStockFile():
    # 여기에 재고 파일 업데이트 코드 추가
    pass


def getDate():
    # 여기에 날짜 입력
    pass


def getId():
    # 여기에 아이디 입력
    pass


def checkDate():
    # 의미 규칙에 맞는 지 확인하는 함수
    pass


def showBasket():
    # 현재 장바구니 출력해주고 메뉴 선택하는 함수
    pass


def modifyBasket():
    # 여기에서 의미 규칙 판단 후 장바구니 수정
    pass


def updateOrderFile():
    # 주문한 내역 order.txt 파일에 저장
    pass

# main 함수


def main():
    global foodList

    while True:
        try:
            a = FileIntegrityChecker(foodFilePath)
            a.checkIntegrity()  # food.txt 파일 무결성 확인

            b = FileIntegrityChecker(stockFilePath)
            b.checkIntegrity()  # stock.txt 파일 무결성 확인

            foodList = getFoodList()  # food 역직렬화
            stockDict = getStockDict()  # stock 역직렬화
            originStockDict = copy.deepcopy(stockDict)  # 깊은 복사
        except Exception as e:
            print(e)  # 파일이 무효하면 프로그램 종료
            exit()

        while True:
            date = getDate()
            if (checkDate(date) == 1):  # 올바른 날짜 입력시까지 입력 계속 받음
                break
        user_id = input()  # 유저아이디 입력

        while True:  # 모드 프롬프트
            basket = ShoppingBasket()  # user_id, date로 인자로 basket 생성

            ret1 = chooseMode()
            if ret1 == 2:  # 종료 선택시
                exit()

            while True:  # 주문 프롬프트
                ret2 = chooseMenu()
                if ret2 == 0:  # 뒤로가기 선택시
                    stockDict = originStockDict
                    break
                elif ret2 == 5:  # 결제하기 선택시
                    ret4 = payment(basket)
                    if ret4 == 1:  # 결제 완료되면
                        updateOrderFile()  # 주문 파일 업데이트
                        updateStockFile()  # 재고 파일 업데이트
                        main()  # main 재귀호출
                        exit()
                elif ret2 == 4:  # 장바구니 수정시
                    while True:
                        ret5 == showBasket()
                        modifyBasket(ret5)  # 장바구니 담을때 주문가능 개수가 변동되는 경우 복구까지
                        if ret5 == 0:
                            break

                else:  # ret2 == 1, 2, or 3
                    while True:  # 장바구니 프롬프트
                        updateFoodList()  # 주문 가능 음식 개수 수정
                        ret3 = insertBasket(ret2, basket)
                        if ret3 == 1:  # 뒤로가기 또는 주문 가능 음식없으면
                            break


main()

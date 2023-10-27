import sys
from res import *
from src.model import *
from src.prompt import *
from src.convert import *
import copy


def main():
    global foodList
    global stockDict
    while True:
        try:
            getFoodList()  # food 역직렬화
            getStockDict()  # stock 역직렬화
            originStockDict = copy.deepcopy(stockDict)  # 깊은 복사
        except Exception as e:
            print(e)  # 파일이 무효하면 프로그램 종료
            exit()

        # 정보 프롬프트
        date = inputUserDate()  # 날짜 입력
        user_id = getUserId()  # 유저아이디 입력

        while True:  # 모드 프롬프트
            # user_id, date로 인자로 basket 생성
            basket = ShoppingBasket(today_date=date, user_id=user_id)

            ret1 = chooseMode()
            if ret1 == 2:  # 종료 선택시
                exit()

            while True:  # 주문 프롬프트
                ret2 = chooseMenu()
                if ret2 == 0:  # 뒤로가기 선택시
                    # stockDict 원래대로 복구
                    stockDict.clear()
                    stockDict.update(originStockDict)
                    break
                elif ret2 == 5:  # 결제하기 선택시
                    ret4 = payment(basket)
                    if ret4 == 1:  # 결제 완료되면
                        updateOrderFile(basket)  # 주문 파일 업데이트
                        updateStockFile()  # 재고 파일 업데이트
                        main()  # main 재귀호출
                        exit()
                elif ret2 == 4:  # 장바구니 수정시
                    while True:
                        ret5 = modifyBasket(basket)
                        if ret5 == 1:
                            break
                else:  # ret2 == 1, 2, or 3
                    while True:  # 장바구니 프롬프트
                        updateFoodList()  # 주문 가능 음식 개수 수정
                        ret3 = insertBasket(ret2, basket)
                        if ret3 == 1:  # 뒤로가기 또는 주문 가능 음식없으면
                            break


def exit():
    sys.exit()


if __name__ == "__main__":
    main()

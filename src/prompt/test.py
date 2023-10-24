"""
test

테스트용 파일입니다.
"""

import basket
import mode 
import order
import sys


class Food:
    """
    예시로 만든 Food 클래스
    """

    def __init__(self, name, price):
        """
        name은 음식 이름, price는 음식 가격
        """
        self.name = name
        self.price = price

FriedChicken = Food("후라이드 치킨", 20000)
SeasonedChicken = Food("양념 치킨", 21000)
BonelessChicken = Food("뼈없는 치킨", 22000)
BSCHicken = Food("순살 양념 치킨", 23000)

if __name__ == "__main__":
    # pizza = basket.Food
    # pizza.price = 10000

    # basket1 = basket.ShooppingBasket()
    # basket1.add(FriedChicken, 2)
    # basket1.add(SeasonedChicken, 3)
    # basket1.add(BonelessChicken, 4)
    # basket1.add(BSCHicken, 5)
    # for i in basket1.basket:
    #     print(i[0].name, i[1])
    # print(basket1.totalPrice)

    while True:  # 모드 프롬프트
        basket1 = basket.ShooppingBasket()

        ret1 = mode.chooseMode()
        if ret1 == 2:  # 종료 선택시
            sys.exit()

        while True:  # 주문 프롬프트
            ret2 = order.chooseMenu()
            if ret2 == 0:  # 뒤로가기 선택시
                # stockDict = originStockDict
                break
            elif ret2 == 4:
                pass
            else:  # ret2 == 1, 2, or 3
                while True:  # 장바구니 프롬프트
                    break

                    # updateFoodList()  # 주문 가능 음식 개수 수정
                    # ret3 = insertBasket(ret2, basket)
                    # if ret3 == 1:  # 뒤로가기 또는 주문 가능 음식
                    #     break

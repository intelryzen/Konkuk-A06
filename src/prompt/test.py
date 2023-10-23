"""
test

테스트용 파일입니다.
"""

import basket

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

    basket1 = basket.ShooppingBasket()
    basket1.add(FriedChicken, 2)
    basket1.add(SeasonedChicken, 3)
    basket1.add(BonelessChicken, 4)
    basket1.add(BSCHicken, 5)
    for i in basket1.basket:
        print(i[0].name, i[1])
    print(basket1.totalPrice)
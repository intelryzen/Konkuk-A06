class ShoppingBasket:
    def __init__(self):
        self.basket = []  # [음식, 수량]을 원소로 갖는 리스트
        self.totalPrice = 0  # basket에 들어있는 음식의 총 가격합

    # 장바구니 담은 목록 출력
    def showBasket(self):
        from main import foodList
        print("장바구니:")
        for item in self.basket:
            food = next(
                (food for food in foodList if food.no == item[0]), None)
            if food:
                print(f"{food.name}: {item[1]}")

    # def addItem(self, food, quantity, price):
    #     """
    #     항목을 basket에 추가하고 totalPrice를 업데이트한다.
    #     food : 음식 이름 혹은 번호
    #     quantity : 음식 수량
    #     price : 음식 단가
    #     """
    #     self.basket.append([food, quantity])
    #     self.totalPrice += price * quantity

from res import foodList


class ShoppingBasket:
    """
    여기에 ShoppingBasket 클래스 정의
    """

    def __init__(self):
        self.basket = []  # [음식번호, 수량]을 원소로 가지는 리스트
        self.totalPrice = 0  # basket에 들어있는 음식의 총 가격합임. 값이 0 이면 장바구니가 비었음을 의미함.

    # 장바구니 담은 목록 출력
    def show(self):
        print("장바구니:")
        for item in self.basket:
            selectedFood = next(
                (food for food in foodList if food.no == item[0]), None)
            if selectedFood:
                print(f"{selectedFood.name}: {item[1]}")

    def add(self, food, quantity):
        """
        장바구니에 음식을 추가함
        """
        # basket에 이미 food.no 을 담았는지 찾는다.
        for item in self.basket:
            if item[0] == food.no:
                item[1] += quantity
                break
        else:  # for-else 구문을 사용하여 for 문이 끝까지 실행되면 새롭게 아이템을 추가함.
            self.basket.append([food.no, quantity])
        self.totalPrice += food.price * quantity

    def remove(self, food, quantity):
        """
        장바구니에서 음식을 삭제함
        """
        self.basket.remove([food.no, quantity])
        self.totalPrice -= food.price * quantity

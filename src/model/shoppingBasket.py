from res import foodList
from .customError import MyCustomError


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
        print("--------------------------")
        for index, item in enumerate(self.basket):
            selectedFood = next(
                (food for food in foodList if food.no == item[0]), None)
            if selectedFood:
                print(f"{index+1}. {selectedFood.name}: {item[1]}")
        print("--------------------------")

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

    # def remove(self, food, quantity):
    #     """
    #     장바구니에서 음식을 삭제함
    #     """
    #     self.basket.remove([food.no, quantity])
    #     self.totalPrice -= food.price * quantity

    def remove(self, selected):
        """
        유효성 검증 및 장바구니에서 음식을 삭제함
        """
        selected_food_index = selected[0] - 1  # 1. 치킨 => 0 번 인덱스
        canceled_quantity = selected[1]

        if 0 > selected_food_index or selected_food_index >= len(self.basket):
            raise MyCustomError(f"선택한 음식이 1 이상 {len(self.basket)} 이하여야 합니다.")
        # 정상 입력
        else:
            # [음식 번호, 수량]
            selected_food = self.basket[selected_food_index]
            food_no = selected_food[0]
            amount = selected_food[1]
            if canceled_quantity <= 0:
                raise MyCustomError(f"취소 가능한 수량은 1 이상이여야 합니다.")
            elif amount < canceled_quantity:
                raise MyCustomError(f"허용되는 수량보다 더 많은 수량을 취소할 수 없습니다.")
            else:
                # 해당 아이템 삭제
                if amount == canceled_quantity:
                    del self.basket[selected_food_index]
                else:
                    self.basket[selected_food_index] = [
                        food_no, amount - canceled_quantity]
                selectedFood = next(
                    (food for food in foodList if food.no == food_no), None)
                self.totalPrice -= selectedFood.price*canceled_quantity
                return food_no

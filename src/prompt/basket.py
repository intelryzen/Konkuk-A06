"""
231022 원규연
"""
        


class ShooppingBasket:
    """
    여기에 ShoppingBasket 클래스 정의
    """

    def __init__(self):
        """
        items는 장바구니에 담긴 상품 목록
        """
        self.basket = [] # [음식,수량]을 원소로 가지는 리스트
        self.totalPrice = 0 # basket에 들어있는 음식의 총 가격합임. 값이 0 이면 장바구니가 비었음을 의미함.
        
        # self.Food = Food

    def add(self, food, quantity):
        """
        장바구니에 음식을 추가함
        """
        self.basket.append([food, quantity])
        self.totalPrice += food.price * quantity

    def remove(self, food, quantity):
        """
        장바구니에서 음식을 삭제함
        """
        self.basket.remove([food, quantity])
        self.totalPrice -= food.price * quantity
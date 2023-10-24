class Food:
    def __init__(self, no, foodTypeNo, name, price, recipe, orderable):
        self.no = no  # 음식 고유번호
        self.foodTypeNo = foodTypeNo  # foodType을 참조하는 번호
        self.name = name  # 음식 이름
        self.price = price  # 음식 가격
        self.recipe = recipe  # stock의 재고번호와 갯수로 구성된 딕셔너리
        self.orderable = orderable  # 주문 가능한 갯수

    # 설계서에 없음.
    # def __str__(self):
    #     return f"음식 이름: {self.name}, 가격: {self.price}원, 주문 가능한 갯수: {self.orderable}"

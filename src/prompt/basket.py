"""
231022 원규연

update foodlist 
"""

"""
class Food:
    def __init__(self, no, foodTypeNo, name, price, recipe, orderable):
        self.no = no  # 음식 고유번호
        self.foodTypeNo = foodTypeNo  # foodType을 참조하는 번호
        self.name = name  # 음식 이름
        self.price = price  # 음식 가격
        self.recipe = recipe  # stock의 재고번호와 갯수로 구성된 딕셔너리
        self.orderable = orderable  # 주문 가능한 갯수
    0 생닭
    1 순살
    2 기름
    3 양념

    후라이드 = {0: 1, 2: 1}
    양념 = {0: 1, 1: 1, 2: 1}
    뼈없는 = {1: 1, 2: 1}
    순살 = {1: 1, 2: 1, 3: 1}
"""
import food


FriedChicken = food.Food(0, 1, "후라이드 치킨", 20000, {0: 1, 2: 1}, 0)
SeasonedChicken = food.Food(1, 1, "양념 치킨", 21000, {0: 1, 2: 1, 3: 1}, 0)
BonelessChicken = food.Food(2, 1, "뼈없는 치킨", 22000, { 1: 1, 2: 1}, 0)
BSCHicken = food.Food(3, 1, "순살 양념 치킨", 23000, {1: 1, 2: 1, 3:1}, 0)

foodList = [FriedChicken, SeasonedChicken, BonelessChicken, BSCHicken]
stockDict = {0: 10, 1: 5, 2: 10, 3: 10}
def updateFoodList():
    """
    전역 변수인 foodList 각각의 Food 객체의 recipe를 읽어 stockDict 의 재고 목록을 토대로 
    해당 음식이 주문 가능하다면 주문 가능한 음식의 수량을,
    더이상 주문 불가능하다면 0을 각 객체의 orderable 에 저장한다.

    foodType = {0: '메인메뉴', 1: '사이드메뉴', 2: '음료수'}
    foodList = []
    stockDict = {}

    """
    global foodList
    global stockDict

    for food in foodList:
        food.orderable = 0
        enableNumber = 0
        leastNumber = 0
        
        for recipeKey in food.recipe.keys():
            leastNumber = stockDict[recipeKey] // food.recipe[recipeKey]
            if stockDict[recipeKey] == 0:
                enableNumber = 0
                break
            if enableNumber == 0 or leastNumber < enableNumber:
                enableNumber = leastNumber

        food.orderable = enableNumber






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

if __name__ == "__main__":
    print(stockDict)
    for food in foodList:
        print(food.name, food.orderable)
    updateFoodList()

    print(foodList[0].name, foodList[0].orderable)
    print(foodList[1].name, foodList[1].orderable)
    print(foodList[2].name, foodList[2].orderable)
    print(foodList[3].name, foodList[3].orderable)

    stockDict[0] = 1
    print(stockDict)
    updateFoodList()


    print(foodList[0].orderable)
    print(foodList[1].orderable)
    print(foodList[2].orderable)
    print(foodList[3].orderable)

    stockDict[0] = 0

    updateFoodList()
    print(foodList[0].orderable)
    print(foodList[1].orderable)
    print(foodList[2].orderable)
    print(foodList[3].orderable)

    a = 0//5
    print(a)
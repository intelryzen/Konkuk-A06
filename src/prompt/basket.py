from ..model import *
from res import *

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


def updateFoodList():
    """
    전역 변수인 foodList 각각의 Food 객체의 recipe를 읽어 stockDict 의 재고 목록을 토대로 
    해당 음식이 주문 가능하다면 주문 가능한 음식의 수량을,
    더이상 주문 불가능하다면 0을 각 객체의 orderable 에 저장한다.
    foodType = {0: '메인메뉴', 1: '사이드메뉴', 2: '음료수'}
    foodList = []
    stockDict = {}
    """
    try: 
        for food in foodList:
            food.orderable = 0
            enableNumber = 0
            leastNumber = 0

            for recipeKey in food.recipe.keys():
                # leastNumber = stockDict[recipeKey] // food.recipe[recipeKey]
                leastNumber = stockDict.get(recipeKey, 0) // food.recipe[recipeKey]
                # if stockDict[recipeKey] == 0:
                if stockDict.get(recipeKey, 0) == 0:
                    enableNumber = 0
                    break
                if enableNumber == 0 or leastNumber < enableNumber:
                    enableNumber = leastNumber

            food.orderable = enableNumber

    except Exception as e:
        print(e)


def updateStockDict(user_selected_food, number, restore=False):
    '''재고 업데이트'''
    if restore:
        for key, value in user_selected_food.recipe.items():
            stockDict[key] = (stockDict[key] + value*number)
    else:
        for stock_number, amount in user_selected_food.recipe.items():
            stockDict[stock_number] = stockDict[stock_number] - \
                amount*number


def insertBasket(foodType, basketObject):
    '''1(주문 가능한 음식이 하나도 없거나 뒤로가기 선택시) 또는 0 반환'''
    # 해당 카테고리 음식이고 주문가능한 음식만 담김
    category_foods = [
        food for food in foodList if food.foodTypeNo == foodType and food.orderable > 0]
    if len(category_foods) == 0:
        print('주문 가능한 음식이 없습니다')
        return 1
    else:
        print("0. 뒤로가기")
        # 주문 가능 음식 모두 출력
        for index, food in enumerate(category_foods):
            print(f"{index + 1}. {food}")
        while True:
            try:
                user = input()
                syntexChecker = PromptSyntaxChecker(user)
                selected = syntexChecker.checkBasketSyntax()
                # 뒤로가기
                if (selected == 0):
                    return 1
                else:
                    selectedFoodIndex = selected[0] - 1
                    # 의미규칙 (선택한 음식)
                    if 0 <= selectedFoodIndex and selectedFoodIndex < len(category_foods):
                        # 사용자가 입력한 담은 수량
                        selectedFood = category_foods[selectedFoodIndex]
                        selectedFoodAmount = selected[1]
                        # 의미규칙 (담은 수량)
                        if selectedFoodAmount <= 0:
                            print("[오류] 입력한 수량이 0과 같거나 작을 수 없습니다.")
                        elif selectedFood.orderable < selectedFoodAmount:
                            print("[오류] 입력한 수량이 주문 가능 수량보다 많을 수 없습니다.")
                        else:
                            # 장바구니에 담음
                            basketObject.add(selectedFood, selectedFoodAmount)
                            updateStockDict(selectedFood, selectedFoodAmount)
                            # 장바구니에 담은 목록 출력
                            basketObject.show()
                            return 0
                    else:
                        print("[오류] 주문 가능한 음식 번호를 정확히 입력하세요.")
            except Exception as e:
                print(e)

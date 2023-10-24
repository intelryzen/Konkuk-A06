from model import *

# 1(주문 가능한 음식이 하나도 없거나 뒤로가기 선택시) 또는 0 반환


def updateStockDict(food, number):
    from main import stockDict


def insertBasket(foodType, basketObject):
    from main import foodList
    # 해당 카테고리 음식이고 주문가능한 음식만 담김
    category_foods = [
        food for food in foodList if food.foodTypeNo == foodType and food.orderable > 0]
    if len(category_foods) == 0:
        print('주문 가능한 음식이 없습니다')
        return 1
    else:
        # 주문 가능 음식 모두 출력
        for index, food in enumerate(category_foods):
            print(f"{index + 1}. {food.name}: {food.price} (가능 수량: {food.orderable})")
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
                        selectedFoodAmount = selected[1]
                        # 의미규칙 (담은 수량)
                        if selectedFoodAmount <= 0:
                            print("[오류] 입력한 수량이 0보다 같거나 작을 수 없습니다.")
                        elif category_foods[selectedFoodIndex].orderable < selectedFoodAmount:
                            print("[오류] 입력한 수량이 주문 가능 수량보다 많을 수 없습니다.")
                        else:
                            # 장바구니에 담음
                            basketObject.basket.append(selected)
                            updateStockDict(
                                food=category_foods[selectedFoodIndex], number=selectedFoodAmount)
                            # 장바구니에 담은 목록 출력
                            basketObject.showBasket()
                            return 0
                    else:
                        print("[오류] 해당되는 음식 번호를 정확히 입력하세요.")
                    # 의미규칙 검사
                    print('[오류] 0 부터 5 까지의 번호를 입력하세요.')
            except Exception as e:
                print(e)

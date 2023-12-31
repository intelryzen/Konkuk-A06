from ..model import PromptSyntaxChecker
from .basket import updateStockDict
from res import foodList
# 1(뒤로가기 또는 장바구니가 비었을 때) 또는 0


def modifyBasket(basket):
    while True:
        if (basket.totalPrice <= 0):
            print("장바구니에 음식이 없습니다.")
            return 1
        else:
            try:
                print("장바구니에 담겨있는 음식목록 중 취소할 '음식번호↹취소할수량'을 입력하세요.")
                print("0. 뒤로가기")
                basket.show()
                user = input()
                # 문법 규칙 체크
                syntexChecker = PromptSyntaxChecker(user)
                selected = syntexChecker.checkBasketSyntax()

                # 뒤로가기 선택시
                if selected == 0:
                    return 1
                else:
                    food_no = basket.remove(selected)
                    # 여기로 넘어오면 바구니에 음식이 제대로 삭제된 상태이며 삭제된 음식 고유 번호를 리턴
                    # 음식객체 가져오기
                    selectedFood = next(
                        (food for food in foodList if food.no == food_no), None)
                    # 재고 수 복구
                    updateStockDict(selectedFood, selected[1], restore=True)

            except Exception as e:
                print(e)

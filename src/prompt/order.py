
from model import *


def showMenu():
    print(
        '''0. 뒤로가기
1. 메인메뉴
2. 사이드메뉴
3. 음료
4. 장바구니
5. 결제하기''')


# 유저가 선택한 메뉴 번호 반환
def chooseMenu():
    while True:
        try:
            showMenu()
            user = input()
            syntexChecker = PromptSyntaxChecker(user)
            selected = syntexChecker.checkDefaultSyntax()
            # 의미규칙 검사
            if (0 <= selected and selected <= 5):
                return selected
            else:
                print('[오류] 0 부터 5 까지의 번호를 입력하세요.')
        except Exception as e:
            print(e)

# 0(결제 불가) 또는 1(결제 완료) 반환


def payment(basketObject):
    from main import foodList
    if basketObject.totalPrice > 0:
        for item in basketObject.basket:
            # 음식 고유번호
            index = item[0]
            # 담은수량 고유번호
            amount = item[1]
            food = next((food for food in foodList if food.no == index), None)
            # 사실상 None 일 경우 없음.
            if food == None:
                continue
            else:
                # 장바구니 아이템 출력
                print(f"{food.name}: {amount}개")
        print(f"총 금액 : {basketObject.totalPrice}")
        print(f'결제가 완료되었습니다.')
        return 1
    else:
        print("장바구니에 음식이 없습니다.")
        return 0

"""
231024 원규연


showMenu 를 호출하고 사용자의 입력을 받아 PromptSyntaxChecker.checkDefaultSyntex 를 호출하여 
올바른 문법인지 확인하고 정상적인 문법(의미 규칙을 포함하며 내부에서 이를 검증함)이라면 최종 입력값을 반환한다.

내부 반복문으로 정상적인 입력값을 반환할 때까지 해당 작업을 반복수행함.

"""


def showMenu():
    """
    0. 뒤로가기 또는 1. 메인메뉴 또는 2. 사이드메뉴 또는 3. 음료수 또는 4. 주문하기
    """
    print("0. 뒤로가기")
    print("1. 메인메뉴")
    print("2. 사이드메뉴")
    print("3. 음료수")
    print("4. 주문하기")

def chooseMenu():
    showMenu()
    menu = input()
    # syntex = PromptSyntaxChecker.checkDefaultSyntex(menu)
    # if syntex == True:
    if menu == '1':
        return 1
    elif menu == '2':
        return 2
    elif menu == '3':
        return 3
    elif menu == '4':
        return 4

    elif menu == '0':
        return 0
    
    else:
        chooseMenu()
    
    # else:
    #     print(syntex)
    #     chooseMenu()

# def insertBasket
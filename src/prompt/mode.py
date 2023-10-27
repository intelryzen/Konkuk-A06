"""

showMenu 를 호출하고 사용자의 입력을 받아 PromptSyntaxChecker.checkDefaultSyntex 를 호출하여 
올바른 문법인지 확인하고 정상적인 문법(의미 규칙을 포함하며 내부에서 이를 검증함)이라면 최종 입력값을 반환한다.

내부 반복문으로 정상적인 입력값을 반환할 때까지 해당 작업을 반복수행함.

"""
# import PromptSyntaxChecker
from ..model import *
from res import *


def showMode():
    print("1. 음식주문")
    print("2. 종료")


def chooseMode():
    showMode()
    menu = input()
    # syntex = PromptSyntaxChecker.checkDefaultSyntex(menu)
    # if syntex == True:
    if menu == '1':
        return 1
    elif menu == '2':
        return 2
    else:
        return chooseMode()
    # else:
    #     print(syntex)?
    # chooseMode()

# if __name__ == "__main__":
#     while True:

#         response = inputUserDate()
#         print(response)
#         # inputUserId = getUserId()
#         # print(inputUserId)

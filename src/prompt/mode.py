"""

showMenu 를 호출하고 사용자의 입력을 받아 PromptSyntaxChecker.checkDefaultSyntex 를 호출하여 
올바른 문법인지 확인하고 정상적인 문법(의미 규칙을 포함하며 내부에서 이를 검증함)이라면 최종 입력값을 반환한다.

내부 반복문으로 정상적인 입력값을 반환할 때까지 해당 작업을 반복수행함.

"""
# import PromptSyntaxChecker
from model import *
from res import *
from datetime import datetime


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
        chooseMode()
    # else:
    #     print(syntex)?
    # chooseMode()


def inputUserDate():
    """
    231026 원규연
    오류 메세지를 자세하게?
    or 
    그냥 오류 메세지만 출력?

    오류검사
    2012.12.25 TRUE
    2111.12.25 FALSE
    2012.13.25 FALSE
    (탭)2012.12.25 FALSE
    (스페이스바)2012.12.25 TRUE
    (스페이스바*6)2012.12.25 TRUE
    2012.12.25(탭) FALSE
    2012.12.25(스페이스바) TRUE

    """

    while True:
        try:
            inputDate = input("날짜를 YYYY.MM.DD 형식으로 입력하세요: ")
            # 스페이스바 파싱
            inputDate = inputDate.replace(" ", "")

            # inputDate 는 반드시 10글자여야 함.
            if len(inputDate) != 10:
                raise MyCustomError("YYYY.MM.DD 형식으로 작성해주세요.")

            # 입력된 문자열을 날짜로 파싱합니다.
            try:
                inputDate = datetime.strptime(inputDate, "%Y.%m.%d")
            except Exception as e:
                raise MyCustomError("유효하지 않은 날짜입니다.")
            # checkValidDate = True

            if 2000 <= inputDate.year <= 2100:
                pass
                # checkValidDate = True
            else:
                raise MyCustomError("년도는 2000년부터 2100년까지 가능합니다.")

        except Exception as e:
            print(e)
            continue

        # 날짜 까지만 반환
        inputDate = inputDate.date()
        return str(inputDate)


def getUserId():
    """
    아이디에 공백이 존재하면 에러를 발생시키고 다시 입력받습니다.

    오류검사 
    a TRUE
    a*6 TRUE
    (스페이스바)a FALSE
    (스페이스바*6)a FALSE
    a(스페이스바) FALSE
    a(스페이스바*6) FALSE
    a(스페이스바)a FALSE
    a(스페이스바*6)a FALSE

    (tab)a FALSE
    (tab*6)a FALSE
    a(tab) FALSE
    a(tab*6) FALSE
    a(tab)a FALSE
    a(tab*6)a FALSE
    """
    while True:
        try:

            inputUserId = input("아이디를 입력하세요: ")

            # 입력받은 아이디에 공백 문자가 있는지 확인합니다.
            if any(char.isspace() for char in inputUserId):
                raise MyCustomError("아이디에 공백이 포함되어 있습니다. 다시 입력하세요.")
            elif len(inputUserId) < 3:
                raise MyCustomError("아이디는 3글자 이상이어야 합니다.")
            else:
                return inputUserId

        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    while True:

        response = inputUserDate()
        print(response)
        # inputUserId = getUserId()
        # print(inputUserId)

from datetime import datetime
from ..model import *
import re

def refineDate(line):
    match = re.search(r'\d{4}-\d{2}-\d{2}', line)
    return match.group

def getLatestDate(file_path):
    """
    order.txt가 있고, 내용이 있다면 가장 아랫줄의 날짜 읽어온다
    order.txt가 있고, 내용이 없다면 아무 날짜나 허용한다.
    order.txt가 없으면, 파일을 만들어야 하고, 아무 날짜나 허용한다
    2000-01-01 이상만 다루므로 1000-01-01을 준다(datetime상에서 가장 작음) 
    """
    try:
        dateTxt = open(file_path, 'r', encoding='UTF-8')
        line = dateTxt.readlines()
        if not line:
            date = datetime.strptime("1000-01-01", "%Y-%m-%d")
            dateTxt.close()
            return date 
        last_line=line[-1].strip()
        date = last_line.split('\t')[0]
        date = datetime.strptime(date, "%Y-%m-%d")
        dateTxt.close()
        return date
    except FileNotFoundError:
        date = datetime.strptime("1000-01-01", "%Y-%m-%d")
        return date  # order.txt가 없음



def inputUserDate(fileDate):
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
            inputDate = inputDate.strip(' ') # 양끝 스페이스바만 허용. \t 이 있으면 오류를 발생해야함.
            inputDate = inputDate.replace(' ',"@") # 발표때 발견한 오류 조치
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
            
            if inputDate>=fileDate:
                pass
            else:
                raise MyCustomError(str(fileDate.strftime("%Y-%m-%d")) + " 와 같거나 이후의 날짜로 입력해주세요.")

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

import sys
from res import *
from model import *
from prompt import *
import copy


def getFoodList():
    global foodList
    # 결제 후 다시 호출될 수 있어서 list 를 항상 비워주어야 함
    foodList.clear()
    try:
        foodTxt = open(foodFilePath, 'r', encoding='UTF8')
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")
    line = foodTxt.readlines()
    for line_number, food in enumerate(line):
        data = food.strip().split('\t')
        if (len(data) == 5):
            try:
                # 정수값으로 정의된것들 확인
                foodNo = int(data[0])
                foodTypeNo = int(data[1])
                price = int(data[3])
                # 음식명
                name = data[2]
                # str -> dic
                recipe = eval(data[4])

                foodList.append(Food(foodNo, foodTypeNo, name, price, recipe))

            except:
                raise MyCustomError(
                    f"{foodFilePath} {line_number+1}번째줄 데이터 타입을 확인해 주세요")
        else:
            raise MyCustomError(f"{foodFilePath} {line_number+1}번째줄 형식이 어긋남")

    # # 확인용
    # print(foodList[3].recipe)

    foodTxt.close()


def getStockDict():
    global stockDict
    # 결제 후 다시 호출될 수 있어서 stockDict 를 항상 비워주어야 함
    stockDict.clear()
    try:
        stockTxt = open(stockFilePath, 'r', encoding='UTF8')
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")

    line = stockTxt.readlines()
    for line_number, stock in enumerate(line):
        data = stock.strip().split('\t')
        if (len(data) == 3):
            try:
                # 재고 번호
                stockNo = int(data[0])
                # 재고 갯수
                stockCnt = int(data[2])

                stockDict[stockNo] = stockCnt
            except:
                raise MyCustomError(
                    f"{stockFilePath} {line_number+1}번째줄 재고 번호나 수량이 정수값이 아닙니다.")
        else:
            raise MyCustomError(
                f"{stockFilePath} {line_number+1}번째줄 형식이 어긋남")

    # 확인용
    # print(stockDict)

    stockTxt.close()

def updateStockFile():
    newStockTxt = ''

    try:
        stockTxt = open(stockFilePath, 'r', encoding='UTF8')
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")

    line = stockTxt.readlines()
    for line_number, stock in enumerate(line):
        data = stock.strip().split('\t')
        if (len(data) == 3):
            try:
                # 재고 번호
                stockNo = int(data[0])
                # 파싱한 데이터 업데이트
                data[2] = str(stockDict[stockNo])
                # 재고 갯수만 수정하여 다시 묶음
                newStockTxt += '\t'.join(data) + '\n'
            except:
                raise MyCustomError(
                    f"{stockFilePath} {line_number+1}번째줄 재고 번호나 수량이 정수값이 아닙니다.")
        else:
            raise MyCustomError(
                f"{stockFilePath} {line_number+1}번째줄 형식이 어긋남")

    stockTxt.close()

    try:
        stockTxt = open(stockFilePath, 'w', encoding='UTF8')
        stockTxt.write(newStockTxt)
        stockTxt.close()
    except:
        raise MyCustomError("파일 쓰기에 실패했습니다.")


def updateOrderFile(basket):
    #기존 주문 내용 확인
    try:
        with open(orderFilePath, 'r', encoding='UTF8') as file_data:
            originOrderTxt = file_data.read()
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")

    # 우선 유저 이름 및 날자 임의로 세팅
    newOrderTxt = '홍길동' + '\t' + '2023.10.26'

    #장바구니 내의 음식 데이터 추가
    for item in basket:
        newOrderTxt += '\t'
        selectedFood = next(
            (food for food in foodList if food.no == item[0]), None)
        if selectedFood:
            newOrderTxt += selectedFood.name + '\t' + str(item[1]) + '\t' + str(selectedFood.price * item[1])

    #끝 구분자 추가
    newOrderTxt += '\t#'
    #기존 주문기록이 날아가지 않게 이어서 작성
    newOrderTxt = originOrderTxt + '\n' + newOrderTxt

    try:
        orderTxt = open(orderFilePath, 'w', encoding='UTF8')
        orderTxt.write(newOrderTxt)
        orderTxt.close()
    except:
        raise MyCustomError("파일 쓰기에 실패했습니다.")




def exit():
    sys.exit()


def main():
    global foodList
    global stockDict
    while True:
        try:
            getFoodList()  # food 역직렬화
            getStockDict()  # stock 역직렬화
            originStockDict = copy.deepcopy(stockDict)  # 깊은 복사
        except Exception as e:
            print(e)  # 파일이 무효하면 프로그램 종료
            exit()

        # while True:
        #     date = getDate()
        #     if (checkDate(date) == 1):  # 올바른 날짜 입력시까지 입력 계속 받음
        #         break
        # user_id = input()  # 유저아이디 입력

        while True:  # 모드 프롬프트
            basket = ShoppingBasket()  # user_id, date로 인자로 basket 생성

            ret1 = chooseMode()
            if ret1 == 2:  # 종료 선택시
                exit()

            while True:  # 주문 프롬프트
                ret2 = chooseMenu()
                if ret2 == 0:  # 뒤로가기 선택시
                    # stockDict 원래대로 복구
                    stockDict.clear()
                    stockDict.update(originStockDict)
                    break
                elif ret2 == 5:  # 결제하기 선택시
                    ret4 = payment(basket)
                    if ret4 == 1:  # 결제 완료되면
                        updateOrderFile(basket.basket)  # 주문 파일 업데이트
                        updateStockFile()  # 재고 파일 업데이트
                        main()  # main 재귀호출
                        exit()
                elif ret2 == 4:  # 장바구니 수정시
                    while True:
                        ret5 = modifyBasket(basket)
                        if ret5 == 1:
                            break
                else:  # ret2 == 1, 2, or 3
                    while True:  # 장바구니 프롬프트
                        updateFoodList()  # 주문 가능 음식 개수 수정
                        ret3 = insertBasket(ret2, basket)
                        if ret3 == 1:  # 뒤로가기 또는 주문 가능 음식없으면
                            break


if __name__ == "__main__":
    main()

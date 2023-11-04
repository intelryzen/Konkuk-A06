from res import *
from ..model.customError import MyCustomError
from ..model.food import Food


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
                if (foodNo < 1) :
                    raise MyCustomError(
                        f"{foodFilePath} {line_number + 1}번째줄 음식 번호를 확인해 주세요")

                foodTypeNo = int(data[1])
                if (foodTypeNo > 3 or foodTypeNo < 1) :
                    raise MyCustomError(
                        f"{foodFilePath} {line_number + 1}번째줄 음식 타입 번호를 확인해 주세요")
                price = int(data[3])
                if (price < 1) :
                    raise MyCustomError(
                        f"{foodFilePath} {line_number + 1}번째줄 음식 가격을 확인해 주세요")
                # 음식명
                name = data[2]
                # str -> dic
                recipe = eval(data[4])
                for key, value in recipe.items():
                    if (key < 1) :
                        raise MyCustomError(
                            f"{foodFilePath} {line_number + 1}번째줄 재료 번호를 확인해 주세요")
                    if (value < 1) :
                        raise MyCustomError(
                            f"{foodFilePath} {line_number + 1}번째줄 재료 갯수를 확인해 주세요")

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

    if (len(stockDict)) == 0 :
        raise MyCustomError("재고가 없습니다.")

    # 확인용
    # print(stockDict)

    stockTxt.close()

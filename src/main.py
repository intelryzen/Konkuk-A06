import copy
from prompt import *
from model import *

# 전역 변수
foodFilePath, stockFilePath = '../files/food.txt', '../files/stock.txt'
foodType = {0: '메인메뉴', 1: '사이드메뉴', 2: '음료수'}
foodList = []
stockDict = {}


def main():
<<<<<<< HEAD
    basket = ShoppingBasket()
    value = chooseMenu()
    if value == 5:
        payment(basket)
    # test()
    # print("시작")
=======
    getStockDict()

# class FileIntegrityChecker:

class Food:
    def __init__(self, no, foodTypeNo, name, price, recipe):
        self.no = no
        self.foodTypeNo = foodTypeNo
        self.name = name
        self.price = price
        self.recipe = recipe
        #최초에는 0으로 초기화
        self.orderable = 0

def getStockDict():
    try:
        stockTxt = open(stockFilePath, 'r', encoding='UTF8')
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")

    line = stockTxt.readlines()
    for stock in line:
        data = stock.strip().split('\t')
        if (len(data) == 3):
            try:
                #재고 번호
                stockNo = int(data[0])
                #재고 갯수
                stockCnt = int(data[2])

                stockDict[stockNo] = stockCnt
            except:
                raise MyCustomError("재고 번호나 수량이 정수값이 아닙니다.")
        else:
            raise MyCustomError("파일 형식에 어긋남")

    # 확인용
    print(stockDict)


# def getFoodList():
#     try:
#         foodTxt = open(foodFilePath, 'r', encoding='UTF8')
#     except:
#         raise MyCustomError("파일 읽기에 실패했습니다.")
#     line = foodTxt.readlines()
#     for food in line:
#         data = food.strip().split('\t')
#         if (len(data) == 5):
#             try:
#
#             except:
#                 raise MyCustomError("재고 번호나 수량이 정수값이 아닙니다.")
#         else:
#             raise MyCustomError("파일 형식에 어긋남")



class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

>>>>>>> af64ab10fba3ed702bd03d9c21fbe7b8da61236e


if __name__ == "__main__":
    main()

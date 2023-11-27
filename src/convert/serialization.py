import fileinput
from res import *
from ..model.customError import MyCustomError


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


def updateOrderFile(basket, user):
    # 기존 주문 내용 확인
    try:
        with open(orderFilePath, 'a+', encoding='UTF8') as file_data:
            file_data.seek(0)
            originOrderTxt = file_data.read()
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")

    # 유저 이름 및 날자 세팅
    newOrderTxt = user.date + '\t' + user.id

    # 장바구니 내의 음식 데이터 추가
    for item in basket.basket:
        newOrderTxt += '\t'
        selectedFood = next(
            (food for food in foodList if food.no == item[0]), None)
        if selectedFood:
            newOrderTxt += selectedFood.name + '\t' + \
                str(item[1]) + '\t' + str(selectedFood.price * item[1])

    # 기존 주문기록이 날아가지 않게 이어서 작성
    if originOrderTxt == '':
        newOrderTxt = newOrderTxt
    else:
        newOrderTxt = originOrderTxt + '\n' + newOrderTxt

    try:
        orderTxt = open(orderFilePath, 'w', encoding='UTF8')
        orderTxt.write(newOrderTxt)
        orderTxt.close()
    except:
        raise MyCustomError("파일 쓰기에 실패했습니다.")

def updateUserCoupon(user_id, couponList):
    try:
        with fileinput.input(couponFilePath, inplace=True, encoding='UTF8') as f:
            for line in f:
                # user id 로 시작하는 행만 수정
                # 앞부분이 겹치는 아이디 있을수 있으니 탭까지 검색
                if line.startswith(user_id + '\t'):
                    couponData = user_id + '\t'
                    for index, coupon in couponList:
                        couponData += coupon.price + '\t' + coupon.expiredDate + '\t' + coupon.isUsed
                        # 마지막 쿠폰은 탭 없이
                        if index != len(couponList) -1:
                            couponData += '\t'
                    print(couponData, end='\n')
                else:
                    print(line, end='')
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")

def updateUserPoint(user_id, PointList):
    try:
        with fileinput.input(pointFilePath, inplace=True, encoding='UTF8') as f:
            for line in f:
                # user id 로 시작하는 행만 수정
                # 앞부분이 겹치는 아이디 있을수 있으니 탭까지 검색
                if line.startswith(user_id + '\t'):
                    pointData = user_id + '\t'
                    for index, point in PointList:
                        pointData += point['price'] + '\t' + point['date']
                        # 마지막 포인트는 탭 없이
                        if index != len(PointList) -1:
                            pointData += '\t'
                    print(pointData, end='\n')
                else:
                    print(line, end='')
    except:
        raise MyCustomError("파일 읽기에 실패했습니다.")
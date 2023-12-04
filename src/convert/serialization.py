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
            newOrderTxt += str(selectedFood.no) + '\t' + selectedFood.name + '\t' + \
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

# def updateUserCoupon(user_id, couponList):
#     try:
#         with fileinput.input(couponFilePath, inplace=True, encoding='UTF8') as f:
#             for line in f:
#                 # user id 로 시작하는 행만 수정
#                 # 앞부분이 겹치는 아이디 있을수 있으니 탭까지 검색
#                 if line.startswith(user_id + '\t'):
#                     couponData = user_id + '\t'
#                     for index, coupon in enumerate(couponList):
#                         # couponData += str(coupon.price) + '\t' + coupon.expiredDate + '\t' + coupon.isUsed # 이전코드 
#                         couponData += str(coupon.price) + '\t' + str(coupon.expiredDate) + '\t' + str(coupon.isUsed)
#                         # 마지막 쿠폰은 탭 없이
#                         if index != len(couponList) -1:
#                             couponData += '\t'
#                     print(couponData, end='\n')
#                 else:
#                     print(line, end='')
#     except Exception as e:
#         # 디버깅용 print
#         print(e)

#         raise MyCustomError("파일 읽기에 실패했습니다.")



def updateUserCoupon(user_id, couponList):
    """
    new
    """
    try:
        found_user = False

        with fileinput.input(couponFilePath, inplace=True, encoding='UTF8') as f:
            for line in f:
                # user id 로 시작하는 행만 수정
                # 앞부분이 겹치는 아이디 있을수 있으니 탭까지 검색
                # 탭으로 분리
                divided_line = line.split('\t')
                
                if divided_line[0] == user_id:
                    # print('updateUserCoupon   id는 ', divided_line)
                # if line.startswith(user_id + '\t'):
                    couponData = user_id + '\t'
                    # print(couponData)
                    for index, coupon in enumerate(couponList):
                        couponData += str(coupon.price) + '\t' + str(coupon.expiredDate) + '\t' + str(coupon.isUsed)
                        # 마지막 쿠폰은 탭 없이
                        if index != len(couponList) - 1:
                            couponData += '\t'
                    print(couponData, end='\n')
                    found_user = True
                else:
                    print(line, end='')

            # 사용자를 찾지 못한 경우, 새로운 행 추가
            if not found_user:
                new_entry = user_id + '\t'
                for index, coupon in enumerate(couponList):
                    new_entry += str(coupon.price) + '\t' + str(coupon.expiredDate) + '\t' + str(coupon.isUsed)
                    if index != len(couponList) - 1:
                        new_entry += '\t'
                # 파일에 추가하는 부분
                with open(couponFilePath, 'a', encoding='UTF8') as f:
                    f.write(new_entry + '\n')


            # 사용자를 찾지 못한 경우, 새로운 행 추가
                # if not found_user:


    except Exception as e:
        # 디버깅용 print
        # print(e)

        raise MyCustomError("파일 읽기에 실패했습니다.")


# def updateUserCoupon2(user_id, couponList):
#     try:
#         with fileinput.input(couponFilePath, inplace=True, encoding='UTF8') as f:
#             for line in f:
#                 # user id 로 시작하는 행만 수정
#                 # 앞부분이 겹치는 아이디 있을수 있으니 탭까지 검색
#                 if line.startswith(user_id + '\t'):
#                     couponData = user_id + '\t'
#                     for index, coupon in couponList:
#                         couponData += coupon['price'] + '\t' + coupon['date'] + '\t' + coupon['use']
#                         # 마지막 쿠폰은 탭 없이
#                         if index != len(couponList) -1:
#                             couponData += '\t'
#                     print(couponData, end='\n')
#                 else:
#                     print(line, end='')
#     except:
#         raise MyCustomError("파일 읽기에 실패했습니다.")

# def updateUserPoint(user_id, PointList):
#     try:
#         print('updateUserPoint', user_id, PointList)
#         with fileinput.input(pointFilePath, inplace=True, encoding='UTF8') as f:
#             for line in f:
#                 # user id 로 시작하는 행만 수정
#                 # 앞부분이 겹치는 아이디 있을수 있으니 탭까지 검색
#                 if line.startswith(user_id + '\t'):
#                     pointData = user_id + '\t'
#                     for index, point in enumerate(PointList):
#                         # pointData += point['point'] + '\t' + point['date'] # 이전코드
#                         pointData += str(point['point']) + '\t' + str(point['date'])
#                         # 마지막 포인트는 탭 없이
#                         if index != len(PointList) -1:
#                             pointData += '\t'
#                     print(pointData, end='\n')
#                 else:
#                     # user id 가 없다면 마지막행에 추가
#                     # print(line, end='') # 이전코드
#                     print(line, end='')
#                     pointData = user_id + '\t'
#                     for index, point in enumerate(PointList):
#                         # pointData += point['point'] + '\t' + point['date'] # 이전코드
#                         pointData += str(point['point']) + '\t' + str(point['date'])
#                         # 마지막 포인트는 탭 없이
#                         if index != len(PointList) -1:
#                             pointData += '\t'
#                     print(pointData, end='\n')
    
        # except Exception as e:
        #     # 디버깅용 print
        #     print(e)
        #     raise MyCustomError("파일 읽기에 실패했습니다.")


def updateUserPoint(user_id, PointList):
    """
    new
    """
    try:
        # print('updateUserPoint', user_id, PointList)
        found_user = False

        with fileinput.input(pointFilePath, inplace=True, encoding='UTF8') as f:
            for line in f:
                # user id 로 시작하는 행만 수정
                # 앞부분이 겹치는 아이디 있을수 있으니 탭까지 검색
                # 탭으로 분리
                divided_line = line.split('\t')
                
                if divided_line[0] == user_id:
                    # print('updateUserPoint   id는 ', divided_line)
                # if line.startswith(user_id + '\t'):
                    pointData = user_id + '\t'
                    for index, point in enumerate(PointList):
                        pointData += str(point['point']) + '\t' + str(point['date'])
                        # 마지막 포인트는 탭 없이
                        if index != len(PointList) - 1:
                            pointData += '\t'
                    print(pointData, end='\n')
                    found_user = True
                else:
                    print(line, end='')

            # 사용자를 찾지 못한 경우, 새로운 행 추가



            if not found_user:
                new_entry = user_id + '\t'
                for index, point in enumerate(PointList):
                    new_entry += str(point['point']) + '\t' + str(point['date'])
                    if index != len(PointList) - 1:
                        new_entry += '\t'
                # 파일에 추가하는 부분
                with open(pointFilePath, 'a', encoding='UTF8') as f:
                    f.write(new_entry + '\n')
                    

                
                

    except Exception as e:
        # 디버깅용 print
        # print(e)

        raise MyCustomError("파일 읽기에 실패했습니다.")
                    

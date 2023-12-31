import sys
from res import foodType
from ..model import *
import math
from datetime import datetime, timedelta


# 임의의 user 객체 생성
# userObject = User('test', 1000, '2021-05-01', {'price': 1000, 'date': '2021-05-01', 'use': True})

"""
이거 변수이름 enable, disalbe로 하자 굳이 variable, invariable로 하지 말자

이거 다시생각해보니깐
어차피 기한 지난 쿠폰과 사용된 쿠폰은 변할 일이 없다
즉 사용하거나 추가할일이 없음

그러니깐 variableCouponList랑 invariableCouponList로 나누고
variableCouponList를 화면에 띄우고
variableCouponList에서 선택한 쿠폰을 invariableCouponList로 옮기는게 나을듯
그리고 결제안하면 업데이트를 안하면 되고
결제 하면 업데이트를 하면 되고

그리고 결제액에 따라서 쿠폰이 생성된다면
variableCouponList에다가 쿠폰 추가해주면 되고
그리고 최종 CouponList를 업데이트 해주면 됨

그리고 이 단계까지 들어가면 취소가 없음
쿠폰을 사용하든 말든 결제까지 완료됨


"""


def makeCouponFromPoint(basketObject, userObject):
    """
    231128
    여기가 지금 dict라서 문제가 생기는거 같음
    class object로 바꿔야할듯

    ====================
    point로 쿠폰 발급
    총 결제액 = point로 변환 후 10000포인트 당 1000원 쿠폰 발급
    쿠폰 발급 후 쿠폰 유효기간은 1주일
    pointList에 point 추가 (포인트가 0원남더라도 0원이라고 명시적 추가)

    point를 사용해서 쿠폰을 발급하게 된다면 반드시 유효기간에 임박한 point부터 사용해야하고
    사용이 됐다면 구조적으로 결제당일이 아닌 포인트는 0이 될수밖에 없음

    결제당일 pointList는 삭제 후 재생성으로 날짜당 1개의 point만 존재하게 됨
    

    쿠폰 발급 후 enableCouponList에 추가
    포인트가 사용됐다면 pointList 갱신
    """

    limitedDate = datetime.strptime(userObject.date, '%Y-%m-%d') + timedelta(days=6)
    limitedDate = limitedDate.strftime('%Y-%m-%d')

    #기존 point
    originPoint = 0
    for i in userObject.enablePoint_list:
        originPoint += int(i['point'])

    newPoint = basketObject.totalPrice
    pointSum = newPoint + originPoint
    # print(newPoint)
    # print(originPoint)
    # print(userObject.enablePoint_list)
    
    usePointSwitch = False
    if pointSum >= 10000:
        usePointSwitch = True

    # point로 쿠폰 발급
    # 기한은 1주일
    while pointSum >= 10000:
        pointSum -= 10000
        coupon = Coupon(1000, limitedDate, 0)
        userObject.enableCoupon_list.append(coupon)

    if usePointSwitch:
        for i in range(len(userObject.enablePoint_list)):
            userObject.enablePoint_list[i]['point'] = 0
            if userObject.enablePoint_list[i]['date'] == limitedDate:
                del userObject.enablePoint_list[i]
        userObject.enablePoint_list.append({'point': pointSum, 'date': limitedDate})

    else:
        for i in range(len(userObject.enablePoint_list)):
            if userObject.enablePoint_list[i]['date'] == limitedDate:
                userObject.enablePoint_list[i]['point'] = int(userObject.enablePoint_list[i]['point']) + newPoint 
                break
        else:
                userObject.enablePoint_list.append({'point': newPoint, 'date': limitedDate})
    # print(userObject.enablePoint_list)
    
    


def chooseCoupon(basketObject, userObject):
    """
    쿠폰 선택
    쿠폰 선택시 총 금액에서 쿠폰 가격만큼 차감

    예를 들어, 쿠폰 액면가가 1000원이고 쿠폰을 5개 가지고있고 지금 2700원을 결제하려는 상황이면, 보유 쿠폰 목록에는 5개의 쿠폰들이 모두 출력되지만, 프롬프트에는:

        min(5, ceil(2700 / 1000)) = min(5, 3) = 3

    이므로 "사용할 쿠폰 갯수를 입력하세요 (0 ~ 3):" 이라고 나오길 원합니다.

    이제, 이 프롬프트에 대한 사용자의 키입력을 k라고 할 때:

    * k가 0일 경우: '사용하지 않겠다'는 의미로 간주하고 결제 완료
    * k가 정수고 0 < k ≤ n일 경우: k 개의 쿠폰을 사용해서 결제 완료
    * k가 정수고 n < k ≤ C일 경우: "진짜요?" 라고 출력하고 쿠폰 갯수 입력 프롬프트 다시 띄움
    * k가 정수고 C < k일 경우: "뻥치지 마세요" 라고 출력하고 쿠폰 갯수 입력 프롬프트 다시 띄움
    * 그 외의 입력일 경우: "잘못된 입력입니다" 라고 출력하고 쿠폰 갯수 입력 프롬프트 다시 띄움

    이렇게 진행되게 해주세요.
    """
    couponPrice = 1000

    can_use_coupon_amount = min(len(userObject.enableCoupon_list), math.ceil(basketObject.totalPrice / couponPrice))
    if len(userObject.enableCoupon_list) > 0:

        while True:
            # # 디버깅용 print
            # for coupon in userObject.enableCoupon_list:
            #     print('사용 가능한 쿠폰 목록입니다.', coupon.price, coupon.expiredDate, coupon.isUsed)
            # for coupon in userObject.disableCoupon_list:
            #     print('사용 불가능한 쿠폰 목록입니다.', coupon.price, coupon.expiredDate, coupon.isUsed)
            # print(f'사용 가능한 포인트 목록입니다.', userObject.enablePoint_list)
            # print(f'사용 불가능한 포인트 목록입니다.', userObject.disablePoint_list)

            print(f'사용 가능한 쿠폰 목록입니다.')
            for i in range(len(userObject.enableCoupon_list)):
                print(f'{i+1}. {userObject.enableCoupon_list[i]}')
            
            print(f'사용하실 쿠폰 개수를 입력하세요. (0 ~ {can_use_coupon_amount}) : ')
          
            
            try:
                # user = input()
                # syntexChecker = PromptSyntaxChecker(user)
                # selected = syntexChecker.checkDefaultSyntax()
                selected = int(input())
                
                # k = 0 (결제 완료)
                if selected == 0:
                    return 1
                # 0 < k <= n (결제 완료)
                elif 0 < selected <= can_use_coupon_amount:
                    while selected > 0:
                        basketObject.totalPrice -= userObject.enableCoupon_list[selected-1].price
                        userObject.enableCoupon_list[selected-1].isUsed = 1
                        userObject.disableCoupon_list.append(userObject.enableCoupon_list[selected-1])
                        del userObject.enableCoupon_list[selected-1]                        
                        selected -= 1
                    return 1
                # n < k <= c
                elif can_use_coupon_amount < selected <= len(userObject.enableCoupon_list):
                    print(f'진짜요?')
                    continue
                # c < k
                elif len(userObject.enableCoupon_list) < selected:
                    print(f'뻥치지 마세요')
                    continue
                # selected < 0
                else:
                    print(f'잘못된 입력입니다')
                    continue

                
            except Exception as e:
                # print(e) # 디버깅용
                print(f'잘못된 입력입니다')
                continue    



def showMenu():
    print(f'''0. 뒤로가기
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


# def payment(basketObject,userObject):
#     from chicken import foodList
#     if basketObject.totalPrice > 0:
#         basketObject.show()
#         print(f"총 금액 : ₩{basketObject.totalPrice}")
#         print(f'결제가 완료되었습니다.')
#         return 1
#     else:
#         print("장바구니에 음식이 없습니다.")
#         return 0

# region new

def combinePointCoupon(userObject):
    """
    point와 coupon을 합친 list를 반환
    """
    combinedPointList = []
    combinedCouponList = []

    for i in userObject.enablePoint_list:
        combinedPointList.append(i)
    for i in userObject.disablePoint_list:
        combinedPointList.append(i)
    for i in userObject.enableCoupon_list:
        combinedCouponList.append(i)
    for i in userObject.disableCoupon_list:
        combinedCouponList.append(i)

    userObject.pointList = combinedPointList
    userObject.couponList = combinedCouponList
    

# endregion new


def payment(basketObject, userObject):
    if basketObject.totalPrice > 0:
        basketObject.show()
        print(f"총 금액 : ₩{basketObject.totalPrice}")
        if userObject.enableCoupon_list:
            # print(f'사용 가능한 쿠폰이 있습니다.')
            if chooseCoupon(basketObject, userObject):
                makeCouponFromPoint(basketObject, userObject)

                # # 디버깅용 print
                # for coupon in userObject.enableCoupon_list:
                #     print('사용 가능한 쿠폰 목록입니다.', coupon.price, coupon.expiredDate, coupon.isUsed)
                # for coupon in userObject.disableCoupon_list:
                #     print('사용 불가능한 쿠폰 목록입니다.', coupon.price, coupon.expiredDate, coupon.isUsed)
                # print(f'사용 가능한 포인트 목록입니다.', userObject.enablePoint_list)
                # print(f'사용 불가능한 포인트 목록입니다.', userObject.disablePoint_list)

                # print(f'사용 가능한 쿠폰 목록입니다.', userObject.enableCoupon_list)
                # print(f'사용 불가능한 쿠폰 목록입니다.', userObject.disableCoupon_list)
                # print(f'사용 가능한 포인트 목록입니다.', userObject.enablePoint_list)
                # print(f'사용 불가능한 포인트 목록입니다.', userObject.disablePoint_list)
                
                # # 디버깅용 print
                print(f'결제가 완료되었습니다. 결제가격은 ₩{basketObject.totalPrice}입니다.')
                combinePointCoupon(userObject)
                # print(f'전체 포인트 목록입니다.', userObject.pointList)
                return 1
            else:
                return 0
        else:
            makeCouponFromPoint(basketObject, userObject)
            combinePointCoupon(userObject)
            print(f'사용 가능한 쿠폰이 없습니다.')
            print(f'결제가 완료되었습니다. 결제가격은 ₩{basketObject.totalPrice}입니다.')
            return 1
    else:
        print("장바구니에 음식이 없습니다.")
        return 0
    

if __name__ == '__main__':
    temp_basket = ShoppingBasket('2021-05-01', 'test')
    temp_basket.add(foodList[0], 1)
    temp_basket.add(foodList[1], 1)

    temp_user = User('test', '2021-05-02', [{'point': 3000, 'date': '2021-05-01'}, {'point': 5000, 'date': '2021-05-02'}], [{'price': 1000, 'date': '2021-05-01', 'use': True}, {'price': 1000, 'date': '2021-05-02', 'use': True}])
    a = payment(temp_basket, temp_user)
    print(a)
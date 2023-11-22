from res import foodType
from ..model import *



class User:
    """
    임의의 user class
    구성요소: id, 주문날짜, pointList, coupon, 
    """
    def __init__(self, id, date, pointList, couponList):
        self.id = id
        self.date = date
        self.pointList = pointList # int라고 가정, 현재 날짜 기준 유효한 포인트
        self.enablePoint_list, self.disablePoint_list = sorting_enablePoint(self.pointList, self.date)

        
        self.couponList = couponList #dict가 모인 list 라고 가정
        self.enableCoupon_list, self.disableCoupon_list = sorting_enableCoupon(self.couponList, self.date)
        

        """
        pointList = [
            {
                'point': 'point', 
                'date': 'pointDate'
            },

            {
                'point': 'point',
                'date': 'pointDate'
            }
        ]

        point = 적립 포인트 int 형식 10000원당 1000원쿠폰으로 변환
        pointDate = 포인트 유효기간(적립날자 아님)'2021-05-01' 형식
        """

        """
        couponList = [
            {
                'price': 'couponPrice',
                'date': 'couponDate',
                'use': 'couponUse'
            },

            {
                'price': 'couponPrice',
                'date': 'couponDate',
                'use': 'couponUse'
            }
        ]

        couponPrice = 쿠폰 할인 가격 int 형식 (현재는 1000)
        couponDate = 쿠폰유효기간(발급날자 아님)'2021-05-01' 형식
        couponUse = True or False , True면 사용가능, False면 사용불가능
        """

# 임의의 user 객체 생성
userObject = User('test', 1000, '2021-05-01', {'price': 1000, 'date': '2021-05-01', 'use': True})

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
def sorting_enablePoint(pointList, date):
    """
    enablePointList, disablePointList로 나누는 함수
    나누고 sorting까지 해줌

    point를 사용해서 쿠폰을 발급하게 된다면 반드시 유효기간에 임박한 point부터 사용해야함
    """
    enablePointList = []
    disablePointList = []
    for i in pointList:
        if i['date'] >= date:
            enablePointList.append(i)
        else:
            disablePointList.append(i)
    enablePointList.sort(key=lambda x: x['date'])
    disablePointList.sort(key=lambda x: x['date'])
    return enablePointList, disablePointList
    

def sorting_enableCoupon(couponList, date):
    """
    enableCouponList, disableCouponList로 나누는 함수
    나누고 sorting까지 해줌

    """


    enableCouponList = []
    disableCouponList = []
    for i in couponList:
        if i['date'] >= date and i['use'] == True:
            enableCouponList.append(i)
        else:
            disableCouponList.append(i)
    enableCouponList.sort(key=lambda x: x['date'])
    enableCouponList.sort(key=lambda x: x['use'], reverse=True)
    disableCouponList.sort(key=lambda x: x['date'])
    disableCouponList.sort(key=lambda x: x['use'], reverse=True)
    return enableCouponList, disableCouponList

def after_payment(basketObject, userObject):
    """
    make_coupon_from_point 함수로
    쿠폰발급,
    포인트 사용 후

    enableCouponList, disableCouponList 를 합쳐서 couponList로 업데이트
    enablePointList, disablePointList 를 합쳐서 pointList로 업데이트
    해당 내용을 쿠폰은 ticket.txt에, 포인트는 point.txt에 저장
    파일이 없다면 생성
    a+모드로 하면 될듯? 
    아 잠만 이러면 아이디당 다 다르니깐
    덮어쓰기가 안됨
    걍 읽어서 id같은애 있으면 그 줄 쌩으로 삭제하고 다시 쓰는걸로
    id같은애 없으면 그냥 새로 쓰면 될듯

    쿠폰도 마찬가지 

    point.txt
    포인트:
    <탭><포인트><탭><유효기간>
    포인트들:
    <포인트>
    <포인트><포인트들>
    포인트(point.txt 의 한 행):
    <아이디><탭><포인트들><탭><개행문자>



    ticket.txt
    쿠폰:
    <탭><쿠폰금액><탭><유효기간><탭><사용여부>
    쿠폰들:
    <쿠폰>
    <쿠폰><쿠폰들>
    쿠폰(ticket.txt 의 한 행):
    <아이디><탭><쿠폰들><개행문자>

    """
    
    userObject.couponList = userObject.enableCoupon_list + userObject.disableCoupon_list
    userObject.pointList = userObject.enablePoint_list + userObject.disablePoint_list

    userObject.enableCoupon_list, userObject.disableCoupon_list = sorting_enableCoupon(userObject.couponList, userObject.date)
    userObject.enablePoint_list, userObject.disablePoint_list = sorting_enablePoint(userObject.pointList, userObject.date)

    updatePointFile(userObject)
    updateCouponFile(userObject)



def updatePointFile(userObject):
    """
    point.txt에 저장하는 함수
    """
    pass

def updateCouponFile(userObject):
    """
    ticket.txt에 저장하는 함수 
    """
    pass

def make_coupon_from_point(basketObject, userObject):
    """
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

    limitedDate = userObject.date + 7

    #기존 point
    originPoint = 0
    for i in userObject.enablePoint_list:
        originPoint += i['point']

    newPoint = basketObject.totalPrice

    # point로 쿠폰 발급
    # 기한은 1주일
    while newPoint >= 10000:
        newPoint -= 10000
        userObject.enableCoupon_list.append({'price': 1000, 'date': limitedDate, 'use': True})

    for i in range(len(userObject.enablePoint_list)):
        userObject.enablePoint_list[i]['point'] = 0
        if userObject.enablePoint_list[i]['date'] == limitedDate:
            del userObject.enablePoint_list[i]
    userObject.enablePoint_list.append({'point': newPoint, 'date': limitedDate})


def selectCoupon(basketObject, userObject):
    """
    쿠폰 선택
    쿠폰 선택시 총 금액에서 쿠폰 가격만큼 차감
    쿠폰 적용시 주문 금액이 0원 이하가 되면 해당 쿠폰사용을 마지막으로 종료
    쿠폰은 반복해서 사용 가능 
    """
    if len(userObject.enableCoupon_list) > 0:

        while True:
            print(f'사용 가능한 쿠폰 목록입니다.')
            print(f'0. 사용하지 않음')
            for i in range(len(userObject.enableCoupon_list)):
                print(f'{i+1}. {userObject.enableCoupon_list[i]}')
            print(f'사용하실 쿠폰 번호를 입력하세요.')
            try:
                user = input()
                syntexChecker = PromptSyntaxChecker(user)
                selected = syntexChecker.checkDefaultSyntax()
                if selected == 0:
                    return 1
                elif selected <= len(userObject.enableCoupon_list):
                    print(f'쿠폰이 적용되었습니다.')
                    print(f'총 금액 : ₩{basketObject.totalPrice}')
                    basketObject.totalPrice -= userObject.enableCoupon_list[selected-1]['price']
                    userObject.enableCoupon_list[selected-1]['use'] = False
                    userObject.disableCoupon_list.append(userObject.enableCoupon_list[selected-1])
                    del userObject.enableCoupon_list[selected-1]
                    print(f'총 금액 : ₩{basketObject.totalPrice}')
                    if basketObject.totalPrice <= 0:
                        print(f'최종 결제 금액은 0원입니다.')
                        print(f'결제가 완료되었습니다.')
                        return 1
                    else:
                        print(f'사용 가능한 쿠폰이 있습니다.')
                        continue
                else:
                    print('[오류] 존재하지 않는 쿠폰입니다.')

                if basketObject.totalPrice <= 0:
                    print(f'최종 결제 금액은 0원입니다.')
                    print(f'결제가 완료되었습니다.')
                    return 1
                
                if len(userObject.enableCoupon_list) == 0:
                    print(f'사용 가능한 쿠폰이 없습니다.')
                    return 1
            except Exception as e:
                print(e)
                continue    



def showMenu():
    print(f'''0. 뒤로가기
1. {foodType[1]}
2. {foodType[2]}
3. {foodType[3]}
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

def payment(basketObject,userObject):
    from chicken import foodList
    if basketObject.totalPrice > 0:
        basketObject.show()
        print(f"총 금액 : ₩{basketObject.totalPrice}")
        if userObject.enableCoupon_list:
            print(f'사용 가능한 쿠폰이 있습니다.')
            if selectCoupon(basketObject, userObject):
                print(f'결제가 완료되었습니다.')
                return 1
            else:
                return 0
        else:
            print(f'사용 가능한 쿠폰이 없습니다.')
            print(f'결제가 완료되었습니다.')
            return 1
    else:
        print("장바구니에 음식이 없습니다.")
        return 0
    
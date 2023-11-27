from datetime import datetime, timedelta

"""
user.py로 할라다가 user라는 이름이 뭔가 오류가 생길수도 있을 것 같아서
임의로 user.py로 이름을 변경

"""

class User:
    """
    임의의 user class
    필요 매개변수: id, 주문날짜, pointList, coupon, 
    """
    def __init__(self, id, date, pointList, couponList):
        self.id = id
        self.date = date
        self.pointList = pointList # int라고 가정, 현재 날짜 기준 유효한 포인트
        self.enablePoint_list, self.disablePoint_list = sorting_enablePoint(self.pointList, self.date)
        self.couponList = couponList #dict가 모인 list 라고 가정
        self.enableCoupon_list, self.disableCoupon_list = sorting_enableCoupon(self.couponList, self.date)
        # print(self.couponList[-1])
        # print(sorting_enableCoupon(self.couponList, self.date))
        
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


def sorting_enablePoint(pointList, date):
    """
    enablePointList, disablePointList로 나누는 함수
    나누고 sorting까지 해줌

    point를 사용해서 쿠폰을 발급하게 된다면 반드시 유효기간에 임박한 point부터 사용해야함
    """
    enablePointList = []
    disablePointList = []
    
    for i in pointList:
        # 현재 날짜
        current_date = datetime.strptime(date, '%Y-%m-%d')
        coupon_date = datetime.strptime(i['date'], '%Y-%m-%d')
        
        # 7일 이내인지 확인
        is_within_7_days = (current_date - coupon_date) <= timedelta(days=7)

        if is_within_7_days:
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
        if i.expiredDate >= date and i.isUsed == 0:
            enableCouponList.append(i)
        else:
            disableCouponList.append(i)
    enableCouponList.sort(key=lambda x: x.expiredDate)
    enableCouponList.sort(key=lambda x: x.isUsed, reverse=True)
    disableCouponList.sort(key=lambda x: x.expiredDate)
    disableCouponList.sort(key=lambda x: x.isUsed, reverse=True)
    return enableCouponList, disableCouponList
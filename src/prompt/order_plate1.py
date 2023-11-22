from res import foodType
from ..model import *



class User:
    """
    임의의 user class
    구성요소: id, point, coupon, 주문날짜
    """
    def __init__(self, id, point, date, coupon):
        self.id = id
        self.point = point # int라고 가정, 현재 날짜 기준 유효한 포인트
        self.date = date
        self.coupon = coupon #dict 라고 가정, 현재 날짜 기준 유효한 쿠폰
        self.enableCoupon_list = sorting_coupon(self.coupon, self.date)
        
        """
        coupon = {
            'price': 'couponPrice'
            'date': 'couponDate'
            'use': 'couponUse'
                  }
        
        couponDate = 쿠폰유효기간(발급날자 아님)'2021-05-01' 형식
        couponPrice = 쿠폰 할인 가격 int 형식 (현재는 1000)
        couponUse = True or False , True면 사용가능, False면 사용불가능
        """

# 임의의 user 객체 생성
userObject = User('test', 1000, '2021-05-01', {'price': 1000, 'date': '2021-05-01', 'use': True})


def sorting_coupon(coupon, date):
    """
    ticket.txt에 저장하는것도 고려한 함수
    # 쿠폰 유효기간이 빠른 순으로 정렬
    # 사용한 쿠폰은 사용하지 않은 쿠폰보다 뒤로 정렬
    주문 완료 후 한번 더 호출해서 사용된 쿠폰은 use를 False로 바꿔줘야함
    """


    coupon_list = []
    for i in coupon:
        coupon_list.append(i)
    coupon_list.sort(key=lambda x: x['date'])
    coupon_list.sort(key=lambda x: x['use'], reverse=True)
    return coupon_list

def sorting_enableCoupon(coupon, date):
    """
    화면에 출력될 쿠폰만 정렬
    # sorting된 쿠폰 중 사용가능한 쿠폰만 반환
    # 유효기간이 지난 쿠폰은 제외
    # 사용한 쿠폰은 제외
    """


    enableCoupon_list = []
    for i in coupon:
        if i['date'] >= date and i['use'] == True:
            enableCoupon_list.append(i)
    return enableCoupon_list


"""
현재 쿠폰에 고유 id가 없어서 
만료일자와 사용여부가 같다면 같은 쿠폰이라고 가정
즉 그냥 순서상 먼저오는애의 use를 False로 바꿈
"""




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


def payment(basketObject,userObject):
    from chicken import foodList
    if basketObject.totalPrice > 0:
        
        # 쿠폰 개수
        
        if len(userObject.coupon) > 0 :
            print(f'사용 가능한 쿠폰 목록입니다.')
            print(f'0. 사용하지 않음')
            for i in range(len(userObject.coupon)):
                print(f'{i+1}. {userObject.coupon[i]}')
            print(f'사용하실 쿠폰 번호를 입력하세요.')
            while True:
                try:
                    user = input()
                    syntexChecker = PromptSyntaxChecker(user)
                    selected = syntexChecker.checkDefaultSyntax()
                    if selected == 0:
                        break
                    elif selected <= len(userObject.coupon):
                        print(f'쿠폰이 적용되었습니다.')
                        print(f'총 금액 : ₩{basketObject.totalPrice}')
                        print(f'결제가 완료되었습니다.')
                        return 1
                    else:
                        print('[오류] 존재하지 않는 쿠폰입니다.')
                except Exception as e:
                    print(e)
        basketObject.show()
        print(f"총 금액 : ₩{basketObject.totalPrice}")
        print(f'결제가 완료되었습니다.')
        return 1
    else:
        print("장바구니에 음식이 없습니다.")
        return 0


import sys
from res import *
from src.model import *
from src.prompt import *
from src.convert import *
import copy


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

        # 정보 프롬프트
        # date = inputUserDate()  # 날짜 입력
        # user_id = getUserId()  # 유저아이디 입력

        """
        파일이 지금은 없으니 임의로 user생성
        """

        date  = '2021-05-02'
        user_id = 'test'

        basket_temp1 = ShoppingBasket()
        # basket_temp1.add(foodList[0], 1)
        basket_temp1.add(foodList[4], 1)

        temp_point_list = [{'point': 3000, 'date': '2021-05-01'}, {'point': 5000, 'date': '2021-05-02'}]
        temp_coupon_list = [{'price': 1000, 'date': '2021-05-01', 'use': True}, 
                            {'price': 1000, 'date': '2021-05-02', 'use': True}, 
                            {'price': 1000, 'date': '2021-05-03', 'use': True},
                            {'price': 1000, 'date': '2021-05-04', 'use': False},
                            ]
        temp_user = User('test', '2021-05-02', [{'point': 3000, 'date': '2021-05-01'}, {'point': 5000, 'date': '2021-05-02'}], temp_coupon_list)




        ret4 = payment(basket_temp1, temp_user)
        if ret4 == 1:  # 결제 완료되면
            try:
                updateOrderFile(basket_temp1)  # 주문 파일 업데이트
                updateStockFile()  # 재고 파일 업데이트
                main()  # main 재귀호출
            except Exception as e:
                print(e)  # 파일오류
            exit()




def exit():
    sys.exit()


if __name__ == "__main__":
    main()

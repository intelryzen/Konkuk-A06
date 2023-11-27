class Coupon:
    def __init__(self, price, expiredDate, isUsed):
        self.price = price  # 쿠폰 가격
        self.expiredDate = expiredDate  # 쿠폰 만료일
        self.isUsed = isUsed  # 쿠폰 사용 여부

    def __str__(self):
        return f"₩{self.price} 유효기간: {self.expiredDate} ({'사용됨' if self.isUsed == 1 else '사용가능'})"

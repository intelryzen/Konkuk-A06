from model.customError import MyCustomError


class PromptSyntaxChecker:
    def __init__(self, inputValue):
        self.inputValue = inputValue

    def checkDefaultSyntax(self):
        try:
            value = int(self.inputValue)
            # 예외적인 경우나 입력값의 범위 등을 여기서 확인하고,
            # 문법에 맞지 않으면 MyCustomError를 발생시킬 수 있음
            return value
        except ValueError:
            raise MyCustomError(f"문법에 맞지 않은 입력입니다.")

    def checkBasketSyntax(self):
        try:
            if self.inputValue == '0':  # 뒤로가기의 경우
                return 0

            foodNumber, quantity = map(int, self.inputValue.split('\t'))
            # 예외적인 경우나 입력값의 범위 등을 여기서 확인하고,
            # 문법에 맞지 않으면 MyCustomError를 발생시킬 수 있음
            return [foodNumber, quantity]
        except ValueError or IndexError:
            raise MyCustomError(f"입력 오류입니다. '0' 또는 '음식번호↹수량' 을 입력하세요")

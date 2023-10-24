import os
from .customError import MyCustomError


class FileIntegrityChecker:
    def __init__(self, filePath):
        self.filePath = filePath

    def checkIntegrity(self):
        if not os.path.exists(self.filePath):
            raise MyCustomError(f"The file {self.filePath} does not exist.")

        # 파일 내용을 읽어서 문법 규칙을 검사하는 코드를 추가 구현 필요
        # 예:
        # with open(self.filePath, 'r') as file:
        #     lines = file.readlines()
        #     for line in lines:
        #         if not self.isValidSyntax(line):
        #             raise FileIntegrityError("The file has invalid syntax.")

        # 각 행의 문법 규칙을 검사하는 코드를 구현 필요
        # 이 함수는 각 행이 정상적인 문법 규칙을 따르고 있는지 검사하여
        # 규칙을 따르고 있으면 True를, 그렇지 않으면 False를 반환해야 함
        pass

import copy
from prompt import *
from model import *

# 전역 변수
foodFilePath, stockFilePath = 'files/food.txt', 'files/stock.txt'
foodType = {0: '메인메뉴', 1: '사이드메뉴', 2: '음료수'}
foodList = []
stockDict = {}


def main():
    test()
    print("시작")


main()

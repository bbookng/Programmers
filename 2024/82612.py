def solution(price, money, count):
    answer = sum([price * i for i in range(1, count+1)])
    if money - answer < 0:
        return answer - money
    else:
        return 0
def solution(wallet, bill):
    answer = 0
    wallet.sort()

    while True:
        bill.sort()
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            return answer

        answer += 1
        bill[1] //= 2

    return answer
import math

def solution(fees, records):
    answer = []
    parking = dict()
    total = dict()

    for record in records:
        time, number, inout = record.split()
        time = list(map(int, time.split(':')))
        if inout == 'IN':
            parking[number] = time[0] * 60 + time[1]
        else:
            car_in = parking[number]
            car_out = time[0] * 60 + time[1]
            parking.pop(number)

            if number not in total:
                total[number] = car_out - car_in
            else:
                total[number] += car_out - car_in

    if parking:
        for k, v in parking.items():
            if k in total:
                total[k] += 1439 - v
            else:
                total[k] = 1439 - v

    total = sorted(total.items())

    for number, time in total:
        fee = fees[1]
        time -= fees[0]
        if time > 0:
            fee += math.ceil(time / fees[2]) * fees[3]

        answer.append(fee)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
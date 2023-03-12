import heapq

def solution(lines):
    answer = 1
    log_list = []

    for line in lines:
        date, s, t = line.split()
        h, m, s = map(float, s.split(':'))

        end_date = int(h * 3600 * 1000) + int(m * 60 * 1000) + int(s * 1000)
        start_date = end_date - int(float(t.replace('s', '')) * 1000) + 1

        log_list.append([start_date, end_date])

    log_list.sort(key=lambda x: x[0])

    arr = []

    # 시작 시간이 앞 로그의 종료 시간보다 작거나 같을 때 겹침
    for log in log_list:
        std = log[0]
        while arr:
            if std - 1000 >= arr[0][1]:
                heapq.heappop(arr)
            else:
                break
        heapq.heappush(arr, log)
        answer = max(answer, len(arr))

    return answer

print(solution( [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
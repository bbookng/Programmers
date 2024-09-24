def solution(video_len, pos, op_start, op_end, commands):
    op_start = calculator(op_start)
    op_end = calculator(op_end)
    video_len = calculator(video_len)
    pos = calculator(pos)

    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if command == 'next':
            if video_len - pos < 10:
                pos = video_len
            else:
                pos += 10
        elif command == 'prev':
            if pos < 10:
                pos = 0
            else:
                pos -= 10

    if op_start <= pos <= op_end:
        pos = op_end

    answer = str(pos // 60).zfill(2) + ':' + str(pos % 60).zfill(2)

    return answer


def calculator(t):
    mm, ss = t.split(':')
    return int(mm) * 60 + int(ss)
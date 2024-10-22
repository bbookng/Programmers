def solution(bandage, health, attacks):
    std_time = 0
    max_health = health

    for attack in attacks:
        time, amount = attack

        # 공격 이전 회복량 계산
        healing_time = time - std_time - 1
        if healing_time > 0:
            total = healing_time * bandage[1]
            if time - std_time > bandage[0]:
                bonus = (time - std_time) // bandage[0]
                total += bonus * bandage[2]
        else:
            total = 0

        # 체력 회복 (최대 체력 초과 방지)
        health = min(max_health, health + total)

        # 공격으로 인한 체력 감소
        health -= amount

        # 체력 확인: 공격 후 즉시 확인
        if health <= 0:
            return -1

        # 현재 시간 업데이트
        std_time = time

    return health

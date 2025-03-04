def solution(hp, monsters, attack):
    monster_damage = {
        -1: 0,  # 회피
        0: monsters['골렘'],
        1: monsters['리본돼지'],
        2: monsters['슬라임']
    }
    
    for hit in attack:
        hp -= monster_damage[hit]
        if hp <= 0:
            return -1
    
    return hp

# 테스트 케이스
hp = 200
monsters = {'골렘': 40, '리본돼지': 20, '슬라임': 10}

attack = [-1, 0, 1, 1, 0, 2, -1, 1]
attack2 = [0, 0, 0, 0, 0, 2, -1, 1]
attack3 = [-1, -1, 1, 1, 0, 2, -1, 1]
attack4 = [-1, -1, -1, -1, -1, -1, -1, -1]

print(solution(hp, monsters, attack))   # 50
print(solution(hp, monsters, attack2))  # -1
print(solution(hp, monsters, attack3))  # 90
print(solution(hp, monsters, attack4))  # 200


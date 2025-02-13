# 목적 : 리스트 숙련 + 자료구조 및 알고리즘 습득
# 리스트 자유자재로 다루기 예제

# 01
# -------------------------------------------------------------------------
# 난이도 = 입문자 , 알고리즘
# 아래는 클럽에 입장하려는 사람들의 나이를 순서대로 담은 리스트입니다.
ages = [18, 20, 17, 15, 13, 12, 21, 24, 33]

# 이 중 19살 이하의 나이를 가진 사람을 입구컷 시키는 로직을 작성하세요.
def ipguCut(result):
    ages.sort()
    result = []
    result = ages[0:5]
    return result

print(ipguCut(ages))

# 팁1. sort  +  리스트 슬라이싱 list[0:3] ... 을 활용하여 푸는 알고리즘
# 팁2. for문, 그리고 if 문을 활용한 알고리즘

ages = [18, 20, 17, 15, 13, 12, 21, 24, 33]

def ipguCut(input):
    result = []
    for i in ages:
        if ages:
            if i <= 19:
                result += [i]
            else:
                pass
    return result
print(ipguCut(ages))
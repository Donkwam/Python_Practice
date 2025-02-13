# 04
# -------------------------------------------------------------------------
# 난이도 = 초~중급 , 리스트 가지고 놀기
# [1, 3, 5, 7, 9 .....] 와같이 정수 n 을 입력하면 1부터 n까지의 홀수만 반환하는 함수를 작성하세요.

def oddList(n):
    answer = []
    return [x for x in range(1,n) if x % 2 == 1]    # oddList에 밑에 값을 받아서 n에 5를 넣어서 계산 하여 리스트로 배열열

print(oddList(5)) # 결과 : [1,3]
print(oddList(8)) # 결과 : [1,3,5,7]

# 팁1. 리스트 컴프리핸션 활용
# 팁2. for문과 if문 활용

def oddList(n):
    answer = []
    for i in range(1,n):
        if i % 2 == 1:
            answer += [i]
    return  answer

print(oddList(5)) # 결과 : [1,3]
print(oddList(8)) # 결과 : [1,3,5,7]
# 05
# -------------------------------------------------------------------------
# 난이도 = 초~중급 , string과 배열의 유사한 점 ?!

# 반갑습니다 를 notice 변수를 활용하여 출력하시오.
notice = "다니습갑반"
result = ""
for i in range(len(notice) - 1, -1, -1): # i 는 문자열 notice 의 마지막 인덱스에서 0 까지 -1씩 감소한다는 뜻
    result += notice[i] # notice의 인덱스에서 뒤에서 부터 차례대로 result에 넣는다?
    print(i)
print(result)

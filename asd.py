
# 딕셔너리 데이터
people = { '최보정': 1995, '이형우': 1996, '강석준': 1995, '우동관': 2000, '황석준': 1996, '김찬수': 2000 }

# 나이 계산 및 출력
for name, birth_year in people.items():
    age = 2025 - birth_year
    print(f'{name} : {age}세')

print(people.items())

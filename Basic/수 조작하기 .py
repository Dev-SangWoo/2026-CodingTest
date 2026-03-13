# 📝 문제 정보
# 문제 이름: 수 조작하기 
# 난이도/출처: 프로그래머스 Lv.0
# 핵심 개념: 문자열 순회

# --------------------------------------------

# 💡 풀이 전략 (Approaches)
# 아이디어: 
# 시간 복잡도: 
# 제약 조건: 

# --------------------------------------------

# ⚠️ 삽질 포인트 (Troubleshooting)
# 처음에 왜 막혔는지, 혹은 어떤 부분에서 시간 초과나 WA가 났는지 적습니다.
# 예: "정렬을 내림차순으로 해야 하는데 오름차순으로 해서 틀림"

# --------------------------------------------

# ✅ 최종 코드 (Code)
# 여기에 깔끔하게 정리된 코드를 붙여넣으세요.
def solution(n, control):
# 먼저 순회로 하나씩 문자 받고
# if로
    for i in control:
        if i=='w':
            n += 1 
        elif i=='s':
            n -= 1
        elif i=='d':
            n += 10
        elif i=='a':
            n -= 10
   
    answer = n
    return answer

print(solution(0,"wsdawsdassw"))

# --------------------------------------------

# 🧠 배운 점 & 복습할 내용
# 문제에서 새로 알게 된 문법이나 테크닉을 적습니다.
# 다음에 비슷한 문제를 만난다면 어떻게 접근할지 한 줄로 요약합니다.

def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])
#zip으로 키-value 묶어서 dict 형태로

def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer
#요기도 결국 객체로 만들어 key-value 구조로 가져감
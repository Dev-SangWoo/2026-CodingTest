# 📝 문제 정보
# 문제 이름: 글자 지우기
# 난이도/출처: 프로그래머스 Lv.0
# 핵심 개념: join, 리스트컴프리헨션, enumerate() 

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
def solution(my_string, indices):
    indices = set(indices)  # 빠른 조회를 위해 집합으로 변환
    return ''.join([ch for idx, ch in enumerate(my_string) if idx not in indices])
#리스트 컴프리헨션으로 배열로 만듬
# enumerate()로 인덱스와 문자열 동시 취득
# indices 아닌 것만 취득하기 

# --------------------------------------------

# 🧠 배운 점 & 복습할 내용
# 문제에서 새로 알게 된 문법이나 테크닉을 적습니다.
# 다음에 비슷한 문제를 만난다면 어떻게 접근할지 한 줄로 요약합니다.ㅌㅋ

def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer
#반대로 안 잘라도 되는 걸 취하기  (not in)


def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)
# 정렬 후 뒤에서 부터 자르기(그러면 중간에 인덱싱이 바뀔 필요 없음) sorted(indices, resverse=True)
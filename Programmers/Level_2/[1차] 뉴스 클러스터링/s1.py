

def make_dict(str):
    length = len(str)

    # dict에 저장해서 반환
    dict = {}

    # 문자열을 2글자씩 확인
    i = 0

    while i < length-1:
        # 우선 문자인지 확인
        if str[i].isalpha() and str[i+1].isalpha():
            tmp = str[i].lower() + str[i+1].lower()

            # 이렇게 in을 사용해서 key가 있나 없나 확인
            if tmp in dict:
                dict[tmp] += 1
            else:
                dict[tmp] = 1
        i += 1
    return dict


def J(dict_a:dict, dict_b:dict):
    key_a = dict_a.keys()
    key_b = dict_b.keys()

    if len(key_a) <= len(key_b):
        keys = key_a
    else:
        keys = key_b

    # 교집합 세기
    # 공통 key값을 세고 각 dict의 공통 value값 중 큰 것을 더해줌
    anb = 0

    # 공통 key값
    common_keys = set()
    for key in key_a:
        if key in key_b:
            common_keys.add(key)

    for key in common_keys:
        if dict_a[key] <= dict_b[key]:
            anb += dict_a[key]
        else:
            anb += dict_b[key]



    # 합집합 세기
    # 공통키에 있는 key들 중에서 두 dict중 큰 dict값을 더함
    # 공통키에 없으면 그냥 값을 더함
    aub = 0

    # 공통 key값 중 큰것 더해주기
    for key in common_keys:
        if dict_a[key] >= dict_b[key]:
            aub += dict_a[key]
        else:
            aub += dict_b[key]
    
    # a만 있는 key값 더해줌
    for key in key_a:
        if not(key in common_keys):
            aub += dict_a[key]

    # b만 있는 key값 더해줌
    for key in key_b:
        if not (key in common_keys):
            aub += dict_b[key]

    # 문제의 예외처리 조건
    if aub == 0:
        return 1
    
    ans = anb/aub
    return ans




def solution(str1, str2):
    answer = 0
    # 입력을 2글자씩 끊어서 다중 집합의 원소로 만듬
    # 자카드 유사도 AnB / AuB


    dict_a = make_dict(str1)
    dict_b = make_dict(str2)

    ans = J(dict_a, dict_b)
    answer = int(ans*65536)
    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2','AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
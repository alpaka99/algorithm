def solution(s):
    answer = ''
    str2num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    i = 0
    while i < len(s):
        # 숫자면
        if s[i].isdigit():
            answer += s[i]
            i += 1
        # 문자면
        else:
            j = 0
            while not (s[i+j].isdigit()):
                j += 1
                tmp = s[i:i+j]
                if tmp in str2num.keys():
                    num = str2num[tmp]
                    answer += num
                    break
            i += j
    return answer

print(solution("one4seveneight"))
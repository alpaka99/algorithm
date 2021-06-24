import sys
sys.stdin = open("input.txt", "r")

# T: test case
# 각 줄에 주어지는 n을 소인수 분해 해야함

for tc in range(1,int(input())+1):
    # 우선 숫자를 받고
    n = int(input())

    # 숫자의 소인수를 찾아야함

    # 우선 약수를 찾고 그 중에 소수를 찾을까
    # 아니면 소수를 쫙 찾고 그것들을 한번씩 나눠가면서 약수인지 판별할까...
    # 개인적으로는 2번이 더 구현하기 편할거같음


    # n 이하의 소수를 찾아보자
    # 0부터 sqrt(n)까지 0으로 채워진 list를 만들고
    # 소수가 아닌 수는 다 1로 체크하자

    primes =[0]*(int(n**0.5)+1)
    # 0이랑 1은 소수가 아니니까 미리 1로 체크해주기
    primes[0], primes[1] = 1, 1

    for i in range(2, len(primes)):
        # 소수가 아닌 수
        if primes[i]:
            continue
        else:
            # 소수인 수(i) 발견
            # 그러면 이 수의 배수들은 싹 다 1로 넣기
            j = 2
            while i*j < int(n**0.5)+1:
                primes[i*j] = 1
                j += 1
    # sqrt(n)까지의 소수는 금방 찾네
    # 여기서 어떻게 발전을 못 시킬까...
    # 지금 문제가 divs안에 들어있는 수의 반대편 수가 소수일때 일어나니까
    # 반대편 수가 소수인지 검사를 해줘야하는데



    #이러면 index를 소수로 갖는 칸은 다 0, 소수가 아닌칸은 다 1
    # 그러면 이 중에서 0인 칸 중 n을 나눴을때 0인 값을 다 list에 담으면 됨
    divs = []
    for i in range(len(primes)):
        if primes[i] == 0:
            if n % i == 0:
                divs.append(i)

############## 대진님 피드백받고 고친 부분 ############
    # 이제 소수인 sqrt(n)까지의 약수는 다 들어있음
    # 그럼 여기서 하나씩 반대편 수를 찾고
    # 소수인지 아닌지 검사를 해보자
    # 어짜피 제곱수의 경우가 있으니까 sort해야하니까 걍 하자
    for i in range(len(divs)):
        # 반대편 수 num
        num = int(n / divs[i])
        
        # divs내에 중복된 값 안만들기
        if num == divs[i]:
            continue

        # num이 소수인가 아닌가?
        # 약수가 있으면 소수가 아님
        prime_flag = True
        for j in range(2,int(num**0.5)):
            # print(j)
            if num % j == 0:
                prime_flag = False
                break
        # 만약 num이 소수면
        if prime_flag:
            divs.append(num)

################################################################
    
    # 만약 스스로가 소수라면.. divs에 아무것도 안들어있을것이므로
    # 스스로를 추가해준다
    if not divs:
        divs.append(n)


    # divs를 몇번 썻는지 확인하는 count list
    count = [0]*len(divs)

    # 이제 divs에 약소수만 담겨있으므로
    # 이걸 이용해서 나누면 됨
    N = n
    for i in range(len(divs)):
        while n != 1:
            # 더이상 안나눠 떨어지면...
            if n % divs[i]:
                break
            else:
                #나눠 떨어지면
                count[i] += 1
                n /= divs[i]

    print("#{} {}은".format(tc, N))
    for i in range(len(divs)):
        print("{}가 {}번,".format(divs[i], count[i]), end = " ")
    print("\b\b으로 이루어져 있습니다")

    # 오... 언팩킹은 신기하구만...
    print("#{}".format(tc),*divs)
# 이젠 잘 돌아가겠지..?
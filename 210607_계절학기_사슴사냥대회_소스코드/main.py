import random

DEER = 0
RABBIT = 1
SNAKE = 2

# 아래 Me 함수를 작성해서 제출하세요.
def Me(opp, turn, opp_prev, opp_last_pattern):
    sasum = opp_last_pattern[opp].count(0)
    toki = opp_last_pattern[opp].count(1)
    bam = opp_last_pattern[opp].count(2)

    # # turn이 0일떄
    if turn == 0:
        if sasum == 0:
            return 2

        elif sasum != 0:
            return random.randint(0,2)

    else:
        # 사슴 많이 낸 사람
        if sasum >= toki and sasum >= bam:
            # 이전에 사슴 -> 또 사슴을 안낼거임
            if opp_prev == 0:
                return 2
            else:
                return 0
        
        # 상대방이 토끼를 많이 낸 사람
        elif toki >= sasum and toki >= bam:
            # 이전에 토끼를 냄 -> 페널티를 피하려고 사슴아니면 뱀을 낼거임
            if opp_prev == 1:
                if sasum > bam:
                    return 0
                else:
                    return 2
            else:
                return 1
        # 상대방이 뱀을 가장 많이 냄
        elif bam >= sasum and bam >= toki:
            # 이전에 뱀을 냄 -> 토끼 혹은 사슴
            if opp_prev == 2:
                if sasum > toki:
                    return 0
                else:
                    return 1
            else:
                return 2

    return random.randint(0,2)
    
    

# def Opponent1(opp, turn, opp_prev, opp_last_pattern):
#     return 0
def Opponent1(opp, turn, opp_prev, opp_last_pattern):
    sasum = opp_last_pattern[opp].count(0)
    toki = opp_last_pattern[opp].count(1)
    bam = opp_last_pattern[opp].count(2)

    # # turn이 0일떄
    if turn == 0:
        if sasum == 0:
            return 2

        elif sasum != 0:
            return random.randint(0,2)

    else:
        # 사슴 많이 낸 사람
        if sasum >= toki and sasum >= bam:
            # 이전에 사슴 -> 또 사슴을 안낼거임
           return 0
        
        # 상대방이 토끼를 많이 낸 사람
        elif toki >= sasum and toki >= bam:
            # 이전에 토끼를 냄 -> 페널티를 피하려고 사슴아니면 뱀을 낼거임
            if opp_prev == 1:
                if sasum > bam:
                    return 0
                else:
                    return 2
            else:
                return 1
        # 상대방이 뱀을 가장 많이 냄
        elif bam >= sasum and bam >= toki:
            # 이전에 뱀을 냄 -> 토끼 혹은 사슴
            if opp_prev == 2:
                if sasum > toki:
                    return 0
                else:
                    return 1
            else:
                return 2
                
    return random.randint(0,2)

def Opponent2(opp, turn, opp_prev, opp_last_pattern):
    if turn == 0:
        return 1
    return opp_prev

def Opponent3(opp, turn, opp_prev, opp_last_pattern):
    if turn == 0:
        return 2
    return opp_prev

def Register(name, func):
    global  f_inx
    names[f_inx] = name
    f[f_inx] = func
    f_inx += 1


###################  main  #######################
f = [0] * 150
names = [""] * 100
f_inx = 0
total_score =[0] * 150
last_pattern = [[[0] * 10 for _ in range(150)] for _ in range(150)] # [팀][대전][패턴]
pattern_count = [0] * 150

Register("Me", "Me")

Register("Opp1", "Opponent1")
Register("Opp2", "Opponent2")
Register("Opp3", "Opponent3")

for i in range(140):
    for j in range(140):
        for k in range(10):
            last_pattern[i][j][k] = -1

for i in range(1, f_inx):
    for j in range(f_inx):
        team_a = j % f_inx
        team_b = (j+i) % f_inx
        print("[{}] vs [{}]".format(names[team_a], names[team_b]))

        a_game_score = 0
        b_game_score = 0

        prev_a = -1
        prev_b = -1

        team_a_cont = 0
        team_b_cont = 0

        a_pattern = [0] * 10
        b_pattern = [0] * 10

        for k in range(10):
            print("<turn {}>".format(k))
            a = eval("{}(team_a, k, prev_b, last_pattern[team_b])".format(f[team_a]))
            b = eval("{}(team_b, k, prev_a, last_pattern[team_a])".format(f[team_b]))
            a_pattern[k] = a
            b_pattern[k] = b

            if a == prev_a: team_a_cont += a+1
            else: team_a_count = 0
            if b == prev_b: team_b_cont += b+1
            else: team_b_count = 0

            if a != 0 and a != 1 and a != 2: team_a_cont = 100
            if b != 0 and b != 1 and b != 2: team_b_cont = 100

            prev_a = a
            prev_b = b

            a_score = 0
            b_score = 0

            if a == DEER and b == DEER: a_score = 50; b_score = 50;
            elif a == DEER and b == RABBIT: a_score = 0; b_score = 20;
            elif a == DEER and b == SNAKE: a_score = 0; b_score = 10;
            elif a == RABBIT and b == DEER: a_score = 20; b_score = 0;
            elif a == RABBIT and b == RABBIT: a_score = 20; b_score = 20;
            elif a == RABBIT and b == SNAKE: a_score = 0; b_score = 30;
            elif a == SNAKE and b == DEER: a_score = 10; b_score = 0;
            elif a == SNAKE and b == RABBIT: a_score = 30; b_score = 0;
            elif a == SNAKE and b == SNAKE: a_score = 10; b_score = 10;

            a_score -= team_a_cont
            b_score -= team_b_cont
            a_score += random.randrange(3)
            b_score += random.randrange(3)

            a_game_score += a_score
            b_game_score += b_score


            if a == 0: print(f"[{names[team_a]}] : DEER, ",  end="")
            elif a == 1: print(f"[{names[team_a]}] : RABBIT, ", end="")
            elif a == 2: print(f"[{names[team_a]}] : SNAKE, ", end="")

            if b == 0: print(f"[{names[team_b]}] : DEER")
            elif b == 1: print(f"[{names[team_b]}] : RABBIT")
            elif b == 2: print(f"[{names[team_b]}] : SNAKE")

            print(f"[{names[team_a]}] score: This turn:{a_score}, Game socre:{a_game_score}, Total score:{total_score[team_a] + a_game_score}")
            print(f"[{names[team_b]}] score: This turn:{b_score}, Game score:{b_game_score}, Total score:{total_score[team_b] + b_game_score}")

        for z in range(10):
            last_pattern[team_a][pattern_count[team_a]][z] = a_pattern[z]
            last_pattern[team_b][pattern_count[team_b]][z] = b_pattern[z]
        pattern_count[team_a] += 1
        pattern_count[team_b] += 1

        print("<game result>")
        if a_game_score == b_game_score: print("Draw")
        else:
            print("Win : [{}]".format(names[team_a] if a_game_score > b_game_score else names[team_b]))
        print()
        total_score[team_a] += a_game_score
        total_score[team_b] += b_game_score

print("<Final score>")
max_inx = 0
max_score = 0
for i in range(f_inx):
    print(f"[{names[i]}] Total Score : {total_score[i]}")
    if max_score < total_score[i]:
        max_inx = i
        max_score = total_score[i]

print(f"<Winner : [{names[max_inx]}] !!!>")



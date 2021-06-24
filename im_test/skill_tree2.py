def pop_skill(pop_list:list, user_skill):
    # pop_list가 다 비었음 -> 스킬이 순서대로 찍힘
    cur_pos = 0
    while pop_list:
        if user_skill[cur_pos] in pop_list: # user_skill에서 내가 가리키고 있는게 pop_list에 있음
            if user_skill[cur_pos] == pop_list[0]:
                pop_list.pop(0)
            else: # 순서대로가 아님
                return 0
        cur_pos += 1
        if cur_pos > len(pop_list):
            break
    return 1

def solution(skill, skill_trees):
    # 스킬 순서 skill list
    # 유저들이 만든 스킬트리 skill_trees
    # 가능한 스킬트리 순서 return
    #print(skill, skill_trees)
    answer = 0
    # skill 을 pop하면서 알아갈거라 복사해줌
    pop_list = [letter for letter in skill]

    # pop_list의 맨 앞과 계속 글자를 비교하면서
    # 만약 list안에 있지만 맨처음이 아니라면 바로 break
    # 끝까지 순서대로 나오면 answer += 1
    for i in range(len(skill_trees)):
        answer += pop_skill(pop_list[:], skill_trees[i])
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
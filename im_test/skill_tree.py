def solution(skill, skill_trees):
    # 스킬 순서 skill list
    # 유저들이 만든 스킬트리 skill_trees
    # 가능한 스킬트리 순서 return

    answer = 0
    # skill 을 pop하면서 알아갈거라 복사해줌
    pop_list = [letter for letter in skill]

    # pop_list의 맨 앞과 계속 글자를 비교하면서
    # 만약 list안에 있지만 맨처음이 아니라면 바로 break
    # 끝까지 순서대로 나오면 answer += 1
    for i in range(len(skill_trees)):
        pop_skill = pop_list[:]
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in pop_list:
                if skill_trees[i][j] == pop_skill[0]:
                    pop_skill.pop(0)
                    # print(pop_skill)
                else:
                    break
            if pop_list == [] or j == len(skill_trees[i]) - 1:
                answer += 1
                # print(skill_trees[i])
                break

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
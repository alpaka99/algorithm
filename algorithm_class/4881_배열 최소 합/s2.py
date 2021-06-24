N = 9
level = 0
visited = [0 for _ in range(N)]
result = []
for i in range(N):
    powerset = []
    for j in range(N):
        if visited[j]:
            break
        else:
            powerset.append[j]

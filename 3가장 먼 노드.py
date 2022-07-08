def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # print(graph)
    queue = [1]
    visited[1] = 0
    while queue:
        temp = queue.pop(0)
        for g in graph[temp]:
            if visited[g] == -1:
                queue.append(g)
                visited[g] = visited[temp] + 1
        # print(queue)
        # print(visited)

    m = max(visited)
    cnt = 0
    for v in visited:
        if v == m:
            cnt += 1

    return cnt
from collections import deque

def solution(maps: list):
    Q = deque([(0, 0)])
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    maps[0][0] = 0
    visited[0][0] = 1
    N, M = len(maps), len(maps[0])

    while Q:
        x, y = Q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and maps[x+dx[i]][y+dy[i]] == 1:
                visited[x + dx[i]][y + dy[i]] = visited[x][y]+1
                Q.append((x+dx[i], y+dy[i]))
                maps[x + dx[i]][y + dy[i]] = 0
    return -1
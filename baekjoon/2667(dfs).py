import sys
import collections

input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
total = 0
houses = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global total
    total += 1
    graph[x][y] = "0"

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if graph[nx][ny] == "1":
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if graph[i][j] == "1":
            total = 0
            dfs(i, j)
            houses.append(total)

print(len(houses))
for t in sorted(houses):
    print(t)

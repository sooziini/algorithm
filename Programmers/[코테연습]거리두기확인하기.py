# 거리두기 확인하기 (2021 KAKAO 채용연계형 인턴십)

from collections import deque

def bfs(place, p_list):
    dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]
    for p in p_list:
        queue=deque([p])
        visited=[[0]*5 for _ in range(5)]
        visited[p[0]][p[1]]=1
        while queue:
            x, y, distance=queue.popleft()
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                    if place[nx][ny]=='O' and distance==0:  # 첫 'O'가 나올 경우 (두 번째 'O'의 경우 큐에 append 하지 않음)
                        queue.append([nx, ny, distance+1])
                        visited[nx][ny]=1
                    if place[nx][ny]=='P' and distance<=1:  #'P'이고 맨해튼 거리가 2 이하일 경우
                        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        p_list=[]   # 'P'에 해당하는 위치의 인덱스를 담을 배열
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    p_list.append([i, j, 0])    # 인덱스 i, 인덱스 j, 현재 위치 기준의 거리
        answer.append(bfs(place, p_list))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
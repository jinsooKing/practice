import numpy as np

def numRoutes(_map, source, destination):
    graph = {} 
    subway_count = {} 

    for i, subway in enumerate(_map):
        for j in range(len(subway) - 1):
            current_station = subway[j]
            if current_station not in graph:
                graph[current_station] = []
                subway_count[current_station] = set()
            graph[current_station].append(subway[j + 1])
            subway_count[current_station].add(i)

        first_station = subway[0]
        last_station = subway[-1]
        if last_station not in graph:
            graph[last_station] = []
            subway_count[last_station] = set()
        graph[last_station].append(first_station)
        subway_count[last_station].add(i)

    # 거리, 이전 역, 사용된 지하철 노선
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    prev = {node: None for node in graph}
    subway = {node: set() for node in graph}

    # 벨만 포드
    for _ in range(len(_map) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[u] != float('inf') and dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    subway[v] = subway[u].union(subway_count[v])

    # source -> destination 까지 path가 없으면 -1
    if dist[destination] == float('inf'):
        return -1
    else: # 있으면 사용된 지하철 개수 계산하고 출력
        num_subway = len(subway[destination])
        return str(num_subway)

if __name__ == "__main__":
    _map = [[1,2,7],[3,6,7]]
    source1 = 1
    destination1 = 6
    
    _map2 = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    source2 = 15
    destination2 = 12
    
    result1 = numRoutes(_map, source1, destination1)
    result2 = numRoutes(_map2, source2, destination2)
    print(f"{_map}이 이용한 지하철의 개수는 {result1}개 입니다.")
    print(f"{_map2}이 이용한 지하철의 개수는 {result2}개 입니다.")
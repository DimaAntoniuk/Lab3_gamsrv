from queue import PriorityQueue
import heapq
#const that is bigger than biggest edge
INF = 10**9 + 1

with open('input.txt', 'r') as input:
    nodes, edges = map(int, input.readline().split())
    graph = []
    for node in range(nodes):
        graph.append([])
    clients = set(map(lambda x: int(x) - 1, input.readline().split()))

    for edge in range(edges):
        node1, node2, weight = map(int, input.readline().split())
        node1 -= 1
        node2 -= 1
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))


def dijkstra(start):
    global max_dist
    global clients
    hq = []
    d = [-1]*nodes
    d[start] = 0
    heapq.heappush(hq, (0, start))
    while len(hq)>0:
        cur_dist, cur_node = heapq.heappop(hq)
        for index in range(len(graph[cur_node])):
            to = graph[cur_node][index][0]
            dist = graph[cur_node][index][1]
            if(d[to] == -1 or d[to] > dist + d[cur_node]):
                d[to] = dist + d[cur_node]
                heapq.heappush(hq, (d[to], to))
    for d_i in range(len(d)):
        if d_i in clients and (max_dist[start] == -1 or max_dist[start] < d[d_i]):
            max_dist[start] = d[d_i]


max_dist = [-1]* nodes
server_node = -1

for node in range(nodes):
    if not node in clients:
        dijkstra(node)

min = max_dist[0]
server_node = 1

for node in range(nodes):
    if min == -1:
        min = max_dist[node]
        server_node = node + 1
    elif max_dist[node] != -1 and max_dist[node] < min:
        server_node = node + 1
        min = max_dist[node]

with open('output.txt', 'w+') as output:
    output.write(str(min))

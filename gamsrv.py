import sortedcollections
with open('input.txt', 'r') as input:
    line = input.readline().split()
    nodes = int(line[0])
    edges = int(line[1])
    graph = []
    for node in range(nodes):
        graph.append([])
    line = input.readline().split()
    clients = set()
    for client in line:
        clients.add(int(client)-1)

    for edge in range(edges):
        line = input.readline().split()
        node1 = int(line[0]) - 1
        node2 = int(line[1]) - 1
        weight = int(line[2])
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))


def dextra(start):
    global max_dist
    d = [10 ** 9] * nodes
    d[start] = 0
    used = [False] * nodes
    for i in range(nodes):
        vertex = -1
        for j in range(nodes):
            if  not used[j] and (vertex==-1 or d[j]<d[vertex]):
                vertex = j
        if(d[vertex] == 10**9):
            break;
        used[vertex] = True
        for to, len in graph[vertex]:
            if(d[vertex] + len < d[to]):
                d[to] = d[vertex] + len
    for node in range(nodes):
        if node in clients and max_dist[start] < d[node]:
            max_dist[start] = d[node]

max_dist = [-1]* nodes
server_node = -1
min = 10 ** 9
def main():
    global min
    global server_node
    global max_dist
    global nodes
    global clients
    for node in range(nodes):
        if not node in clients:
            dextra(node)

    for node in range(nodes):
        if max_dist[node] != -1 and max_dist[node] < min:
            server_node = node
            min = max_dist[node]

main()

with open('output.txt', 'a+') as output:
    output.write("nodes:" + str(nodes) + '\n')
    output.write("edges:" + str(edges) + '\n')
    output.write("clients:" + str(clients) + '\n')
    output.write("graph:\n")
    for node in range(nodes):
        output.write(str(graph[node]))
        output.write('\n')
    output.write(str(min) + ' ' + str(server_node+1) + '\n')

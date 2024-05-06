import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = {i: {} for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.adjList[u][v] = weight

    def dijkstra(self, start):
        distances = {node: float('inf') for node in range(self.vertices)}
        distances[start] = 0
        minH = [[0, start]]

        while minH:
            current_distance, current_node = heapq.heappop(minH)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adjList[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(minH, [distance, neighbor])

        return distances

# Get input from the user
vertices = int(input("Enter the number of vertices in the graph: "))
g = Graph(vertices)

edges = int(input("Enter the number of edges in the graph: "))
for _ in range(edges):
    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
    g.add_edge(u, v, weight)

start_node = int(input("Enter the starting node: "))

print("Shortest distances from node", start_node, "to other nodes:")
print(g.dijkstra(start_node))

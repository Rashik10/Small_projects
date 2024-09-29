#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>

using namespace std;

// Structure to represent an edge in the graph
struct Edge {
    int to, weight;
};

// Custom comparator for the priority queue to sort by distance
class Compare {
public:
    bool operator()(pair<int, int>& p1, pair<int, int>& p2) {
        return p1.second > p2.second; // Sort based on distance (second value in pair)
    }
};

// Dijkstra's algorithm to find the shortest paths from the source node
void dijkstra(int src, int V, vector<vector<Edge>>& graph) {
    // Initialize distance array with infinity
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;

    // Priority queue to store (node, distance) and sort by distance
    priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;
    pq.push({src, 0});

    // Dijkstra's algorithm loop
    while (!pq.empty()) {
        int u = pq.top().first;
        pq.pop();

        // Explore neighbors of node u
        for (Edge& edge : graph[u]) {
            int v = edge.to;
            int weight = edge.weight;

            // Relaxation step: check if we can find a shorter path to node v
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({v, dist[v]}); // Push the updated distance into the priority queue
            }
        }
    }

    // Print the shortest distances from the source
    cout << "Vertex \t Distance from Source " << src << endl;
    for (int i = 0; i < V; ++i) {
        cout << i << " \t\t " << dist[i] << endl;
    }
}

int main() {
    int V = 9; // Number of vertices in the graph

    // Graph represented as an adjacency list
    vector<vector<Edge>> graph(V);

    // Add edges to the graph
    // Node 0
    graph[0].push_back({1, 4});
    graph[0].push_back({7, 8});

    // Node 1
    graph[1].push_back({0, 4});
    graph[1].push_back({2, 8});
    graph[1].push_back({7, 11});

    // Node 2
    graph[2].push_back({1, 8});
    graph[2].push_back({3, 7});
    graph[2].push_back({5, 4});
    graph[2].push_back({8, 2});

    // Node 3
    graph[3].push_back({2, 7});
    graph[3].push_back({4, 9});
    graph[3].push_back({5, 14});

    // Node 4
    graph[4].push_back({3, 9});
    graph[4].push_back({5, 10});

    // Node 5
    graph[5].push_back({2, 4});
    graph[5].push_back({3, 14});
    graph[5].push_back({4, 10});
    graph[5].push_back({6, 2});

    // Node 6
    graph[6].push_back({5, 2});
    graph[6].push_back({7, 1});
    graph[6].push_back({8, 6});

    // Node 7
    graph[7].push_back({0, 8});
    graph[7].push_back({1, 11});
    graph[7].push_back({6, 1});
    graph[7].push_back({8, 7});

    // Node 8
    graph[8].push_back({2, 2});
    graph[8].push_back({6, 6});
    graph[8].push_back({7, 7});

    // Run Dijkstra's algorithm from the source node 0
    dijkstra(0, V, graph);

    return 0;
}


// g++ Dijkstra_Algorithm.cpp -o Dijkstra_Algorithm
// Dijkstra_Algorithm
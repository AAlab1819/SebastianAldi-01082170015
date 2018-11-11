#include <bits/stdc++.h>

using namespace std;
bool visited[500];
int distanceToSource[500];
int adjMatrix[500][500];
int n, m, u;
void BFS(bool train)
{
    for(int i = 0; i < 500; i++)
    {
        distanceToSource[i] = INT_MAX;
        visited[i] = false;
    }
    queue <int> q;
    q.push(1);
    visited[1] = true;
    distanceToSource[1] = 0;
    while(!q.empty())
    {
        u = q.front();
        q.pop();
        for(int i = 1; i <= n; i++)
        {
            if(train)
            {
                if(adjMatrix[u][i] == 1 && visited[i] == false)
                {
                    q.push(i);
                    visited[i] = true;
                    distanceToSource[i] = distanceToSource[u] + 1;
                    if(i == n) return;
                }
            } else {
                if(adjMatrix[u][i] == 0 && visited[i] == false)
                {
                    q.push(i);
                    visited[i] = true;
                    distanceToSource[i] = distanceToSource[u] + 1;
                    if(i == n) return;
                }
            }
        }
    }
}
int main()
{
    int u, v, train = 0, bus = 0;
    cin >> n >> m;
    memset(adjMatrix, 0, sizeof(adjMatrix));
    for(int i = 0; i < m; i++)
    {
        cin >> u >> v;
        adjMatrix[u][v] = 1;
        adjMatrix[v][u] = 1;
    }
    if(adjMatrix[1][n] == 1)
        train = 1;
    else
        bus = 1;
    if(train)
    {
        BFS(false);
        bus = distanceToSource[n];
    } else {
        BFS(true);
        train = distanceToSource[n];
    }
    int answer = max(bus, train);
    if(answer == INT_MAX)
        cout << -1;
    else cout << answer;
    return 0;
}

#include <bits/stdc++.h>
#define ll long long

using namespace std;
const int N = 1e5 + 5;
int n, m, a, b, w;
vector<pair<int,int>> graph[N];
int source[N];
ll shortestDistance[N] = {0};
bool visited[N] = {0};
void dijkstra(int startingPoint)
{
    typedef tuple<ll, int, int> path;
    ll cost;
    int destination, previous;
    priority_queue<path, vector<path>, greater<path>> q;
    q.push(make_tuple(0, startingPoint, -1));
    while(!q.empty())
    {
        path now = q.top();
        q.pop();
        cost = get<0>(now);
        previous = get<2>(now);
        destination = get<1>(now);
        if(visited[destination])
            continue;
        else {
            visited[destination] = true;
            source[destination] = previous;
            for(int i = 0; i < graph[destination].size(); i++)
            {
                if(visited[graph[destination][i].first] == false)
                    q.push(make_tuple(cost + graph[destination][i].second, graph[destination][i].first, destination));
            }
        }
    }
}
void printPath(int destination)
{
    if(source[destination] == -1)
        cout << -1;
    else {
        stack <int> vertex;
        while(destination > 0)
        {
            vertex.push(destination);
            destination = source[destination];
        }
        while(!vertex.empty())
        {
            cout << vertex.top() << " ";
            vertex.pop();
        }
    }
}
int main()
{
    cin >> n >> m;
    for(int i = 0; i < N; i++)
        source[i] = -1;
    while(m--)
    {
        cin >> a >> b >> w;
        graph[a].push_back(make_pair(b, w));
        graph[b].push_back(make_pair(a, w));
    }
    dijkstra(1);
    printPath(n);
    return 0;
}

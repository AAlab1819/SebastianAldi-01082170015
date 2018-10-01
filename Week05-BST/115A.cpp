#include <bits/stdc++.h>

using namespace std;

int main()
{
    map <int, int> superior;
    int employees, manager, depth, check, ans = 0;
    cin >> employees;
    for(int i = 1; i <= employees; i++)
    {
        cin >> manager;
        superior[i] = manager;
    }
    for(int i = 1; i <= employees; i++)
    {
        depth = 1;
        check = superior[i];
        while(check != -1)
        {
            depth++;
            check = superior[check];
        }
        ans = max(depth, ans);
    }
    cout << ans;
    return 0;
}

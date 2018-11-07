#include <bits/stdc++.h>
#define forn(n) for(int i = 0; i < n; i++)
using namespace std;
int objectWeight[1001] = {0},
    objectWorth[1001] = {0};
int main()
{
    int testCases, objects, members, member, ans;
    cin >> testCases;
    while(testCases--)
    {
        int dpTable[31] = {0};
        ans = 0;
        cin >> objects;
        forn(objects)
            cin >> objectWorth[i] >> objectWeight[i];
        forn(objects)
            for(int j = 30; j >= 0; j--)
            {
                if(objectWeight[i] <= j)
                {
                    dpTable[j] = max(dpTable[j], objectWorth[i] + dpTable[j - objectWeight[i]]);
                }
            }
        cin >> members;
        forn(members)
        {
            cin >> member;
            ans += dpTable[member];
        }
        cout << ans << endl;
    }
    return 0;
}

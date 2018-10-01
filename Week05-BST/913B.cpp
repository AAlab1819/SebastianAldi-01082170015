#include <bits/stdc++.h>

using namespace std;

int main()
{
    int vertices, parent, leafCount;
    cin >> vertices;
    map <int, vector <int> > tree;
    bool spruce = true;
    for(int i = 2; i <= vertices; i++)
    {
        cin >> parent;
        tree[parent].push_back(i);
    }
    for(int i = 1; i <= vertices; i++)
    {
        if(tree[i].size() == 0) continue;
        else {
            leafCount = 0;
            for(int j = 0 ; j < tree[i].size(); j++)
            {
                if(tree[tree[i][j]].size() == 0)
                    leafCount++;
            }
            if(leafCount < 3)
                spruce = false;
        }
    }
    if(spruce)
        cout << "Yes";
    else
        cout << "No";
    return 0;
}

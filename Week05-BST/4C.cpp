#include <bits/stdc++.h>

using namespace std;

int main()
{
    map <string, int> username;
    int n; cin >> n;
    string name;
    while(n>0)
    {
        cin >> name;
        if(username[name] == 0)
        {
            username[name] = 1;
            cout << "OK" << endl;
        } else {
            cout << name << username[name] << endl;
            username[name]++;
        }
        n--;
    }
    return 0;
}
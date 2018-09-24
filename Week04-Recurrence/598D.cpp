#include <bits/stdc++.h>

using namespace std;

int ans = 0;
int keyCounter = 0;
char museum[1000][1000];
int answer[1000000] = {0};
int key[1000][1000] = {0};
int maxRow, maxCol;
void floodfill(int row, int col)
{
    if(row < 0 || row >= maxRow || col < 0 || col >= maxCol) return;
    if(key[row][col] != 0) return;
    if(museum[row][col] == '*')
    {
        ans++;
        return;
    }
    key[row][col] = keyCounter;
    floodfill(row-1, col);
    floodfill(row+1, col);
    floodfill(row, col-1);
    floodfill(row, col+1);
    return;
}
int main()
{
    int testCase, testRow, testCol;
    cin >> maxRow >> maxCol >> testCase;
    for(int i = 0; i < maxRow; i++)
    {
        for(int j = 0; j < maxCol; j++)
        {
            cin >> museum[i][j];
        }
    }
    for(int i = 0; i < maxRow; i++)
    {
        for(int j = 0; j < maxCol; j++)
        {
            if(museum[i][j] == '.' && key[i][j] == 0)
            {
                keyCounter++;
                ans = 0;
                floodfill(i,j);
                answer[keyCounter] = ans;
            }
        }
    }
    for(int x = 0; x < testCase; x++)
    {
        cin >> testRow >> testCol;
        cout << answer[key[testRow-1][testCol-1]] << endl;
    }
    return 0;
}

#include <iostream>
#include <vector>
using namespace std;

vector<string> cavityMap(const vector<string> &grid)
{
    vector<string> res = grid;

    for (int i = 1; i < res.size() - 1; i++)
    {
        for (int j = 1; j < res[i].length() - 1; j++)
        {
            int current = static_cast<int>(res[i][j]);
            int up = static_cast<int>(res[i - 1][j]);
            int down = static_cast<int>(res[i + 1][j]);
            int left = static_cast<int>(res[i][j - 1]);
            int right = static_cast<int>(res[i][j + 1]);

            if (current > up && current > down && current > left && current > right)
                res[i][j] = 'X';
        }
    }

    return res;
}

int main()
{
    int n;
    cin >> n;
    vector<string> grid(n);
    for (string &str : grid)
        cin >> str;

    vector<string> result(cavityMap(grid));
    for (const string &str : result)
        cout << str << '\n';

    return 0;
}

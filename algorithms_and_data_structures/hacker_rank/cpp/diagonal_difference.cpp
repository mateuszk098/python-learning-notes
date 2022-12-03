#include <iostream>
#include <vector>
using namespace std;

int diagonalDifference(const vector<vector<int>> &v)
{
    int r_to_l = 0, l_to_r = 0;

    for (int i = 0; i < v.size(); i++)
        for (int j = 0; j < v[i].size(); j++)
        {
            if (i == j)
            {
                r_to_l += v[i][j];
                l_to_r += v[v.size() - 1 - i][j];
            }
        }

    return abs(r_to_l - l_to_r);
}

int main()
{
    vector<vector<int>> v;
    int n, tmp;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        v.push_back(vector<int>());

        for (int j = 0; j < n; j++)
        {
            cin >> tmp;
            v[i].push_back(tmp);
        }
    }

    cout << diagonalDifference(v) << '\n';
    return 0;
}

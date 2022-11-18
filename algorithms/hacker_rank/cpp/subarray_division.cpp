#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int birthday(const vector<int> &s, const int &d, const int &m)
{
    int ways = 0;

    for (int i = 0; i <= s.size() - m; i++)
        if (accumulate(s.begin() + i, s.begin() + i + m, 0) == d)
            ways++;

    return ways;
}

int main()
{
    int n, d, m;
    cin >> n;
    vector<int> v(n);

    for (auto &val : v)
        cin >> val;

    cin >> d >> m;
    cout << birthday(v, d, m) << '\n';

    return 0;
}

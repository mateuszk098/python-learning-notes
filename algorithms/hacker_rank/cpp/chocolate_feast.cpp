#include <iostream>
#include <vector>
using namespace std;

int chocolateFeast(const int &n, const int &c, const int &m)
{
    int bars = n / c;
    int wrapper = bars;
    int remainder = 0;

    while (wrapper >= m)
    {
        remainder = wrapper / m;
        bars = bars + remainder;
        remainder = remainder + wrapper % m;
        wrapper = remainder;
    }

    return bars;

    // int bars = n / c;
    // return bars + (bars-1) / (m-1);
}

int main()
{
    int t, n, c, m;
    cin >> t;

    vector<int> v;
    for (int i = 0; i < t; i++)
    {
        cin >> n >> c >> m;
        v.push_back(chocolateFeast(n, c, m));
    }

    for (const int &val : v)
        cout << val << '\n';

    return 0;
}

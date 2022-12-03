#include <iostream>
#include <vector>
using namespace std;

void countApplesAndOranges(const int &s, const int &t, const int &a, int const &b, vector<int> apples, vector<int> oranges)
{
    int a_count = 0;
    int o_count = 0;

    for (int i = 0; i < apples.size(); i++)
    {
        apples.at(i) += a;

        if (s <= apples.at(i) && apples.at(i) <= t)
            a_count++;
    }

    for (int i = 0; i < oranges.size(); i++)
    {
        oranges.at(i) += b;

        if (s <= oranges.at(i) && oranges.at(i) <= t)
            o_count++;
    }

    cout << a_count << '\n';
    cout << o_count << '\n';
}

int main()
{
    int s, t, a, b, m, n, tmp;
    vector<int> apples, oranges;
    cin >> s >> t >> a >> b >> m >> n;

    for (int i = 0; i < m; i++)
    {
        cin >> tmp;
        apples.push_back(tmp);
    }

    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        oranges.push_back(tmp);
    }

    countApplesAndOranges(s, t, a, b, apples, oranges);

    return 0;
}
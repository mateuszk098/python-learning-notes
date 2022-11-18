#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minimumDistances(const vector<int> &a)
{
    vector<int> pairs;

    for (int i = 0; i < a.size(); i++)
        for (int j = i; j < a.size() - 1; j++)
            if (a.at(i) == a.at(j + 1))
                pairs.push_back(j + 1 - i);

    if (pairs.size() > 0)
        return *min_element(pairs.begin(), pairs.end());

    return -1;
}

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &val : a)
        cin >> val;

    cout << minimumDistances(a) << '\n';
    return 0;
}
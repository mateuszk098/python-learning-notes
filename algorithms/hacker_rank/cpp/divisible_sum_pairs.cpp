#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int divisibleSumPairs(const int &n, const int &k, const vector<int> &ar)
{
    int pairs = 0;

    for (int i = 0; i < ar.size(); i++)
        for (int j = 0; j < ar.size(); j++)
            if (i < j && (ar.at(i) + ar.at(j)) % k == 0)
                pairs++;

    return pairs;
}

int main()
{
    int n, k;
    cin >> n >> k;
    vector<int> v(n);

    for (int &val : v)
        cin >> val;

    cout << divisibleSumPairs(n, k, v) << '\n';

    return 0;
}
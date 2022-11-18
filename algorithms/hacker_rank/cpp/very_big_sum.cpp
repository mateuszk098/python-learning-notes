#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

inline long long aVeryBigSum(const vector<long> &v)
{
    return (long long)accumulate(v.begin(), v.end(), 0ll);
}

int main()
{
    vector<long> v;
    long tmp;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }

    cout << aVeryBigSum(v) << '\n';

    return 0;
}

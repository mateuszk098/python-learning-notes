#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int birthdayCakeCandles(const vector<int> &v)
{
    if (v.size() == 0)
        return -1;

    int max = *max_element(v.begin(), v.end());
    int counts = count(v.begin(), v.end(), max);
    return counts;
}

int main()
{
    int n, tmp;
    vector<int> v;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }

    cout << birthdayCakeCandles(v);

    return 0;
}
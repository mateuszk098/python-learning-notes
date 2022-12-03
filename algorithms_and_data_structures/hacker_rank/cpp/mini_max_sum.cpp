#include <iostream>
#include <numeric>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;

void miniMaxSum(const vector<int> &v)
{
    long long sum = accumulate(v.begin(), v.end(), 0ll);
    vector<long long> vtmp;

    for (int i = 0; i < v.size(); i++)
    {
        vtmp.push_back(sum - v.at(i));
    }

    long long vmin = *min_element(vtmp.begin(), vtmp.end());
    long long vmax = *max_element(vtmp.begin(), vtmp.end());

    cout << vmin << ' ' << vmax << '\n';
}

int main()
{
    vector<int> v;
    int tmp;
    string line;
    getline(cin, line);
    stringstream ss(line);

    while (ss >> tmp)
        v.push_back(tmp);

    miniMaxSum(v);

    return 0;
}

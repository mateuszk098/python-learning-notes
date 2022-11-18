#include <iostream>
#include <vector>
using namespace std;

vector<int> circularArrayRotation(vector<int> v, const int &k, const vector<int> &queries)
{
    int tmp = 0;
    vector<int> v_tmp;

    for (int i = 0; i < k; i++)
    {
        tmp = v.back();
        v.pop_back();
        v.insert(v.begin(), tmp);
    }

    for (int i = 0; i < queries.size(); i++)
        v_tmp.push_back(v.at(queries.at(i)));

    return v_tmp;
}

int main()
{
    int n, k, q, tmp;
    cin >> n >> k >> q;
    vector<int> v(n), queries(q);

    for (int &tmp : v)
        cin >> tmp;

    for (int &tmp : queries)
        cin >> tmp;

    vector<int> result = circularArrayRotation(v, k, queries);
    for (const auto &val : result)
        cout << val << '\n';

    return 0;
}
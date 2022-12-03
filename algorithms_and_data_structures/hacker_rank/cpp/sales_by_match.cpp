#include <iostream>
#include <vector>
#include <map>
using namespace std;

int sockMerchant(const int &n, const vector<int> &v)
{
    map<int, int> pairs;
    int count = 0;

    for (const int &value : v)
        ++pairs[value];

    // Zlicz ile mamy par (calkowie dzielenie przez 2) dla wartosci spod klucza mapy
    for (const auto &[key, value] : pairs)
        count += value / 2;

    // for (const auto &[key, value] : pairs)
    // {
    //     std::cout << '[' << key << "] = " << value << "; ";
    // }

    return count;
}

int main()
{
    int n;
    cin >> n;
    vector<int> v(n);

    for (int &val : v)
        cin >> val;

    cout << sockMerchant(n, v) << '\n';

    return 0;
}

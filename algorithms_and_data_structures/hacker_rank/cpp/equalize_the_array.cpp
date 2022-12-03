#include <iostream>
#include <map>
#include <vector>
using namespace std;

int equalizeArray(const vector<int> &arr)
{

    map<int, int> hash;
    int mostFrequent;

    for (const int &value : arr)
        ++hash[value];

    int mostFrequentCounts = 0;
    for (const auto &[key, value] : hash)
        if (mostFrequentCounts < value)
            mostFrequentCounts = value;

    return arr.size() - mostFrequentCounts;
}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int &val : arr)
        cin >> val;

    cout << equalizeArray(arr) << '\n';
    return 0;
}

#include <iostream>
#include <vector>
using namespace std;

vector<int> missingNumbers(vector<int> arr, vector<int> brr)
{
    const int SIZE = 10001;
    vector<int> v(SIZE, 0);

    for (int i = 0; i < arr.size(); i++)
    {
        int val = arr[i];
        --v[val];
    }

    for (int i = 0; i < brr.size(); i++)
    {
        int val = brr[i];
        ++v[val];
    }

    vector<int> missing;

    for (int i = 0; i < SIZE; i++)
    {
        if (v[i] > 0)
            missing.push_back(i);
    }

    return missing;
}

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int &v : arr)
        cin >> v;

    int m;
    cin >> m;
    vector<int> brr(m);
    for (int &v : brr)
        cin >> v;

    vector<int> result(missingNumbers(arr, brr));
    for (const int &v : result)
        cout << v << ' ';

    return 0;
}
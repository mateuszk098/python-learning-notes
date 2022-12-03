#include <iostream>
#include <vector>
using namespace std;

int workbook(int n, int k, vector<int> arr)
{
    int page = 1;
    int special = 0;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= arr[i - 1]; j++)
        {
            if (j == page)
                ++special;

            if (j % k == 0 || j == arr[i - 1])
                ++page;
        }
    }

    return special;
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> arr(n);
    for (int &val : arr)
        cin >> val;

    cout << workbook(n, k, arr) << '\n';
    return 0;
}
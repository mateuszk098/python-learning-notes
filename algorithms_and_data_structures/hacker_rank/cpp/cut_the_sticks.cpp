#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> cutTheSticks(vector<int> arr)
{
    vector<int> cuts;
    int n = arr.size();
    sort(arr.begin(), arr.end());

    // Przy posortowanej tablicy, mozemy myslec jako o obcinaniu stickow
    // jak przy przechodzeniu przez nia i patrzeniu gdzie zmienia sie liczba
    // w tablicy. Jezeli na danym indeksie sie zmienia to musimy uciac n - index razy
    cuts.push_back(n);
    for (int i = 1; i < n; i++)
    {
        if (arr.at(i - 1) != arr.at(i))
            cuts.push_back(n - i);
    }
    return cuts;
}

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);

    for (int &val : arr)
        cin >> val;

    vector<int> out{cutTheSticks(arr)};
    for (const int &val : out)
        cout << val << '\n';

    return 0;
}
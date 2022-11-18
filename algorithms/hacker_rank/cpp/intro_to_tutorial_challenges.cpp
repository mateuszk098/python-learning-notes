#include <iostream>
#include <vector>
using namespace std;

int introTutorial(const int &V, vector<int> &arr)
{
    vector<int>::iterator itr = find(arr.begin(), arr.end(), V);
    return distance(arr.begin(), itr);
}

int main()
{
    int V, n;
    cin >> V >> n;
    vector<int> v(n);

    for (int &val : v)
        cin >> val;

    cout << introTutorial(V, v);
}
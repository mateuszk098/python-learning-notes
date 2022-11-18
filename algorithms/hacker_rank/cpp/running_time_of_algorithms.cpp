#include <iostream>
#include <vector>
using namespace std;

void insertionSort(const int &N, vector<int> &v)
{
    int i, j, value, shifts = 0;

    for (i = 1; i < N; i++)
    {
        value = v.at(i);
        j = i - 1;

        while (j >= 0 && value < v.at(j))
        {
            v.at(j + 1) = v.at(j);
            j = j - 1;
            v.at(j + 1) = value;
            ++shifts;
        }
    }

    cout << shifts;
}
int main(void)
{
    int N;
    cin >> N;
    vector<int> v(N);

    for (int &val : v)
        cin >> val;

    insertionSort(N, v);

    return 0;
}
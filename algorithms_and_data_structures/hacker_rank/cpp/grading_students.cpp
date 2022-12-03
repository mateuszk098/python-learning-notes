#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> gradingStudents(vector<int> &v)
{
    int nearest_multiple = 0;

    for (int i = 0; i < v.size(); i++)
    {
        if (v.at(i) >= 38)
        {
            nearest_multiple = 5 * round(v.at(i) / 5.);

            if (v.at(i) < nearest_multiple && abs(nearest_multiple - v.at(i)) < 3)
                v.at(i) = nearest_multiple;
        }
    }

    return v;
}

int main()
{
    vector<int> v;
    int n, tmp;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }

    v = gradingStudents(v);

    for (const auto &val : v)
        cout << val << '\n';

    return 0;
}
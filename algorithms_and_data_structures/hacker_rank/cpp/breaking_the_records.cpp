#include <iostream>
#include <vector>
using namespace std;

vector<int> breakingRecords(const vector<int> &scores)
{
    vector<int> v(2, 0);
    int most = 0, least = 0;
    int max_score = scores.at(0);
    int min_score = scores.at(0);

    for (int i = 1; i < scores.size(); i++)
    {
        if (scores.at(i) > max_score)
        {
            max_score = scores.at(i);
            most++;
        }
        else if (scores.at(i) < min_score)
        {
            min_score = scores.at(i);
            least++;
        }
    }

    v.at(0) = most;
    v.at(1) = least;

    return v;
}

int main()
{
    int n;
    cin >> n;
    vector<int> scores(n);

    for (int &val : scores)
        cin >> val;

    vector<int> result = breakingRecords(scores);
    for (const int &val : result)
        cout << val << ' ';

    return 0;
}

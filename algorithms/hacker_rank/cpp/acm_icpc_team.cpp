#include <iostream>
#include <vector>
using namespace std;

/*
 * Complete the 'acmTeam' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING_ARRAY topic as parameter.
 */

vector<int> acmTeam(const vector<string> &topic)
{
    vector<int> result(2, 0);
    unsigned int size = topic.size();
    unsigned int len = topic.back().length();
    unsigned int known = 0;
    unsigned int maxKnown = 0;
    unsigned int teams = 0;

    for (int i = 0; i < size - 1; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            for (int k = 0; k < len; k++)
                if (topic[i][k] == '1' || topic[j][k] == '1')
                    ++known;

            if (maxKnown < known)
            {
                maxKnown = known;
                teams = 0;
            }
            
            if (maxKnown == known)
                ++teams;

            known = 0;
        }
    }

    result[0] = maxKnown;
    result[1] = teams;

    return result;
}

int main()
{
    int n, m;
    cin >> n >> m;

    vector<string> topic(n);
    for (string &s : topic)
        cin >> s;

    vector<int> result = acmTeam(topic);

    for (const int &v : result)
        cout << v << '\n';

    return 0;
}

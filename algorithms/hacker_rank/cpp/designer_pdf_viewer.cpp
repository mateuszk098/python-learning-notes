#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <algorithm>
using namespace std;

int designerPdfViewer(const vector<int> &h, const string &word)
{
    vector<char> letters{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'u', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    vector<int> found_h;
    vector<char>::iterator itr;
    int index;

    for (const char &c : word)
    {
        itr = find(letters.begin(), letters.end(), c); // find iterator indicate to letter
        index = distance(letters.begin(), itr);        // calculate index of it
        found_h.push_back(h.at(index));                // save height value of that letter
    }

    int max_val = *max_element(found_h.begin(), found_h.end());
    return max_val * found_h.size();
}

int main()
{
    vector<int> h(26);
    string word;

    for (int &val : h)
        cin >> val;
    cin >> word;

    cout << designerPdfViewer(h, word) << '\n';

    return 0;
}
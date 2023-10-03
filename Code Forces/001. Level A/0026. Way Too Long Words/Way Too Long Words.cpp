#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int main()
{
    int number_of_words = 0;

    cin >> number_of_words;
    cin.ignore();

    vector<string> strs;
    for (int i = 0; i < number_of_words; i++)
    {
        string line;

        getline(cin, line);

        strs.push_back(line);
    }

    for (int i = 0; i < number_of_words; i++)
    {

        string item = strs.at(i);

        if (item.length() <= 10)
        {
            cout << item << endl;
        }
        else
        {
            int item_length = item.length();

            int last_char_index = item_length - 1;
            char last_char = item[last_char_index];

            cout << item[0] << item_length - 2 << last_char << endl;
        }
    }

    return 0;
}

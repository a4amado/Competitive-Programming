
#include <iostream>

#include <cstring>

using namespace std;

int main()
{

    string line;
    getline(cin, line);

    int *uniqie = new int[(122 - 97) +1];

    char *c_str = new char[line.length() + 1];
    strcpy(c_str, line.c_str());

    int count = 0;

    for (int i = 0; i < (int)(line.length() - 1); i++)
    {
        int char_ascii = (int)c_str[i];

        if (char_ascii <= 122 && char_ascii >= 97)
        {
            int char_index = char_ascii - 97;

            if (uniqie[char_index] != 1)
            {
                count++;
                uniqie[char_index] = 1;
            }
        }
    }
    delete[] c_str;
    delete[] uniqie;
    cout << count << endl;
    return 0;
}
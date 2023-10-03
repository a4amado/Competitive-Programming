#include <iostream>

using namespace std;

int main()
{
    int s[4];
    cin >> s[0] >> s[1] >> s[2] >> s[3];


    int num = 0;

    for (int i = 0; i < 3; i++) {
        bool is_unique = false;

        for (int j = i + 1; j < 4;j++) {
            if (s[i] == s[j]) {
                is_unique = true;
                break;
            }
        }

    if (is_unique) {
        num++;
    }
    }
                cout << num << endl;
return 0;
}
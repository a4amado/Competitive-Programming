#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char a[] = "a b c d e f";
    char dit[] = " ";

    char* token;

    token = strtok_s(a, dit);

    cout << token << endl;

    strtok(NULL, dit);
    token = strtok(a, dit);

    cout << token << endl;
    return 0;
}
/**
 * Name: Black Square
 * Link: https://codeforces.com/contest/431/problem/A
 */
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

void removeSpaces(char *str);

int main()
{

    vector<int> calories;
    string calories_string;
    getline(cin, calories_string);

    int c_length = calories_string.length() + 1;
    char *c = new char[c_length];
    strcpy(c, calories_string.c_str());

    char det[] = " ";
    char *token;
    token = strtok(c, det);

    while (token != NULL)
    {
        calories.push_back(atoi(token));
        token = strtok(NULL, det);
    }

    string touches_string;
    getline(cin, touches_string);

    int max = 0;
    for (int i = 0; i < touches_string.length() ; i++)
    {
        int index = static_cast<int>(touches_string[i] - '0') - 1;
        max += calories.at(index);
    }

    cout << max << endl;
    return 0;
}

void removeSpaces(char *str)
{

    int count = 0;

    for (int i = 0; str[i]; i++)
    {
        if (str[i] != ' ')
        {
            str[count] = str[i];
            count++;
        }
    }
    str[count] = '\0';
}
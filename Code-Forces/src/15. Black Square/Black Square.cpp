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

    char calories_string;
    getline(cin, calories_string);

    char det[] = " ";

    char *token;
    token = strtok(calories_string, det);

    string touches_string;
    getline(cin, touches_string);

    int total_wasted_calories = 0;

    for (int i = 0; i < touches_string.length(); i++)
    {

        int calorie_value = static_cast<int>(cstr[static_cast<int>(touches_string[i] - '0') - 1] - '0');

        total_wasted_calories += calorie_value;
    };

    cout << total_wasted_calories << endl;
    delete[] cstr;

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
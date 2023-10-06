#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>

using namespace std;

struct Student
{
    int64_t index;
};

struct Team
{
    Student programming;
    Student maths;
    Student PE;
};

int main()
{
    int64_t number_of_students;
    cin >> number_of_students;
    vector<Team> teams;

    vector<Student> number_of_programming;
    vector<Student> number_of_maths;

    vector<Student> PE;

    for (int64_t i = 0; i < number_of_students; i++)
    {
        int num;
        cin >> num;

        Student s;
        s.index = i + 1; // Correct index assignment

        if (num == 1)
        {
            number_of_programming.push_back(s);
        }
        else if (num == 2)
        {
            number_of_maths.push_back(s);
        }
        else if (num == 3)
        {
            PE.push_back(s);
        }
    }

    while (!number_of_maths.empty() && !number_of_programming.empty() && !PE.empty())
    {
        Team team;
        Student s_m = number_of_maths.back();
        team.maths = s_m;
        number_of_maths.pop_back();

        Student s_p = number_of_programming.back();
        team.programming = s_p;

        number_of_programming.pop_back();

        Student s_e = PE.back();
        team.PE = s_e;
        PE.pop_back();

        teams.push_back(team);
    }

    cout << teams.size() << endl;
    for (int i = 0; i < teams.size(); i++)
    {
        cout << teams.at(i).programming.index << " " << teams.at(i).maths.index << " " << teams.at(i).PE.index << endl;
    }

    return 0;
}
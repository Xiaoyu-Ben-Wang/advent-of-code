#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int solveP1();
int solveP2();
int main()
{
    cout <<"Part 1 Answer: "<< solveP1()<<endl;
    cout << "Part 2 Answer: " <<solveP2() << endl;
    return 0;
}

int solveP1()
{
    int total = 0;

    fstream f("2020day2.txt");
    if (f.is_open())
    {
        string line;
        while (getline(f, line))
        {
            string limits, key, password;
            int lower, higher;
            stringstream ss(line);
            getline(ss, limits, ' ');
            getline(ss, key, ' ');
            getline(ss, password, ' ');
            lower = stoi(limits.substr(0, limits.find('-')));
            higher = stoi(limits.substr(limits.find('-') + 1, limits.size() - limits.find('-')));
            key = key.substr(0, 1);
            password = password.substr(0, password.length());
            int count = 0;
            for (int i = 0; i < password.length(); i++)
            {
                if (*key.c_str() == password.c_str()[i])
                {
                    count++;
                }
            }
            if (count >= lower && count <= higher)
            {
                total++;
            }
        }
        f.close();
        return total;
    }
    else
    {
        cout << "Error Opening File" << endl;
    }
    return -1;
}
int solveP2()
{
    int total = 0;

    fstream f("2020day2.txt");
    if (f.is_open())
    {
        string line;
        while (getline(f, line))
        {
            string limits, key, password;
            int i, j;
            stringstream ss(line);
            getline(ss, limits, ' ');
            getline(ss, key, ' ');
            getline(ss, password, ' ');
            i = stoi(limits.substr(0, limits.find('-')));
            j = stoi(limits.substr(limits.find('-') + 1, limits.size() - limits.find('-')));
            key = key.substr(0, 1);
            password = password.substr(0, password.length());


            if ((*key.c_str() == password.c_str()[i - 1] && *key.c_str() != password.c_str()[j - 1]) || (*key.c_str() != password.c_str()[i - 1] && *key.c_str() == password.c_str()[j - 1]))
                total++;
        }
        f.close();
        return total;
    }
    else
    {
        cout << "Error Opening File" << endl;
    }
    return -1;
}
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
int solveP1();
int solveP2();
int main()
{
    cout << "Part 1 Answer: " << solveP1() << endl;
    cout << "Part 2 Answer: " << solveP2() << endl;
    return 0;
}
int solveP1()
{
    ifstream f("2020day6.txt");
    string input;
    set<char> s = {};
    int total = 0;
    while (getline(f, input))
    {
        if (input.length() == 0)
        {
            total += s.size();
            s.clear();
        }
        else
        {
            for (int i = 0; i < input.length(); i++)
                if (isalpha(input[i]))
                    s.insert(input[i]);
        }
    }
    total += s.size();
    f.close();
    return total;
}

int solveP2()
{
    ifstream f("2020day6.txt");
    string input;
    int total = 0;
    bool first = true;
    vector<char> all;
    while (getline(f, input))
    {
        if (input.length() == 0)
        {
            total += all.size();
            first = true;
        }
        else
        {
            if (first)
            {
                first = false;
                set<char> s;
                for (int i = 0; i < input.length(); i++)
                    s.insert(input[i]);
                vector<char> a(s.begin(), s.end());
                all = a;

            }
            else
            {
                set<char> s;
                for (int i = 0; i < input.length(); i++)
                    if (find(all.begin(), all.end(), input[i]) != all.end())
                        s.insert(input[i]);
                vector<char> a(s.begin(), s.end());
                all = a;
            }
        }
    }
    total += all.size();
    f.close();
    return total;
}

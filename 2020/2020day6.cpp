#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using std::chrono::duration;
using std::chrono::duration_cast;
using std::chrono::high_resolution_clock;
using std::chrono::milliseconds;
int solveP1();
int solveP2();
int main()
{
    auto t1 = high_resolution_clock::now();
    cout << "Part 1 Answer: " << solveP1() << endl;
    cout << "Part 2 Answer: " << solveP2() << endl;
    auto t2 = high_resolution_clock::now();
    duration<double, std::milli> ms_double = t2 - t1;
    cout << ms_double.count() << "ms";
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

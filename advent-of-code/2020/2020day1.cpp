#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int solve1(vector<int> vt);
int solve2(vector<int> vt);

int main()
{
    vector<int> v;
    fstream f("2020day1.txt");
    if (f.is_open())
    {
        int num;
        while (f >> num)
        {
            v.push_back(num);
        }
        f.close();
    }

    else
    {
        cout << "Error Opening File" << endl;
    }
    cout << "Part 1 Answer: " << solve1(v) << endl;
    cout << "Part 2 Answer: " << solve2(v) << endl;
}

int solve1(vector<int> vt)
{
    int size = vt.size();
    for (int i = 0; i < size; i++)
    {
        for (int j = i; j < size; j++)
        {

            if (vt[i] + vt[j] == 2020)
            {
                return vt[i] * vt[j];
            }
        }
    }
    return -1;
}
int solve2(vector<int> vt)
{
    int size = vt.size();
    for (int i = 0; i < size; i++)
    {
        for (int j = i; j < size; j++)
        {
            for (int k = j; k < size; k++)
            {
                if (vt[i] + vt[j] + vt[k] == 2020)
                {
                    return vt[i] * vt[j] * vt[k];
                }
            }
        }
    }
    return -1;
}
#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>
using namespace std;
int solveP1();
int solveP2(long int weakness);
int main()
{
    long int n = solveP1();
    cout << "Part 1 Answer: " << n << endl;
    cout << "Part 2 Answer: " << solveP2(n) << endl;
    return 0;
}

int solveP1()
{
    ifstream f("2020day9.txt");
    vector<long int> Q;
    long int x;
    while (f >> x)
    {
        if (Q.size() < 25)
            Q.push_back(x);
        else
        {
            bool valid = false;
            for (int i = 0; i < 25; i++)
                for (int j = 0; j < 25; j++)
                    if (Q[i] + Q[j] == x)
                    {
                        valid = true;
                        break;
                    }
            if (!valid)
            {
                f.close();
                return x;
            }
            Q.erase(Q.begin());
            Q.push_back(x);
        }
    }
    return -1;
}
int solveP2(long int weakness)
{
    ifstream f("2020day9.txt");
    vector<long int> Q;
    long int x;
    while (f >> x)
        Q.push_back(x);
    f.close();
    for (int i = 0; i < Q.size(); i++)
    {
        for (int j = i; j < Q.size(); j++)
        {
            long int sum = 0, smallest = Q[i], largest = Q[i];
            for (vector<long int>::iterator n = Q.begin() + i; n <= Q.begin() + j; n++)
            {
                sum += *n;
                if (*n < smallest)
                    smallest = *n;
                if (*n > largest)
                    largest = *n;
            }
            if (sum == weakness)
                return smallest + largest;
        }
    }
    
    return -1;
}
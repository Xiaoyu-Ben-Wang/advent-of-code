#include <iostream>
#include <fstream>
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
    ifstream f("2020day10.txt");
    int x;
    vector<int> arr;
    while (f >> x)
        arr.push_back(x);
    f.close();
    sort(arr.begin(), arr.end());
    int one=0, three=1;
    if (arr[0]==1)
        one++;
    if (arr[0]==3)
        three++;
    for (int i = 0; i < arr.size()-1; i++)
    {
        if(arr[i+1]-arr[i]==1)
            one++;
        if(arr[i+1]-arr[i]==3)
            three++;
    }
    return one*three;
}
int solveP2()
{

    return -1;
}
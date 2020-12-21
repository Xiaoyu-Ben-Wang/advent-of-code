#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int solveP1();
long long int solveP2();
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
    int one = 0, three = 1;
    if (arr[0] == 1)
        one++;
    if (arr[0] == 3)
        three++;
    for (int i = 0; i < arr.size() - 1; i++)
    {
        if (arr[i + 1] - arr[i] == 1)
            one++;
        if (arr[i + 1] - arr[i] == 3)
            three++;
    }
    return one * three;
}
long long int solveP2()
{
    ifstream f("2020day10.txt");
    int x;
    vector<int> arr;
    while (f >> x)
        arr.push_back(x);
    f.close();
    sort(arr.begin(), arr.end());
    vector<long long int> nodes(arr.size(),1);
    nodes[nodes.size()-1] = 1;
    for (int i = nodes.size()-2; i >= 0; i--)
    {
        long long int sum=0;
        for (int j = i+1; j < nodes.size();j++)
            if (arr[j]-arr[i]<=3)
                sum += nodes[j];
        nodes[i] *= sum;
        //cout << nodes[i] <<endl;
    }
    long long int ans = 0;
    for (int i = 0; i < arr.size();i++)
        if (arr[i]<=3)
            ans += nodes[i];
        else
            break;
        return ans;
}

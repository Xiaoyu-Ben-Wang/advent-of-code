#include <iostream>
#include <fstream>
#include <string>
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
    ifstream f("11.txt");
    vector<string> arr;
    string x;
    getline(f, x);
    string spacer(x.size() + 2, '*');
    arr.push_back(spacer);
    arr.push_back('*' + x + '*');
    while (getline(f, x))
        arr.push_back('*' + x + '*');
    arr.push_back(spacer);
    f.close();
    for (int i = 0; i < arr.size(); i++)
        cout
            << arr[i] << endl;
    vector<string> temp = arr;
    do
    {
        temp = arr;
        for (int i = 1; i < arr.size() - 1; i++)
        {
            for (int j = 1; j < arr[i].size() - 1; j++)
            {
                int adjacent = 0;
                if (arr[i][j] == 'L')
                {
                    arr[i][j + 1] == '#' ? adjacent++ : adjacent;
                    arr[i][j - 1] == '#' ? adjacent++ : adjacent;
                    arr[i + 1][j] == '#' ? adjacent++ : adjacent;
                    arr[i - 1][j] == '#' ? adjacent++ : adjacent;
                    arr[i + 1][j + 1] == '#' ? adjacent++ : adjacent;
                    arr[i + 1][j - 1] == '#' ? adjacent++ : adjacent;
                    arr[i - 1][j + 1] == '#' ? adjacent++ : adjacent;
                    arr[i - 1][j - 1] == '#' ? adjacent++ : adjacent;
                    adjacent > 0 ? temp[i][j] == '#' : 0;
                }
                else if (arr[i][j] == '#')
                {
                    arr[i][j + 1] == '#' ? adjacent++ : adjacent;
                    arr[i][j - 1] == '#' ? adjacent++ : adjacent;
                    arr[i + 1][j] == '#' ? adjacent++ : adjacent;
                    arr[i - 1][j] == '#' ? adjacent++ : adjacent;
                    arr[i + 1][j + 1] == '#' ? adjacent++ : adjacent;
                    arr[i + 1][j - 1] == '#' ? adjacent++ : adjacent;
                    arr[i - 1][j + 1] == '#' ? adjacent++ : adjacent;
                    arr[i - 1][j - 1] == '#' ? adjacent++ : adjacent;
                    adjacent >= 4 ? temp[i][j] == 'L' : 0;
                }
            }
        }
        if (equal(arr.begin(), arr.end(), temp.begin()))
            break;
        arr = temp;
    } while (true);
    for (int i = 0; i < arr.size(); i++)
        cout
            << arr[i] << endl;
    return -1;
}
int solveP2()
{
    return -1;
}

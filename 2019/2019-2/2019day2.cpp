#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int funct1(int X, int Y);
int main()
{
    cout << "Part 1 Answer: " << funct1(12, 2) << endl;

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            int ans = funct1(i, j);
            if (ans == 19690720)
            {
                cout << "Part 2 Noun: " << i << " Verb: " << j << endl;
                cout << "100*noun+verb = " << 100 * i + j << endl;
            }
        }
    }
    return 0;
}

int funct1(int X, int Y)
{
    ifstream f("2019day2.txt");
    int size = 1;
    vector<int> arr(0);
    int n = 0;
    string x;

    if (f.is_open())
    {
        while (getline(f, x, ','))
        {
            arr.push_back(stoi(x));
        }
        f.close();
    }
    arr[1] = X;
    arr[2] = Y;
    for (int i = 0; i <= int(arr.size()); i += 4)
    {
        int opcode = arr[i];
        if (opcode == 99)
        {
            return arr[0];
        }

        int a = arr[i + 1];
        int b = arr[i + 2];
        int c = arr[i + 3];

        if (opcode == 1)
        {
            arr[c] = arr[a] + arr[b];
        }
        else if (opcode == 2)
        {
            arr[c] = arr[a] * arr[b];
        }
    }
    return 0;
}

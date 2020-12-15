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
    ifstream f("2020day5.txt");
    string input;
    int current_max = -1;
    while (f >> input)
    {
        int l_row = 0, h_row = 127, l_col = 0, h_col = 7;
        for (int i = 0; i < 6; i++)
            input[i] == 'F' ? h_row -= (h_row - l_row + 1) / 2 : l_row += (h_row - l_row + 1) / 2;
        input[6] == 'F' ? h_row = l_row : l_row = h_row;
        for (int i = 0; i < 2; i++)
            input[i + 7] == 'L' ? h_col -= (h_col - l_col + 1) / 2 : l_col += (h_col - l_col + 1) / 2;
        input[9] == 'L' ? h_col = l_col : l_col = h_col;
        (l_row * 8 + l_col > current_max) ? current_max = l_row * 8 + l_col : 0;
    }
    f.close();
    return current_max;
}

int solveP2()
{
    ifstream f("2020day5.txt");
    string input;
    vector<int> ids;
    bool seats[128][8];
    while (f >> input)
    {
        int l_row = 0, h_row = 127, l_col = 0, h_col = 7;
        for (int i = 0; i < 6; i++)
            input[i] == 'F' ? h_row -= (h_row - l_row + 1) / 2 : l_row += (h_row - l_row + 1) / 2;
        input[6] == 'F' ? h_row = l_row : l_row = h_row;
        for (int i = 0; i < 2; i++)
            input[i + 7] == 'L' ? h_col -= (h_col - l_col + 1) / 2 : l_col += (h_col - l_col + 1) / 2;
        input[9] == 'L' ? h_col = l_col : l_col = h_col;
        seats[l_row][l_col] = true;
        ids.push_back(l_row * 8 + l_col);
    }
    for (int i = 1; i < 127; i++)
        for (int j = 0; j < 8; j++)
            if (seats[i][j] == false && find(ids.begin(), ids.end(), i * 8 + j - 1) != ids.end() && find(ids.begin(), ids.end(), i * 8 + j + 1) != ids.end())
                return i * 8 + j;
    return -1;
}

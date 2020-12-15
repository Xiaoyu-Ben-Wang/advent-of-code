#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
int solveP1();
int solveP2(int right, int down);

int main()
{
    cout << "Part 1 Answer: " << solveP1() << endl;
    cout << "Part 2 Answer: " << solveP2(1, 1) * solveP2(3, 1) * solveP2(5, 1) * solveP2(7, 1) * solveP2(1, 2) << endl;
}

int solveP1()
{
    int trees = 0;
    int index = 0;
    fstream f("2020day3.txt");
    string line;
    //getline(f, line);
    while (getline(f, line))
    {
        stringstream ss(line);
        char input;
        vector<char> array;
        while (ss >> input)
        {
            array.push_back(input);
        }
        if (array[index] == '#')
        {
            trees++;
        }
        index = (index + 3) % (array.size());
    }
    f.close();
    return trees;
}
int solveP2(int right, int down)
{
    int trees = 0;
    int index = 0;
    fstream f("2020day3.txt");
    string line;
    getline(f, line);
    while (true)
    {

        vector<char> array = {};
        for (int i = 0; i < down; i++)
        {
            getline(f, line);
        }
        if (f.eof())
            break;
        stringstream ss(line);
        char input;
        while (ss >> input)
        {
            array.push_back(input);
        }
        index = (index + right) % (array.size());
        if (array[index] == '#')
        {
            trees++;
        }
        //cout << array.capacity() << endl;
    }
    f.close();
    return trees;
}

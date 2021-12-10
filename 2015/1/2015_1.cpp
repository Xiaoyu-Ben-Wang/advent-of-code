#include <iostream>
#include <fstream>
using namespace std;
int part1();
int part2();

int main()
{
    cout << "===== Day 1 =====" << endl;
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
}

int part1()
{
    ifstream myfile("1.txt");
    char x;
    int floor = 0;
    while (myfile >> x)
    {
        if (x == '(')
        {
            floor++;
        }
        else if (x == ')')
        {
            floor--;
        }
    }
    return floor;
}
int part2()
{
    char x;
    ifstream myfile("1.txt");
    int floor = 0;
    int count = 0;
    while (myfile >> x)
    {
        count++;
        if (x == '(')
            floor++;
        else if (x == ')')
            floor--;
        if (floor < 0)
            break;
    }
    return count;
}
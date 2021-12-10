#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int sum1 = 0;
    int sum2 = 0;
    int x;
    ifstream myfile("1.txt");
    if (myfile.is_open())
    {
        while (myfile >> x)
        {
            sum1 += x / 3 - 2;
            sum2 += x / 3 - 2;
            int temp = x / 3 - 2;
            while (temp / 3 - 2 >= 0)
            {
                temp = temp / 3 - 2;
                sum2 += temp;
            }
        }
        myfile.close();
    }
    else
    {
        cout << "Unable to open file";
        exit(0);
    }
    cout << "Part 1 Total: " << sum1 << endl;
    cout << "Part 2 Total: " << sum2 << endl;
    return 0;
}

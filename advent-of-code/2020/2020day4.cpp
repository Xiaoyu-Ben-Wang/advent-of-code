#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int solveP1();
int solveP2();
int main()
{
    cout << "Part 1 Answer: " << solveP1() << endl;
    cout << "Part 2 Answer: " << solveP2() << endl;
}

int solveP1()
{
    int valid = 0;
    fstream f("2020day4.txt");
    do
    {
        string passport = "";
        string lines;
        while (true)
        {
            getline(f, lines);
            if (lines != "")
                passport += +" " + lines;
            else
            {
                stringstream ss(passport);
                string field;
                int matched = 0;
                while (getline(ss, field, ' '))
                {
                    field.find("byr") != string::npos ? matched++ : matched;
                    field.find("iyr") != string::npos ? matched++ : matched;
                    field.find("eyr") != string::npos ? matched++ : matched;
                    field.find("hgt") != string::npos ? matched++ : matched;
                    field.find("hcl") != string::npos ? matched++ : matched;
                    field.find("ecl") != string::npos ? matched++ : matched;
                    field.find("pid") != string::npos ? matched++ : matched;
                }
                if (matched == 7)
                    valid++;
                break;
            }
        }
    } while (!f.eof());
    f.close();
    return valid;
}
int solveP2()
{
    int valid = 0;
    fstream f("2020day4.txt");
    do
    {
        string passport = "";
        string lines;
        while (true)
        {
            getline(f, lines);
            if (lines != "")
                passport += lines + " ";
            else
            {
                stringstream ss(passport);
                string field;
                int matched = 0;
                while (getline(ss, field, ' '))
                {
                    string code = field.substr(0, 4);
                    string value = field.substr(4, field.size() - 4);
                    if (code == "byr:")
                    {
                        int year = stoi(value);
                        if (year >= 1920 && year <= 2002)
                            matched++;
                    }
                    if (code == "iyr:")
                    {
                        int year = stoi(value);
                        if (year >= 2010 && year <= 2020)
                            matched++;
                    }
                    if (code == "eyr:")
                    {
                        int year = stoi(value);
                        if (year >= 2020 && year <= 2030)
                            matched++;
                    }
                    if (code == "hgt:")
                    {
                        string unit = value.substr(value.size() - 2, 2);
                        int n = stoi(value);
                        if (unit == "cm" && n >= 150 && n <= 193)
                            matched++;
                        if (unit == "in" && n >= 59 && n <= 76)
                            matched++;
                    }
                    if (code == "hcl:")
                    {
                        char c = value[0];
                        string color = value.substr(1, value.length() - 1);
                        if (color.find_first_not_of("abcedf0123456789", 0) == string::npos && c == '#' && color.length() == 6)
                            matched++;
                    }
                    if (code == "ecl:")
                    {
                        string colors[] = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
                        for (int i = 0; i < sizeof(colors)/sizeof(string); i++)
                        {
                            if (value == colors[i])
                            {
                                matched++;
                                break;
                            }
                        }
                    }
                    if (code =="pid:")
                    {
                        if (value.length()==9 && value.find_first_of("abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ",0)==string::npos)
                            matched++;
                    }
                }
                //cout << passport << " Valid:" << matched << endl;
                if (matched == 7)
                    valid++;
                break;
            }
        }
    } while (!f.eof());
    f.close();
    return valid;
}

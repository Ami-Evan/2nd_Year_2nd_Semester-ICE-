#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Create LPS array
void createLPS(string pattern, int lps[])
{
    int m = pattern.length();

    int len = 0;
    lps[0] = 0;

    int i = 1;

    while (i < m)
    {
        if (pattern[i] == pattern[len])
        {
            len++;
            lps[i] = len;
            i++;
        }
        else
        {
            if (len != 0)
            {
                len = lps[len - 1];
            }
            else
            {
                lps[i] = 0;
                i++;
            }
        }
    }
}

// KMP Search
void KMP(string text, string pattern)
{
    int n = text.length();
    int m = pattern.length();

    int lps[m];

    createLPS(pattern, lps);

    int i = 0;
    int j = 0;

    bool found = false;

    while (i < n)
    {
        if (text[i] == pattern[j])
        {
            i++;
            j++;
        }

        if (j == m)
        {
            cout << "Pattern found at position: " << i - j << endl;

            found = true;

            j = lps[j - 1];
        }
        else if (i < n && text[i] != pattern[j])
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                i++;
            }
        }
    }

    if (!found)
    {
        cout << "Pattern not found!" << endl;
    }
}

int main()
{
    ifstream file("text.txt");

    if (!file)
    {
        cout << "File could not be opened!" << endl;
        return 0;
    }

    string text;
    string line;

    // Read complete text file
    while (getline(file, line))
    {
        text += line;
        text += '\n';
    }

    file.close();

    string pattern;

    cout << "Enter word to search: ";
    cin >> pattern;

    KMP(text, pattern);

    return 0;
}


/*
text.txt এ যেমন লিখতে পারো
Hello, my name is Evan.
I am learning C++ and Competitive Programming.
I love programming and I practice programming every day.

Program run করলে:

Enter word to search: programming

Output:

Pattern found at position: 57
Pattern found at position: 79
*/
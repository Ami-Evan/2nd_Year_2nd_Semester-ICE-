
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string text, pattern;

    // Text file open
    ifstream file("text.txt");

    if (!file)
    {
        cout << "File could not be opened!" << endl;
        return 0;
    }

    // File theke text read
    getline(file, text);

    file.close();

    // Pattern input
    cout << "Enter the pattern: ";
    getline(cin, pattern);

    int n = text.length();
    int m = pattern.length();

    bool found = false;

    // Pattern Matching
    for (int i = 0; i <= n - m; i++)
    {
        int j;

        for (j = 0; j < m; j++)
        {
            if (text[i + j] != pattern[j])
            {
                break;
            }
        }

        if (j == m)
        {
            cout << "Pattern found at position: " << i << endl;
            found = true;
        }
    }

    if (!found)
    {
        cout << "Pattern not found!" << endl;
    }

    return 0;
}

#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> a;

bool safe(int r, int c)
{
    for (int i = 0; i < r; i++)
        if (a[i][c]) return false;

    for (int i=r-1,j=c-1; i>=0&&j>=0; i--,j--)
        if (a[i][j]) return false;

    for (int i=r-1,j=c+1; i>=0&&j<n; i--,j++)
        if (a[i][j]) return false;

    return true;
}

bool solve(int r)
{
    if (r == n) return true;

    for (int c = 0; c < n; c++)
    {
        if (safe(r,c))
        {
            a[r][c] = 1;

            if (solve(r+1)) return true;

            a[r][c] = 0;
        }
    }
    return false;
}

int main()
{
    cin >> n;
    a.resize(n, vector<int>(n,0));

    if (solve(0))
        for (auto row : a)
        {
            for (int x : row) cout << x << " ";
            cout << endl;
        }
}


//using array
/*
#include <iostream>
using namespace std;

int n;
int board[10][10];

bool safe(int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        if (board[i][col] == 1)
            return false;
    }

    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
    {
        if (board[i][j] == 1)
            return false;
    }

    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
    {
        if (board[i][j] == 1)
            return false;
    }

    return true;
}

bool solve(int row)
{
    if (row == n)
        return true;

    for (int col = 0; col < n; col++)
    {
        if (safe(row, col))
        {
            board[row][col] = 1;

            if (solve(row + 1))
                return true;

            board[row][col] = 0;
        }
    }

    return false;
}

int main()
{
    cout << "Enter n: ";
    cin >> n;

    if (solve(0))
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                cout << board[i][j] << " ";

            cout << endl;
        }
    }
    else
        cout << "No solution";

    return 0;
}
*/
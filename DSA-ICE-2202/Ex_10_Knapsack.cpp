#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, C;

    cout << "Enter number of items: ";
    cin >> n;

    cout << "Enter capacity: ";
    cin >> C;

    vector<int> P(n);
    vector<int> W(n);

    cout << "Enter profits: ";
    for (int i = 0; i < n; i++)
        cin >> P[i];

    cout << "Enter weights: ";
    for (int i = 0; i < n; i++)
        cin >> W[i];

    vector<vector<int>> dp(n + 1, vector<int>(C + 1, 0));

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= C; j++)
        {
            if (W[i - 1] <= j)
            {
                dp[i][j] = max(dp[i - 1][j],
                               P[i - 1] + dp[i - 1][j - W[i - 1]]);
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << "Maximum Profit = " << dp[n][C] << endl;

    return 0;
}




//using array
/*
#include <iostream>
using namespace std;

int main()
{
    int n, C;

    cout << "Enter number of items: ";
    cin >> n;

    cout << "Enter capacity: ";
    cin >> C;

    int P[50], W[50];
    int dp[51][101] = {0};

    cout << "Enter profits: ";
    for (int i = 0; i < n; i++)
        cin >> P[i];

    cout << "Enter weights: ";
    for (int i = 0; i < n; i++)
        cin >> W[i];

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= C; j++)
        {
            if (W[i - 1] <= j)
            {
                dp[i][j] = max(dp[i - 1][j],
                               P[i - 1] + dp[i - 1][j - W[i - 1]]);
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << "Maximum Profit = " << dp[n][C] << endl;

    return 0;
}
*/
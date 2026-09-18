#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n = 4, C = 20;

    vector<int> P = {15, 25, 13, 23};
    vector<int> W = {2, 6, 12, 9};

    vector<vector<int>> dp(n + 1, vector<int>(C + 1, 0));

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= C; j++)
        {
            if (W[i - 1] <= j)
                dp[i][j] = max(dp[i - 1][j],
                               P[i - 1] + dp[i - 1][j - W[i - 1]]);
            else
                dp[i][j] = dp[i - 1][j];
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
    int n = 4, C = 20;

    int P[] = {15, 25, 13, 23};
    int W[] = {2, 6, 12, 9};

    int dp[5][21] = {0};

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= C; j++)
        {
            if (W[i - 1] <= j)
                dp[i][j] = max(dp[i - 1][j],
                               P[i - 1] + dp[i - 1][j - W[i - 1]]);
            else
                dp[i][j] = dp[i - 1][j];
        }
    }

    cout << "Maximum Profit = " << dp[n][C] << endl;

    return 0;
}
*/
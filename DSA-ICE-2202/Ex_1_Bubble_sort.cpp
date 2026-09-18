#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> v(n);

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
        cin >> v[i];

    cout << "\nInitial Array: ";
    for (int x : v)
        cout << x << " ";

    cout << "\n\nBubble Sort Steps:\n";

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (v[j] > v[j + 1])
            {
                int temp = v[j];
                v[j] = v[j + 1];
                v[j + 1] = temp;
            }
        }

        cout << "Pass " << i + 1 << ": ";

        for (int x : v)
            cout << x << " ";

        cout << endl;
    }

    cout << "\nSorted Array: ";

    for (int x : v)
        cout << x << " ";

    cout << endl;

    return 0;
}

//using array
/*
#include <iostream>
using namespace std;

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[50];

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "\nInitial Array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    cout << "\n\nBubble Sort Steps:\n";

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }

        cout << "Pass " << i + 1 << ": ";

        for (int k = 0; k < n; k++)
            cout << arr[k] << " ";

        cout << endl;
    }

    cout << "\nSorted Array: ";

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    cout << endl;

    return 0;
}
*/
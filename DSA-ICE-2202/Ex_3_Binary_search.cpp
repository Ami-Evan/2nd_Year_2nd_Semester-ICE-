#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> v(n);

    cout << "Enter elements in sorted order: ";
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    int key;

    cout << "Enter element to search: ";
    cin >> key;

    int low = 0;
    int high = n - 1;

    bool found = false;

    cout << "\nBinary Search Steps:\n";

    while (low <= high)
    {
        int mid = (low + high) / 2;

        cout << "Low = " << low
             << ", Mid = " << mid
             << ", High = " << high << endl;

        cout << "Middle element = " << v[mid] << endl;

        if (v[mid] == key)
        {
            cout << "Element found at position " << mid + 1 << endl;
            found = true;
            break;
        }
        else if (key < v[mid])
        {
            cout << "Search in left half" << endl;
            high = mid - 1;
        }
        else
        {
            cout << "Search in right half" << endl;
            low = mid + 1;
        }

        cout << endl;
    }

    if (found == false)
    {
        cout << "Element not found" << endl;
    }

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

    cout << "Enter elements in sorted order: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int key;
    cout << "Enter element to search: ";
    cin >> key;

    int low = 0;
    int high = n - 1;
    bool found = false;

    cout << "\nBinary Search Steps:\n";

    while (low <= high)
    {
        int mid = (low + high) / 2;

        cout << "Low = " << low
             << ", Mid = " << mid
             << ", High = " << high << endl;

        cout << "Middle element = " << arr[mid] << endl;

        if (arr[mid] == key)
        {
            cout << "Element found at position " << mid + 1 << endl;
            found = true;
            break;
        }
        else if (key < arr[mid])
        {
            cout << "Search in left half\n";
            high = mid - 1;
        }
        else
        {
            cout << "Search in right half\n";
            low = mid + 1;
        }

        cout << endl;
    }

    if (found == false)
    {
        cout << "Element not found" << endl;
    }

    return 0;
}
*/
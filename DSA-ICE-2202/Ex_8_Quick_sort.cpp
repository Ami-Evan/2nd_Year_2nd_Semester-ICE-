#include <iostream>
using namespace std;

int n;

// Print array
void printArray(int arr[])
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    cout << endl;
}

// Partition function
int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Put pivot in correct position
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    cout << "Pivot = " << pivot << " : ";
    printArray(arr);

    return i + 1;
}

// Quick Sort
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[50];

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "\nInitial Array: ";
    printArray(arr);

    cout << "\nQuick Sort Steps:\n";

    quickSort(arr, 0, n - 1);

    cout << "\nFinal Sorted Array: ";
    printArray(arr);

    return 0;
}



// using vector
/*
#include <iostream>
#include <vector>
using namespace std;

int n;

// Print vector
void printArray(vector<int> &arr)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    cout << endl;
}

// Partition function
int partition(vector<int> &arr, int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Put pivot in correct position
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    cout << "Pivot = " << pivot << " : ";
    printArray(arr);

    return i + 1;
}

// Quick Sort
void quickSort(vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> arr(n);

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "\nInitial Array: ";
    printArray(arr);

    cout << "\nQuick Sort Steps:\n";

    quickSort(arr, 0, n - 1);

    cout << "\nFinal Sorted Array: ";
    printArray(arr);

    return 0;
}
*/
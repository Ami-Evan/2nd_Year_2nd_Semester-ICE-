#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> &v)
{
    for (int x : v)
        cout << x << " ";

    cout << endl;
}

void merge(vector<int> &v, int l, int m, int r)
{
    vector<int> temp;

    int i = l;
    int j = m + 1;

    while (i <= m && j <= r)
    {
        if (v[i] < v[j])
        {
            temp.push_back(v[i]);
            i++;
        }
        else
        {
            temp.push_back(v[j]);
            j++;
        }
    }

    while (i <= m)
    {
        temp.push_back(v[i]);
        i++;
    }

    while (j <= r)
    {
        temp.push_back(v[j]);
        j++;
    }

    for (int k = 0; k < temp.size(); k++)
        v[l + k] = temp[k];
}

void mergeSort(vector<int> &v, int l, int r)
{
    if (l >= r)
        return;

    int m = (l + r) / 2;

    mergeSort(v, l, m);
    mergeSort(v, m + 1, r);

    merge(v, l, m, r);

    cout << "Merge: ";
    for (int i = l; i <= r; i++)
        cout << v[i] << " ";

    cout << endl;
}

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
    print(v);

    cout << "\nMerge Sort Steps:\n";

    mergeSort(v, 0, n - 1);

    cout << "\nSorted Array: ";
    print(v);

    return 0;
}

//using array
/*
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

// Merge two parts
void merge(int arr[], int left, int mid, int right)
{
    int temp[50];

    int i = left;
    int j = mid + 1;
    int k = 0;

    // Compare and merge
    while (i <= mid && j <= right)
    {
        if (arr[i] < arr[j])
        {
            temp[k] = arr[i];
            i++;
        }
        else
        {
            temp[k] = arr[j];
            j++;
        }

        k++;
    }

    // Copy remaining left part
    while (i <= mid)
    {
        temp[k] = arr[i];
        i++;
        k++;
    }

    // Copy remaining right part
    while (j <= right)
    {
        temp[k] = arr[j];
        j++;
        k++;
    }

    // Put sorted values back into array
    for (int x = 0; x < k; x++)
    {
        arr[left + x] = temp[x];
    }

    // Show merge step
    cout << "Merge: ";
    for (int x = left; x <= right; x++)
        cout << arr[x] << " ";

    cout << endl;
}

// Merge Sort
void mergeSort(int arr[], int left, int right)
{
    if (left >= right)
        return;

    int mid = (left + right) / 2;

    // Sort left part
    mergeSort(arr, left, mid);

    // Sort right part
    mergeSort(arr, mid + 1, right);

    // Merge both parts
    merge(arr, left, mid, right);
}

int main()
{
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[50];

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "\nInitial Array: ";
    printArray(arr);

    cout << "\nMerge Sort Steps:\n";

    mergeSort(arr, 0, n - 1);

    cout << "\nSorted Array: ";
    printArray(arr);

    return 0;
}
*/
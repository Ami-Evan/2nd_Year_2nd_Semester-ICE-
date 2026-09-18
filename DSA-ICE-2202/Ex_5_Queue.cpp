#include <iostream>
#include <vector>
using namespace std;

vector<int> q;

// Enqueue operation
void enqueue(int value)
{
    q.push_back(value);
    cout << value << " inserted into queue" << endl;
}

// Dequeue operation
void dequeue()
{
    if (q.empty())
    {
        cout << "Queue is empty" << endl;
        return;
    }

    cout << q.front() << " removed from queue" << endl;
    q.erase(q.begin());
}

// Front operation
void front()
{
    if (q.empty())
    {
        cout << "Queue is empty" << endl;
        return;
    }

    cout << "Front element: " << q.front() << endl;
}

// Size operation
void size()
{
    cout << "Queue size: " << q.size() << endl;
}

// Empty operation
void empty()
{
    if (q.empty())
        cout << "Queue is empty" << endl;
    else
        cout << "Queue is not empty" << endl;
}

int main()
{
    int n, value;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter " << n << " elements:" << endl;

    for (int i = 0; i < n; i++)
    {
        cin >> value;
        enqueue(value);
    }

    cout << endl;

    front();
    size();
    empty();

    cout << endl;

    dequeue();

    front();
    size();
    empty();

    return 0;
}



//using array
/*
#include <iostream>
using namespace std;

#define SIZE 5

int q[SIZE];
int frontIndex = 0;
int rear = -1;

// Enqueue operation
void enqueue(int value)
{
    if (rear == SIZE - 1)
    {
        cout << "Queue is full" << endl;
        return;
    }

    rear++;
    q[rear] = value;

    cout << value << " inserted into queue" << endl;
}

// Dequeue operation
void dequeue()
{
    if (frontIndex > rear)
    {
        cout << "Queue is empty" << endl;
        return;
    }

    cout << q[frontIndex] << " removed from queue" << endl;
    frontIndex++;
}

// Front operation
void front()
{
    if (frontIndex > rear)
    {
        cout << "Queue is empty" << endl;
        return;
    }

    cout << "Front element: " << q[frontIndex] << endl;
}

// Size operation
void size()
{
    cout << "Queue size: " << rear - frontIndex + 1 << endl;
}

// Empty operation
void empty()
{
    if (frontIndex > rear)
        cout << "Queue is empty" << endl;
    else
        cout << "Queue is not empty" << endl;
}

int main()
{
    int n, value;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter " << n << " elements:" << endl;

    for (int i = 0; i < n; i++)
    {
        cin >> value;
        enqueue(value);
    }

    cout << endl;

    front();
    size();
    empty();

    cout << endl;

    dequeue();

    front();
    size();
    empty();

    return 0;
}
*/
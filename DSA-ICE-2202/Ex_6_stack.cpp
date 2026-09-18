#include <iostream>
#include <vector>
using namespace std;

vector<int> st;

// Push operation
void push(int value)
{
    st.push_back(value);
    cout << value << " pushed into stack" << endl;
}

// Pop operation
void pop()
{
    if (st.empty())
    {
        cout << "Stack is empty" << endl;
        return;
    }

    cout << st.back() << " popped from stack" << endl;
    st.pop_back();
}

// Top operation
void top()
{
    if (st.empty())
    {
        cout << "Stack is empty" << endl;
        return;
    }

    cout << "Top element: " << st.back() << endl;
}

// Size operation
void size()
{
    cout << "Stack size: " << st.size() << endl;
}

// Empty operation
void empty()
{
    if (st.empty())
        cout << "Stack is empty" << endl;
    else
        cout << "Stack is not empty" << endl;
}

int main()
{
    int n, value;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter " << n << " elements: " << endl;

    for (int i = 0; i < n; i++)
    {
        cin >> value;
        push(value);
    }

    cout << endl;

    top();
    size();
    empty();

    cout << endl;

    pop();

    top();
    size();
    empty();

    return 0;
}
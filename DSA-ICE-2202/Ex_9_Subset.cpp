#include <iostream> 
using namespace std; 
int s[] = {5, 10, 12, 13, 15, 18}; 
int n = 6; 
int d; 
int subset[10]; 
  
void findSubset(int index, int sum, int count) { 
    if (sum == d) { 
        cout << "Subset found: "; 
        for (int i = 0; i < count; i++) 
            cout << subset[i] << " "; 
        cout << endl; 
        return; 
    } 
  
    if (index == n || sum > d) 
        return; 
  
    // Include current element 
    subset[count] = s[index]; 
    findSubset(index + 1, sum + s[index], count + 1); 
  
    // Exclude current element 
    findSubset(index + 1, sum, count); 
} 
  
int main() { 
    cout << "Enter target sum d: "; 
    cin >> d; 
  
    findSubset(0, 0, 0); 
  
    return 0; 
}



//using array
/*
#include <iostream>
using namespace std;

#define SIZE 5

int stackArr[SIZE];
int topIndex = -1;

// Push operation
void push(int value)
{
    if (topIndex == SIZE - 1)
    {
        cout << "Stack is full" << endl;
        return;
    }

    topIndex++;
    stackArr[topIndex] = value;

    cout << value << " pushed into stack" << endl;
}

// Pop operation
void pop()
{
    if (topIndex == -1)
    {
        cout << "Stack is empty" << endl;
        return;
    }

    cout << stackArr[topIndex] << " popped from stack" << endl;
    topIndex--;
}

// Top operation
void top()
{
    if (topIndex == -1)
    {
        cout << "Stack is empty" << endl;
        return;
    }

    cout << "Top element: " << stackArr[topIndex] << endl;
}

// Size operation
void size()
{
    cout << "Stack size: " << topIndex + 1 << endl;
}

// Empty operation
void empty()
{
    if (topIndex == -1)
        cout << "Stack is empty" << endl;
    else
        cout << "Stack is not empty" << endl;
}

int main()
{
    push(10);
    push(20);
    push(30);

    top();
    size();
    empty();

    pop();

    top();
    size();
    empty();

    return 0;
}
*/

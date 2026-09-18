#include <iostream>
using namespace std;

void hanoi(int n, char from, char to, char aux)
{
    if (n == 1)
    {
        cout << "Move disk 1 from " << from << " to " << to << endl;
        return;
    }

    hanoi(n - 1, from, aux, to);

    cout << "Move disk " << n << " from " << from << " to " << to << endl;

    hanoi(n - 1, aux, to, from);
}

int main()
{
    int n;

    cout << "Enter number of disks: ";
    cin >> n;

    hanoi(n, 'A', 'C', 'B');

    return 0;
}

/*
Example Output

Input:

3

Output:

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

এখানে A = Source, B = Auxiliary, C = Destination।
*/
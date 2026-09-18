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


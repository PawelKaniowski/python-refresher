#include <iostream> 
using namespace std;
void doubler(int &x)
{
    x = x * 2;
}

int main()
{
    int x = 5;
    cout << "Before function call: " << x << endl;
    f(x);
    cout << "After function call:  " << x << endl;
    return 0;
}
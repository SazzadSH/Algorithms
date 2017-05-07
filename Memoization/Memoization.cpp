#include <iostream>

using namespace std;

int fib_ara[1000], function_calls;

int fibonacci(int x);

int main()
{

    for(int i = 0; i < 1000; i++)
    {
        fib_ara[i] = NULL;
    }

    int n;

    cout << "Nth term: ";

    cin >> n;

    cout << "Fibonacci sequence: " << fibonacci(n) << endl;

    cout << "Number of function calls: " << function_calls << endl;

    return 0;
}

int fibonacci(int x)
{
    function_calls++;

    if(fib_ara[x] == NULL)
    {
        if(x <= 1)
        {
            fib_ara[x] = x;
        }
        else
            fib_ara[x] = fibonacci(x - 1) + fibonacci(x - 2);
    }

    return fib_ara[x];
}

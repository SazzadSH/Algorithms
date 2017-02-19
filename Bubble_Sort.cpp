/*

Program: Bubble Sort Demonstration
Category: Sorting Algorithm
Algorithm: Bubble Sort
Algorithm Details: https://en.wikipedia.org/wiki/Bubble_sort

Program Coder: Sazzad Hossen (http://fb.com/SazzadSH)
Github: http://www.github.com/SazzadSH

*/


#include <iostream>                                         //Input Output Stream Header File

using namespace std;                                        //Standard Namespace

void Bubble_Sort(int ara[], int x);                        //Bubble Sort Function prototype

int main()                                                 //Main Function
{
    int n;                                                 //integer declaration for item number

    cout << "Number of items: " << endl;

    cin >> n;                                              //Input number of items

    int items[n];                                          //Array declaration for items

    for(int i = 0; i < n; i++)                             //Loop for array items input
    {
        cout << "Enter item " << i + 1 << ": " << endl;

        cin >> items[i];                                   //Input items
    }

    cout << "Your items (unsorted): " << endl;

    for(int i = 0; i < n; i++)                            //Loop for unsorted items output
    {
        cout << items[i] << " ";
    }

    cout << endl << "Your items (sorted): " << endl;

    Bubble_Sort(items, n);                                //Bubble Sort Function calling

    return 0;                                             //End of Main Function
}

void Bubble_Sort(int ara[], int x)                       //Bubble Sort Function
{
    for(int i = 0; i < x; i++)                           //Sorting loop
    {
        for(int j = 0; j < x-i-1; j++)
        {
            if(ara[j] > ara[j+1])
            {
                int temp = ara[j];
                ara[j] = ara[j+1];
                ara[j+1] = temp;
            }
        }
    }

    for(int i = 0; i < x; i++)                          //Loop for sorted items output
    {
        cout << ara[i] << " ";
    }
}

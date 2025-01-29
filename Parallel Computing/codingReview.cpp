// Stack and Heap for memory management
// malloc is on the heap(free after use), a[100] is on stack
// The new operator is worked on heap

// Why do we want heaps
// the variable that created in stack will be freed when the function is returned.
#include <stdio.h>
#include <iostream>
#include <vector>
namespace mynamespace{
    int x = 5;
}

void outBoundCase(){
    int p[3];
    int a = 4;
    std::cout << a << "\n";
    p[3] = 5;
    std::cout << a << "\n";
}

void workOnHeap(){
    int *rp = new int(); // run on heap. Remember to free. Use rp->width to get attribute. On stack, we can use rp.width
    delete rp; 
}

int square(int &x){
    return x * x;
}

void loop(){
    std::vector<int> images = std::vector<int>(9);

    for (int &i:images){
        // Do something. Also, ++i is faster than i++.
    }
}

// Same class name in different namespaces, a folder to put classes into.
namespace mynamespace{
    int x = 5;
}
int main() {
    // Pass reference rather than passing value(pointer)
    int x = 2;
    square(x);

    return 0;
}
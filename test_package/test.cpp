#include <mimetic/version.h>
#include <iostream>

int main(int argc, char *argv[])
{
    std::cout << mimetic::version.str() << std::endl;
    return 0;
}


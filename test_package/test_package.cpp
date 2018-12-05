#include <cstdlib>
#include <iostream>

#include "tl/expected.hpp"

int main()
{
    tl::expected<int,int> e;
    if (e == 0) { std::cout << "Bincrafters\n"; }
    return EXIT_SUCCESS;
}

#include <string>
#include <cstdio>
#include <cstdint>
#include <loader.h>
#include <iostream>

auto main(int argc, char* argv[]) -> int {
    size_t i;
    Binary bin;
    Section* psec;
    Symbol* psym;
    std::string filename;

    if(argc < 2) {
        std::cout << "Usage: " << argv[0] << " <binary>" << std::endl;
        return 0;
    }

    filename.assign(argv[1]);
    unit_test();
    return 0;
}

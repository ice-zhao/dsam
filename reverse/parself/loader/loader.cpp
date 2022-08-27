#include <config.h>
#include <bfd.h>
#include <loader.h>
#include <iostream>

static bfd* open_bfd(const std::string& filename) {
    static bool bfd_inited = false;
    bfd* pbfd;

    if(!bfd_inited) {
        bfd_init();
        bfd_inited = true;
    }

    if(bfd_inited) {
        std::cout << "bfd inited" << std::endl;
    }

    return nullptr;
}



void unit_test() {
    open_bfd("abc");
}

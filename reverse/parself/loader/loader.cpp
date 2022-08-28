#include <config.h>
#include <bfd.h>
#include <loader.h>
#include <iostream>
#include <cstdio>
#include <glog/logging.h>
#include <cstdlib>

static bfd* open_bfd(const std::string& filename) {
    static bool bfd_inited = false;
    bfd* pbfd;

    if(!bfd_inited) {
        bfd_init();
        bfd_inited = true;
    }

    if(bfd_inited) {
        std::cout << "bfd inited." << std::endl;
        LOG(INFO) << "bfd inited.";
    }

    pbfd = bfd_openr(filename.c_str(), nullptr);
    if(pbfd == nullptr) {
        std::cerr << "failed to open binary file: " << filename << " (" <<
            bfd_errmsg(bfd_get_error()) << ")."<< std::endl;
        return nullptr;
    }

    if(!bfd_check_format(pbfd, bfd_object)) {
        std::cerr << "file " << filename << " does not look like an executable (" <<
            bfd_errmsg(bfd_get_error()) << ")."<< std::endl;
        return nullptr;
    }

    bfd_set_error(bfd_error_no_error);

    if(bfd_get_flavour(pbfd) == bfd_target_unknown_flavour) {
        std::cerr << "unrecognized format for binary " << filename << " (" <<
            bfd_errmsg(bfd_get_error()) << ")."<< std::endl;
        return nullptr;
    }

    return pbfd;
}

static int load_symbols_bfd(bfd* pbfd, Binary* pbin) {
    int ret;
    long n, nsyms, i;
    asymbol** ppbfd_symtab;
    Symbol* sym;

    ppbfd_symtab = nullptr;

    /*
     * to find how many space we need to allocate to store the symbol table
     * if existed.
     */
    n = bfd_get_symtab_upper_bound(pbfd);
    if(n < 0) {
        LOG(ERROR) << "failed to read symtab (" <<
            bfd_errmsg(bfd_get_error()) << ")."<< std::endl;
        goto fail;
    }

fail:
    ret = -1;

cleanup:
    if(ppbfd_symtab) free(ppbfd_symtab);

    return ret;
}

void unit_test_loader(const std::string& filename) {
    bfd* pbfd = open_bfd(filename);
    if (pbfd != nullptr) {
        std::cout << "open binary file successful!" << std::endl;
        bfd_close(pbfd);
        pbfd = nullptr;
    }
}

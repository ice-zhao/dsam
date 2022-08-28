#ifndef __SYMBOL_H__
#define __SYMBOL_H__

#include <cstdint>
#include <string>
#include <vector>

class Binary;
class Section;
class Symbol;

enum class SymbolType {
    SYM_TYPE_UKN,
    SYM_TYPE_FUNC
};

class Symbol {
public:
    SymbolType type;
    std::string name;
    uint64_t addr;

    Symbol() : type(SymbolType::SYM_TYPE_UKN), name(), addr(0) {}
};

enum class SectionType {
    SEC_TYPE_NONE,
    SEC_TYPE_CODE,
    SEC_TYPE_DATA
};

class Section {
public:
    Binary *binary;
    std::string name;
    SectionType type;
    uint64_t vma;
    uint64_t size;
    uint8_t *bytes;

    Section(): binary(nullptr), type(SectionType::SEC_TYPE_NONE), name(), vma(0), size(0), bytes(nullptr) {}
    bool contains(uint64_t addr) { return (addr >= vma) && (addr - vma < size); }
};

enum class BinaryType {
    BIN_TYPE_AUTO,
    BIN_TYPE_ELF,
    BIN_TYPE_PE
};

enum class BinaryArch {
    ARCH_NONE,
    ARCH_X86
};

class Binary {
public:
    std::string filename;
    BinaryType type;
    std::string type_str;
    BinaryArch arch;
    std::string arch_str;
    unsigned bits;
    uint64_t entry;
    std::vector<Section> sections;
    std::vector<Symbol> symbols;

    Binary(): type(BinaryType::BIN_TYPE_AUTO), arch(BinaryArch::ARCH_NONE), bits(0), entry(0) {}

    Section* get_text_section() {
        for(auto& s : sections) {
            if(s.name == ".text")
                return &s;
        }
        return nullptr;
    }

};

int load_binary(std::string& filename, Binary* bin, BinaryType type);
void unload_binary(Binary* pbin);
void unit_test_loader(const std::string& filename);

#endif

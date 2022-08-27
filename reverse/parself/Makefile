binutils_base=/home/ice/cto/tools/sources/tools/reverse/binutils-gdb
libs_dir=-L/home/ice/cto/tools/sources/tools/reverse/binutils-gdb/install/lib

CXXFLAGS=
LDFLAGS=
include_dir=-I${PWD}/include
LDLIBS=-lbfd

objs-loader=${PWD}/loader/loader.o

all:
	make all -C ./labs
	make all -C ./loader
	make parself

parself: ${objs-loader} parself.o
	g++ ${LDFLAGS} ${libs_dir} $^ -o $@ ${LDLIBS}

parself.o: parself.cpp
	g++ ${CXXFLAGS} ${include_dir} -c $< -o $@


clean:
	make clean -C ./labs/
	make clean -C ./loader
	rm -rf parself

.PHONY: all clean

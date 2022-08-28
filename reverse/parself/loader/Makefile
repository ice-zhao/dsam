binutils_base=/home/ice/cto/tools/sources/tools/reverse/binutils-gdb
glog_base=/home/ice/gm/tools/logging/glog/install

include_dir=-I${PWD}/include -I${binutils_base}/install/include -I${binutils_base}/bfd -I${glog_base}

libs_dir=-L/home/ice/cto/tools/sources/tools/reverse/binutils-gdb/install/lib

CXXFLAGS=
LDFLAGS=
LDLIBS=-lbfd

all: loader.o

loader.o: loader.cpp
	g++ ${CXXFLAGS} ${include_dir} -c $< -o $@

clean:
	rm -rf loader.o



.PHONY: all clean

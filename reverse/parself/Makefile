binutils_base=/home/ice/cto/tools/sources/tools/reverse/binutils-gdb
glog_base=/home/ice/gm/tools/logging/glog/install

libs_dir=-L${binutils_base}/install/lib -L${binutils_base}/libiberty -L${binutils_base}/zlib \
		-L${glog_base}

CXXFLAGS=
LDFLAGS=
include_dir=-I${PWD}/include -I${glog_base}
LDLIBS=-lbfd -liberty -ldl -lz -lglog

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

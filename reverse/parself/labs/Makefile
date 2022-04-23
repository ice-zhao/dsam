program=hello test.o

all: $(program)

hello: hello.c
	#gcc -m32 -o $@ $<
	gcc $< -o $@

test.o: test.c
	gcc -m32 -c $< -o $@

clean:
	rm -rf $(program)

.PHONY: all clean

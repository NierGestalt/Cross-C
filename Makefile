# Use the C++ compiler to link
LINK.o = $(LINK.cc)
# Flags to compile for the debugger
CXXFLAGS =-Wall -ggdb3

all: Main 

runtests: Main.o

clean:
	rm -f Main *.o

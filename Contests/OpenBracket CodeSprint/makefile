.DEFAULT_GOAL := test

FILES :=     \
	ViralAdvertising

CXX          := g++
INCLUDE      := /usr/include
CXXFLAGS     := -pedantic -std=c++11 -Wall -Weffc++


%.exe: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $(<:.exe=.c++)

clean:
	rm -f *.exe

test: $(FILES:=.exe)

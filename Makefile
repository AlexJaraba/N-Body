SHELL = /bin/sh
CC = gcc
FC = g77
CXX = g++

CXXFLAGS = -std=c++11 -Wall -O2 -I"C:/msys64/mingw64/include"

TARGET = few_body_nc

SRCS = src/main.cpp src/body.cpp src/solver.cpp src/io.cpp src/leapfrog.cpp src/globals.cpp src/Heuns.cpp
OBJS = $(SRCS:src/%.cpp=src/%.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

src/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

run: $(TARGET)
	./$(TARGET)

clean:
	cmd /c del /Q src\*.o $(TARGET).exe 2> NUL
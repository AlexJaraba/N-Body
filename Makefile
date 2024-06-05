CXX = g++
CXXFLAGS = -std=c++11 -Wall

TARGET = few_body_nc

SRCS = src/main.cpp src/body.cpp src/solver.cpp src/io.cpp src/leapfrog.cpp src/globals.cpp
OBJS = $(SRCS:.cpp=.o)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)


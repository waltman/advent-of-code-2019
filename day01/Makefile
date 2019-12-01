CXX = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = rocket_equation.o

rocket_equation: $(OBJECTS)

%.o: %.cpp
	$(CXX) $(CFLAGS) -c $<

rocket_equation: $(OBJECTS)
	$(CXX) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f rocket_equation

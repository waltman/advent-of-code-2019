CXX = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = secure_container.o

secure_container: $(OBJECTS)

%.o: %.cpp
	$(CXX) $(CFLAGS) -c $<

secure_container: $(OBJECTS)
	$(CXX) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f secure_container

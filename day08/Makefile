CXX = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = space_image_format.o

space_image_format: $(OBJECTS)

space_image_format.o:  space_image_format.cpp array2d.h array3d.h

%.o: %.cpp
	$(CXX) $(CFLAGS) -c $<

space_image_format: $(OBJECTS)
	$(CXX) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f space_image_format

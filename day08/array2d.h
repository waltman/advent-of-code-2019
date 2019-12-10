// DESCRIPTION: header file for the array2d class
//                                         
// Copyright(C) 6/13/2006 by Walt Mankowski
// walt@cs.drexel.edu
//                                         
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//                                         
// $Id: array2d.h 479 2008-01-17 02:39:10Z walt $
//

#ifndef ARRAY2D_H
#define ARRAY2D_H

// This is a class that encapsulates allocating a 2d array.  The only
// functions supported are adding and retrieving elements, and
// querying the dimensions.  It's assumed that the size of the array
// will not change after allocation.  For speed, no bounds checking is
// peformed.
//
// The "2d array" is really just a giant 1d array, where the offsets
// are calculated in the operator() method.

#include <iostream>
#include <string>
#include <string.h>

using std::ostream;
using std::string;
using std::endl;

template <typename T>
class array2d {

private:
        int _x_dim;
        int _y_dim;
        T *_data;
        void init(const int x, const int y, const int c = 0);

public:
        array2d() { _x_dim = _y_dim = 0; _data = NULL; }
        array2d(const int x, const int y) { init(x, y); }
        array2d(const int x, const int y, const int c) { init(x, y, c); }
        array2d(const array2d &rhs);
        ~array2d() { delete[] _data; }
        void resize(const int x, const int y);
        int x_dim() { return _x_dim; }
        int y_dim() { return _y_dim; }

        // this is used to get and set array elements
        T &operator() (const int x, const int y) {
                return _data[x * _y_dim + y];
        }

        // explicit get and set methods
        T &get(const int x, const int y) const {
                return _data[x * _y_dim + y];
        }
        void set(const int x, const int y, const T val ) {
                _data[x * _y_dim + y] = val;
        }

};

template <typename T>
inline
void array2d<T>::init(const int x_dim, const int y_dim, const int c) {
        _x_dim = x_dim;
        _y_dim = y_dim;
        _data = new T[x_dim * y_dim];
        memset(_data, c, x_dim * y_dim * sizeof(T));
}

template <typename T>
inline
void array2d<T>::resize(const int x_dim, const int y_dim) {
        // trash whatever was already there
        if (_data != NULL) {
                delete[] _data;
                _data = NULL;
        }
        init(x_dim, y_dim);
}

template <typename T>
inline
array2d<T>::array2d(const array2d &rhs) {
        printf("calling copy ctor\n");
        _x_dim = rhs._x_dim;
        _y_dim = rhs._y_dim;
        _data = new T[_x_dim * _y_dim];
        memcpy(_data, rhs.data, _x_dim * _y_dim * sizeof(T));
}

// allow sending an array2d to a stream, using matlab's formatting
template <typename T>
inline
ostream &operator<<(ostream &os, array2d<T> &m) {
        string s;
        char num[100];
        for (int i = 0; i < m.x_dim(); i++) {
                for (int j = 0; j < m.y_dim() - 1; j++) {
                        sprintf(num, "%f, ", m(i,j));
                        s += num;
                }
                sprintf(num, "%f;\n", m(i,m.y_dim()-1));
                s += num;
        }
        return os << s << "];" << endl;
}

inline
ostream &operator<<(ostream &os, array2d<int> &m) {
        string s;
        char num[100];
        for (int i = 0; i < m.x_dim(); i++) {
                for (int j = 0; j < m.y_dim() - 1; j++) {
                        sprintf(num, "%d, ", m(i,j));
                        s += num;
                }
                sprintf(num, "%d;\n", m(i,m.y_dim()-1));
                s += num;
        }
        return os << s << "];" << endl;
}

// allow sending a pointer to an array2d to a stream, using matlab's formatting
template <typename T>
inline
ostream &operator<<(ostream &os, array2d<T> *m) {
        string s;
        char num[100];
        for (int i = 0; i < m->x_dim(); i++) {
                for (int j = 0; j < m->y_dim() - 1; j++) {
                        sprintf(num, "%f, ", (*m)(i,j));
                        s += num;
                }
                sprintf(num, "%f;\n", (*m)(i,m->y_dim()-1));
                s += num;
        }
        return os << s << "];" << endl;
}

#endif

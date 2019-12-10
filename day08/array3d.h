// DESCRIPTION: header file for the array3d class
//                                         
// Copyright(C) 6/12/2006 by Walt Mankowski
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
// $Id: array3d.h 32 2006-08-03 13:05:17Z waltman $
//

#ifndef _ARRAY3D_H_
#define _ARRAY3D_H_

// This is a class that encapsulates allocating a 3d array.  The only
// functions supported are adding and retrieving elements, and
// querying the dimensions.  It's assumed that the size of the array
// will not change after allocation.  For speed, no bounds checking is
// peformed.
//
// The "3d array" is really just a giant 1d array, where the offsets
// are calculated in the operator() method.

template <typename T>
class array3d {

private:
        int _x_dim;
        int _y_dim;
        int _z_dim;
        T *_data;

public:
        array3d(int x, int y, int z);
        ~array3d() { delete[] _data; }
        int x_dim() { return _x_dim; }
        int y_dim() { return _y_dim; }
        int z_dim() { return _z_dim; }

        // this is used to get and set array elements
        T &operator() (int x, int y, int z) {
                return _data[x * (_y_dim * _z_dim) + y * _z_dim + z];
        }
};

template <typename T>
array3d<T>::array3d(int x_dim, int y_dim, int z_dim) {
        _x_dim = x_dim;
        _y_dim = y_dim;
        _z_dim = z_dim;
        _data = new T[x_dim * y_dim * z_dim];
        memset(_data, 0, x_dim * y_dim * z_dim * sizeof(T));
}

#endif

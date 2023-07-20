#!/usr/bin/python3

'''Defining a new class.'''


class Square:
    '''Representing a Square.'''

    def __init__(self, size=0):
        '''Initializing a new Square.'''

        if no isinstance(self, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
         self.__size = size   

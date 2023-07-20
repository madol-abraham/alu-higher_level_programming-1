#!/usr/bin/python3

'''Defining a new class.'''


class Square:
    '''Representing a new Square.'''

    def __init__(self, size):
        '''Initializing a new class.
        
        Args:
            size (int): The size of the new square.
        '''
        if no isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

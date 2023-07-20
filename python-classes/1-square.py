#!/usr/bin/python3

'''Defining a new class.'''


class Square:
    '''Representing a Square.'''
        
        def __init__(self, size):
        '''Initializing a new Square.
        
        Args:
            size (int): The size of the new square.
            '''
        self.__size = size

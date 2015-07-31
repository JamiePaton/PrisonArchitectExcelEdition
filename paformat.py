# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 01:51:10 2015

@author: Jamie
"""
TITLE = ''
VERSION = '0.0.0'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs
'    BEGIN "67 41"      Mat ConcreteFloor  Con 88.99933  Ind true  END'
'    BEGIN "67 41"      Mat ConcreteFloor  Con 88.99933  Ind  true  END'
'    BEGIN "68 37"      Mat PavingStone  Con 96.65614  END'
'    BEGIN "68 35"      Con 22.44483  END'

indoor_materials = {'Dirt': False,
                    'Sand': False,
                    'PavingStone': False,
                    'ConcreteFloor': True,
                    'Grass': False}

class Cell(object):
    def __init__(self, x, y, material='Dirt', condition=100.0, indoors=False):
        self.x = x
        self.y = y
        self.material = material
        self.condition = condition
        self.indoors = indoor_materials[self.material]
    
    def __repr__(self):
        if self.material != 'Dirt' and self.indoors is not False:
            return '    BEGIN "{} {}"      Mat {}  Con {}  Ind {}  END'.format(self.x, 
                                                                               self.y,
                                                                               self.material,
                                                                               self.condition,
                                                                               self.indoors)
        elif self.material != 'Dirt' and self.indoors is False:
            return '    BEGIN "{} {}"      Mat {}  Con {}  END'.format(self.x, 
                                                                       self.y,
                                                                       self.material,
                                                                       self.condition)
        else:
            return '    BEGIN "{} {}"      Con {}  END'.format(self.x, 
                                                               self.y,
                                                               self.condition)

def main(args):
    print Cell(67, 41, 'Dirt', condition=88.99933)
    print Cell(67, 41, 'ConcreteFloor', condition=88.99933)

    
class Testing(unittest.TestCase):
    """
    
    Methods
    -------
    
    
    Notes
    -----
    @given(parameter=hs.strategies.integers())
    
    def test_something(parameter):
        assert type(parameter) == int
    """


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    sys.exit(main(sys.argv))


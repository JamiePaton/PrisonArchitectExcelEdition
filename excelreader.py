# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:54:51 2015

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
import openpyxl
import xlwings
import os
import pprint
import paformat

def main(args):
    logger = logging.getLogger(__name__)
    logger.info('opening excel document')
    wb = xlwings.Workbook(os.path.join(os.getcwd(), 'prisontest.xlsx'), app_visible=False)
    
    colours = build_material_dict()
    materials = build_material_array()
    
#    print colours['(118, 147, 60)']
    logger.info('closing excel document')
    wb.close()

def build_material_array():
    pass

def build_material_dict():
    material_colours = {}
    n=1
    while True:
        material = xlwings.Range('Settings', 'A{}'.format(n)).value
        logger.debug('A{}:\t{}'.format(n, material))
        if material is None:
            break
        else:
            colour = xlwings.Range('Settings', 'B{}'.format(n)).color
            logger.debug('B{}:\t{}'.format(n, str(colour)))
            material_colours[str(colour)] = material
            n += 1
    return material_colours
    
    
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
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    sys.exit(main(sys.argv))


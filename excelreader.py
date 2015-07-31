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

import re
import string

def col2num(col):
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num

def main(args):
    logger = logging.getLogger(__name__)
    logger.info('opening excel document')
    wb = xlwings.Workbook(os.path.join(os.getcwd(), 'prisontest.xlsm'), app_visible=False)
    
    materials = build_material_dict()
#    pprint.pprint(materials)
    logger.info('reading cell colours')
    cells = []
#    for cell in xlwings.Range('Small', 'B2:C3'):
    for cell in xlwings.Range('Small', 'B2:CV81'):
#        print cell.get_address(False, False)
        address = re.split('(\d+)', cell.get_address(False, False))
#        print col2num(address[0]), address[1]
        c = paformat.Cell(col2num(address[0])-2, int(address[1])-2,
                                  material=materials[str(cell.color)])
        cells.append(c)
        
    wb.close()
    logger.info('saving cell data')
    with open('test.txt', 'w') as f:
        f.write('\n'.join([str(cell) for cell in cells]))
#    print colours['(118, 147, 60)']
    logger.info('closing excel document')

    

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
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    sys.exit(main(sys.argv))


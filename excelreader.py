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


def main(args):
    wb = xlwings.Workbook(os.path.join(os.getcwd(), 'prisontest.xlsx'), app_visible=False)
    print xlwings.Range('Small', 'E2').color
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


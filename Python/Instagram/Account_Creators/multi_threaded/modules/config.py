
"""
    author: Sylar
    Configuration files
"""
import os

import logging

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(BASE_DIR, 'Assets' )
MODULES_DIR = os.path.join(BASE_DIR, 'modules' )

Config = {

}
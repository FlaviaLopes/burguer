#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
from distutils.sysconfig import get_python_lib
import os
import sys

sys.path.append(os.curdir)
from data import *

AUTHOR = 'Flavia Lopes'
SITENAME = 'Junky Hamburgueria'
SITETITLE = 'Desde 1998'
SITEDESCRIPTION = '''Uma lanchonete completa.'''
KEYWORDS = '''lanchonete,fast food,pizzaria'''
SITEURL = ''
RELATIVE_URLS = True
DEFAULT_METADATA = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/capa/logo.png'
}
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt_BR'
CURRENTYEAR = date.today().year

### adicionado ###
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ['.git']
THEME = 'theme/burguer'

LOAD_CONTENT_CACHE = False

############## Plugins #################
PLUGIN_PATHS = [get_python_lib()]
PLUGINS = [
    'pelican_image_process',
]

# image_process
IMAGE_PROCESS_DIR = 'derivees'

IMAGE_PROCESS = {
    'crisp': {
        'type': 'responsive-image',
        'srcset': [('1x', ["scale_in 800 600 True"]),
                   ('2x', ["scale_in 1600 1200 True"]),
                   ('4x', ["scale_in 3200 2400 True"]),
                   ],
        'default': '1x',
    },
    'large': {
        'type': 'responsive-image',
        'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, (min-width: 769px) 718px, 100vw',
        'srcset': [('600w', ["scale_in 600 450 True"]),
                   ('800w', ["scale_in 800 600 True"]),
                   ('1600w', ["scale_in 1600 1200 True"]),
                   ],
        'default': '800w',
    },
    'small': {
        'type': 'responsive-image',
        'sizes': '(min-width: 992px) 780px, (min-width: 769px) 620px, '
                 '\ (min-width: 480px) 460px, 100vw',
        'srcset': [
            ('320w', ["scale_in 380 200 True"]),
            ('640w', ["scale_in 760 400 True"]),
            ('960w', ["scale_in 1140 600 True"]),
            ('1280w', ["scale_in 1520 800 True"]),
            ('1920w', ["scale_in 2280 1200 True"]),
            ('2560w', ["scale_in 3040 1600 True"]),
        ],
        'default': '250w',
    }
}

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
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
DEFAULT_METADATA = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/capa/logo.png'
}
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt_BR'
CURRENTYEAR = date.today().year

### adicionado ###
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']
THEME = 'theme/burguer'

LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


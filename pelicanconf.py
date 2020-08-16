#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Flavia Lopes'
SITENAME = 'Junky Hamburgueria'
SITETITLE = 'Desde 1998'
SITEDESCRIPTION = '''Uma lanchonete completa.'''
KEYWORDS = '''lanchonete,fast food,pizzaria'''
SITEURL = ''
DEFAULT_METADATA = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/logo.png'
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

# -------- Header content -------------- #
HEADER = {
    'title': 'Apresentando...',
    'subtitle': 'Burgão Tropical',
    'text': '''Alface, Calabresa, Cebola, Duas Fatias de Queijo, Filé de Frango 80g, Maionese, Molho Especial, Pão, Queijo Cremoso, Tomate'''
}
# -------- First Section content -------------- #
FIRST_CONTENT_FEATURED = {
    'image': 'feature_bg.jpg',
    'name': 'x-frango',
    'desc': 'pão, frango, ovo, alface, milho, presunto, queijo'
}
FIRST_CONTENT_SIGNATURE = {
    'image': 'signature.jpg',
    'name': 'x-bacon',
    'desc': 'pão, bacon, ovo, alface, milho, presunto, queijo'

}
# -------- Second Section content -------------- #
SECOND_CONTENT_CLASSIC = {
    'image': 'classic_bg.jpg',
    'name': 'x-tudo',
    'desc': 'pão, frango, bacon, calabreza, carne, ovo, alface, milho, presunto, queijo'
}

SECOND_CONTENT_CAROUSEL = [
    {
        'image': 'mais_vendido1.jpg',
        'name': 'x-salada',
        'desc': 'pão, tomate, ovo, alface, milho, presunto, queijo'
    },
    {
        'image': 'mais_vendido2.jpg',
        'name': 'sanduba tropical',
        'desc': 'pão, abacaxi, bacon, carne, presunto, queijo'
    },
    {
        'image': 'mais_vendido3.jpg',
        'name': 'à moda da casa',
        'desc': 'pão, carne, bacon, calabraza, tomate, ovo, alface, milho, presunto, queijo'
    }
]

# -------- Third Section content -------------- #
THIRD_CONTENT_CAROUSEL = [
    {
        'image': 'large_slider_img.jpg',
        'name': 'bebidas variadas',
        'desc': 'refrigerantes, sucos naturais, vitaminas, cerveja.'
    },
    {
        'image': 'large_slider_img.jpg',
        'name': 'caldos e refeições',
        'desc': 'caldo de carne, caldo de frango, filé com batata frita'
    },
    {
        'image': 'large_slider_img.jpg',
        'name': 'pizzas',
        'desc': 'pizzas variadas: mussarela, carne seca, bacon, vegetariana, calabreza.'
    }
]

# -------- Footer content -------------- #
LOCK_TITLE = '''Servindo mais do que apenas lanches desde 1998.'''
LOCK_TEXT = '''Confira nosso horário de atendimento, localização e cardápio logo abaixo.'''

# Contact
CONTACT = {
    'email': 'email@email.com',
    'phone': '5593999999999'
}
# Address
ADDRESS = {
    'address': 'Rua Imaginária, nº 100, Localidade',
    'cep': '68165-000',
    'city': 'Rurópolis - PA'
}

# Social
SOCIAL = (
    ('facebook', 'https://www.facebook.com/flavialopesads'),
    ('twitter', 'https://www.twitter.com/_flavialopes_'),
    ('instagram', 'https://www.instagram.com/_flavialopes_'),
)

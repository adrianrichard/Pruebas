from distutils import setup
import py2exe

setup (

options = {'py2exe'	:{ 'bundle_flies': 1,	'compressed': True}},
Windows = [{'script' : "analizadorlexico.py"}],
zipfile = None
)

# 'icon_resources'	:	[(O, 'G:/Pruebas/'
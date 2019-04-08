try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'questionmaker (encuestador)',
  'author': 'Iñigo Gonzalez',
  'url': 'https://github.com/igponce/questionmaker',
  'download_url': 'https://github.com/igponce/questionmaker',
  'author_email': 'igponce @at@ gmail .dot. com',
  'install_requires': [ 'pytest', 'pyyaml' ],
  'packages': ['questionmaker'],
  'scripts': [],
  'name': 'questionmaker'
}

setup (**config)

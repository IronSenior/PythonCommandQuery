from distutils.core import setup

setup(
  name = 'plato_cqrs',
  packages = ['plato_cqrs'],
  version = '1.1',
  license='GPL-3',
  description = 'Simple CQRS implementation',
  author = 'Pepe Márquez Doblas',
  author_email = 'pepemarquezof@gmail.com',
  url = 'https://github.com/IronSenior/PythonCommandQuery',
  download_url = 'https://github.com/IronSenior/PythonCommandQuery/archive/refs/tags/1.1.tar.gz',
  keywords = ['CQRS', 'COMMAND', 'QUERY'],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)
import sys
from setuptools import setup, find_packages


packages = find_packages()

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('CHANGES.rst', 'r', encoding='utf-8') as f:
    changes = f.read()


setup(name='async-yandex-music',
      version='0.1.2',
      author='Il`ya Semyonov : therrors',
      author_email='Ilya@marshal.by',
      license='LGPLv3',
      url='https://github.com/therrors/async-yandex-music-api/',
      keywords='python yandex music api wrapper library async питон пайтон яндекс музыка апи обёртка библиотека',
      description='Делаю то, что по определённым причинам не сделала компания Yandex.',
      long_description=f'{readme}\n{changes}',
      packages=packages,
      install_requires=['aiohttp'],
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Natural Language :: Russian',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Multimedia :: Sound/Audio',
          'Topic :: Internet',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ],
      project_urls={
          'Code': 'https://github.com/MarshalX/yandex-music-api',
          'Documentation': 'https://yandex-music.readthedocs.io',
          'Chat': 'https://ttttt.me/yandex_music_api',
          'Codecov': 'https://codecov.io/gh/MarshalX/yandex-music-api',
          'Codacy': 'https://www.codacy.com/manual/MarshalX/yandex-music-api',
      })

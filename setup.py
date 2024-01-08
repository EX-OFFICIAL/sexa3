from setuptools import setup
setup(
   name='sexa3',
   version='2.0',
   description='tools for disassembling and reassembling python code',
   author='mr. ex',
   author_email='itzmenoyon@gmail.com',
   packages=['sexa3'],
   entry_points={"console_scripts": ["sexa3=sexa3:main"]}
)

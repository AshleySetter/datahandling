from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='DataHandling',
      version='1.0',
      description='Python package with functions for data analysis',
      author='Ashley Setter',
      auther_email='A.Setter@soton.ac.uk',
      url=None,
      packages=['DataHandling'],
      package_dir={'DataHandling': 'DataHandling',
                   'LeCroy': 'LeCroy'
      },
      install_requires=requirements,
)

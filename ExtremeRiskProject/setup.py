from distutils.core import setup

setup(
    name='Extreme Risk',
    version='0.0.0.1',
    author='Eric Hill and Seabury Neucollins',
    author_email='',
    packages=['ExtremeRisk', 'ExtremeRisk.Main'],
#   scripts=['Setup Path Script'],
#   url='',
    license='license.txt',
    description='Extreme Risk Project',
    long_description=open('readme.txt').read(),
#    install_requires=[
#        "Django >= 1.1.1",
#        "caldav == 0.1.4",
#    ],
)

# Distribution files and projects inspired by http://guide.python-distribute.org/creation.html
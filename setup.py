import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
requires = ["Django>=1.4.1", "xlwt>=0.7.5"] ## open(os.path.join(os.path.dirname(__file__), 'requirements.tx')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-export-xls',
    version='0.1.1',
    packages=['export_xls'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to export data to an excel file.',
    long_description=README,
    url='http://github.com/Daiech/django-export-xls',
    author='Mauricio Aizaga',
    author_email='mauricioaizaga@gmail.com',
    install_requires=requires,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
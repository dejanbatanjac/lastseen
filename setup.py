from setuptools import setup, find_packages
import lastseen

setup(
    name='lastseen',
    version=str(lastseen.__VERSION__),
    packages=find_packages(),
    description='last seen SO script',
    url='https://programming-review.com',
    license="MIT",
    install_requires=['lxml', 'requests'],
    entry_points={
        'console_scripts': ['lastseen=lastseen.lastseen:main'],
    }    
)

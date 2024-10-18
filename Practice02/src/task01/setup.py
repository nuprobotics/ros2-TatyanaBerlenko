from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'task01'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),

    ],
    install_requires=['setuptools', 'std_msgs'],
    zip_safe=True,
    maintainer='maintainer',
    maintainer_email='your.email@example.com',
    description='Task01 package',
    license='TBD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'receiver = task01.receiver:main',
        ],
    },

)
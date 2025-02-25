from setuptools import setup
from glob import glob
import os

package_name = 'arena_gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "sdf"), glob('sdf/*')),
        (os.path.join('share', package_name, "meshes"), [log for log in glob('meshes/*') if not os.path.isdir(log)]),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='svenbecker',
    maintainer_email='sven.becker@epfl.ch',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

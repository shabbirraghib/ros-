from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'image_conversion'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/image_conversion']),
        ('share/image_conversion', ['package.xml']),
        (os.path.join('share', 'image_conversion', 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shabbir',
    maintainer_email='shabbir@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_conversion_node = image_conversion.image_conversion_node:main'        ],
    },
)

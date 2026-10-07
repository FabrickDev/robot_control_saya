from setuptools import find_packages, setup

package_name = 'robot_control_saya'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='faqisna',
    maintainer_email='faqisna@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'inverse_kinematics = robot_control_saya.inverse_kinematics:main',
            'pelajaran = robot_control_saya.pelajaran:main',
        ],
    },
)

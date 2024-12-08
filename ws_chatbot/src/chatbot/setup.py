from setuptools import find_packages, setup

package_name = 'chatbot'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'nltk',],
    zip_safe=True,
    maintainer='celia123',
    maintainer_email='cecilia.goncalves@sou.inteli.edu.br',
    description='Chatbot para controle de robôs no ROS 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'chatbot = chatbot.chatbot:main',
        ],
    },
)

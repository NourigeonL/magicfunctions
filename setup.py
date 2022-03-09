from setuptools import find_packages, setup
setup(
    name='magicLib',
    packages=find_packages(include=['magicLib']),
    version='0.1.0',
    description='The magic library',
    author='Louis Nourigeon',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
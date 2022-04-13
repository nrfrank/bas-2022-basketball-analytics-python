from setuptools import find_packages, setup

setup(
    name='src',
    packages=[p for p in find_packages() if 'bas' in p],
    version='0.1.0',
    description='Sample Python project for Basketball Analytics Summit 2022 workshop “How to Begin Your Journey: Hands on Basketball Analytics',
    author='Nathan Frank',
    license='MIT',
    install_requires=[],
    python_requires='>=3.9',
    extras_require={
        'dev': [
            'coverage',
            'pytest',
            'pytest-tldr'
        ]
    }
)

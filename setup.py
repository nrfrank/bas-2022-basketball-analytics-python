from setuptools import find_packages, setup

from bas import __version__

setup(
    name='bas',
    packages=[p for p in find_packages() if 'bas' in p],
    version=__version__,
    description='Sample Python project for Basketball Analytics Summit 2022 workshop “How to Begin Your Journey: Hands on Basketball Analytics',
    author='Nathan Frank',
    license='MIT',
    install_requires=[
        'basketball-reference-scraper==1.0.30',
        'numpy==1.21.0',
        'pandas==1.3.1',
        'seaborn==0.11.2'
    ],
    python_requires='>=3.9',
    extras_require={
        'dev': [
            'coverage',
            'ipykernel',
            'ipywidgets',
            'jupytext',
            'notebook',
            'pytest',
            'pytest-tldr'
        ]
    }
)

from setuptools import setup, find_packages

setup(
    name="code-formatter-pro-moon-20260530_132840",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'code=code:main',
        ],
    },
)

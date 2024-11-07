import os
from setuptools import setup, find_packages

# Read the README file
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
        return f.read()

# Read version from pyproject.toml
def get_version():
    with open('pyproject.toml', encoding='utf-8') as f:
        for line in f:
            if line.startswith('version = '):
                return line.split('=')[1].strip().strip('"')
    return '0.1.0'  # fallback version

setup(
    name="logic-gates",
    version=get_version(),
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python implementation of digital logic gates",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/logic-gates",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
    python_requires=">=3.8",
    install_requires=[
        # List your project's dependencies here
        # e.g., "numpy>=1.20.0",
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.7.0',
            'isort>=5.12.0',
            'flake8>=6.1.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'logic-gates=logic_gates.gates:main',
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/logic-gates/issues",
        "Documentation": "https://github.com/yourusername/logic-gates/wiki",
        "Source Code": "https://github.com/yourusername/logic-gates",
    },
)

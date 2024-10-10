from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="FileXfer",
    version="1.0.0",
    author="Al-Areef",
    description="A terminal-based file transfer tool that works across Windows, macOS, and Linux platforms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NUCCASJNR/FileXfer",
    packages=find_packages(),
    install_requires=[
        "click",
        "tqdm",
        "cryptography",
        "paramiko",
        "pytest",
        "mocket"
    ],
    entry_points={
        'console_scripts': [
            'filexfer=filexfer.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)

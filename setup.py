from setuptools import setup

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="hash_calc",            
    version="1.1.0",
    author="5f0",
    url="https://github.com/5f0ne/hash-calc",
    description="Calculates MD5 and SHA256 hashes for a given file or bytes",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=["hash_calc"],
    install_requires=[
        
    ],
    entry_points={
        "console_scripts": [
            "hash_calc = hash_calc.__main__:main"
        ]
    },
    data_files=[]
)
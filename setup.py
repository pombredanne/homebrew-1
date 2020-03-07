from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="homebrew",
    version="0.1.11",
    description="Homebrew wrapper",
    long_description=readme,
    author="Iwan in 't Groen",
    author_email="iwanintgroen@gmail.com",
    url="https://github.com/igroen/homebrew",
    packages=find_packages(),
    tests_require=["pytest"],
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["hb=homebrew.command_line:main"]},
    license="ISCL",
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3.7",
    ],
)

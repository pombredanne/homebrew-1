from setuptools import setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read().replace(".. :changelog:", "")

requirements = []
test_requirements = ["pytest"]


setup(
    name="homebrew",
    version="0.0.35",
    description="Homebrew wrapper",
    long_description=readme + "\n\n" + history,
    author="Iwan in 't Groen",
    author_email="iwanintgroen@gmail.com",
    url="https://github.com/igroen/homebrew",
    packages=["homebrew"],
    package_dir={"homebrew": "homebrew"},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords="homebrew",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    tests_require=test_requirements,
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["hb=homebrew.command_line:main"]},
)

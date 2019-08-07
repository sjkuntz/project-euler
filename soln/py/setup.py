import setuptools

version = '0.0.1'

install_requires = [
    'setuptools',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="project-euler-sjkuntz",
    version=version,
    author="Steven Kuntz",
    author_email="stevenjkuntz@gmail.com",
    description="Common functions for Project Euler problems.",
    long_description=long_description,
    long_description_content_type="markdown",
    url="https://github.com/sjkuntz/project-euler",
    py_modules=['euler'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
)

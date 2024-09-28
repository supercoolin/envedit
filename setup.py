from setuptools import setup, find_packages

setup(
    name="envedit",
    version="1.1.0",
    description="A custom Python project to edit environment variables.",
    author="Colin Evrard",
    author_email="colin.evrard.134@gmail.com",
    url="https://github.com/supercoolin/envedit",  # If you have a repository
    packages=["envedit"],
    scripts=["scripts/editvars.py"],
    install_requires=[
        # List your dependencies here, e.g.,
        #'pandas>=2.2.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)

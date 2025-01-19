import subprocess

subprocess.run(["pip", "install", "setuptools"])

from setuptools import setup, find_packages

setup(
    name="techtonique_cli",  # Replace with your package name
    version="0.1.0",  # Version of your package
    packages=find_packages(where="cli"),  # Automatically find packages in the cli directory
    package_dir={"": "cli"},  # Specify the package directory
    entry_points={
        "console_scripts": [
            "techtonique=cli.cli:cli",
        ],
    },
    install_requires=[
        "click",  # Add any other dependencies your CLI needs
        "requests",
        # Add other dependencies here
    ],
    description="A CLI tool for Techtonique API",  # Short description of your package
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",
    url="https://github.com/Techtonique/cli/",  # URL to your project
    author="Techtonique",  # Your name
    author_email="support@techtonique.net",  # Your email
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if using a different license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
)

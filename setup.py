"""Setup configuration for socratic-docs"""

from setuptools import setup, find_packages

setup(
    name="socratic-docs",
    version="0.1.0",
    description="Automated documentation generation for projects",
    author="Socratic Team",
    author_email="team@socratic.dev",
    url="https://github.com/Nireus79/Socratic-docs",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "pytest>=6.0",  # Core testing package
        "pytest-xdist",  # Multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "pytest-mock",  # For creating and using mocks
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
        "pytest-benchmark",  # For performance tests
    ],
    "lint": [
        "black>=25.1.0,<26",  # Auto-formatter and linter
        "mypy>=1.15.0,<2",  # Static type analyzer
        "types-requests",  # Needed for mypy type shed
        "types-setuptools",  # Needed for mypy type shed
        "flake8>=7.1.2,<8",  # Style linter
        "flake8-pydantic",  # For detecting issues with Pydantic models
        "flake8-type-checking",  # Detect imports to move in/out of type-checking blocks
        "isort>=5.13.2,<6",  # Import sorting linter
        "mdformat>=0.7.22",  # Auto-formatter for markdown
        "mdformat-gfm>=0.3.5",  # Needed for formatting GitHub-flavored markdown
        "mdformat-frontmatter>=0.4.1",  # Needed for frontmatters-style headers in issue templates
        "mdformat-pyproject>=0.0.2",  # Allows configuring in pyproject.toml
    ],
    "doc": [
        "Sphinx>=6.1.3,<7",  # Documentation generator
        "sphinx_rtd_theme>=1.2.0,<2",  # Readthedocs.org theme
        "towncrier>=19.2.0,<20",  # Generate release notes
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools>=75.6.0",  # Installation tool
        "setuptools-scm",  # Installation tool
        "wheel",  # Packaging tool
        "twine==3.8",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="ape-solidity",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Plugin for Ape Ethereum Framework for compiling Solidity contracts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ApeWorX Ltd.",
    author_email="admin@apeworx.io",
    url="https://github.com/ApeWorX/ape-solidity",
    include_package_data=True,
    install_requires=[
        "py-solc-x>=2.0.2,<3",
        "eth-ape>=0.8.4,<0.9",
        "ethpm-types",  # Use the version ape requires
        "eth-pydantic-types",  # Use the version ape requires
        "packaging",  # Use the version ape requires
        "requests",
    ],
    python_requires=">=3.9,<4",
    extras_require=extras_require,
    py_modules=["ape_solidity"],
    entry_points={
        "ape_cli_subcommands": [
            "ape_solidity=ape_solidity._cli:cli",
        ],
    },
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ape_solidity": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)

from distutils.core import setup
setup(
    name = "ecosystem-nix-shared",
    packages = ["EDANixShared"],
#    packages = find_packages(),
    version = "0.0.1a1",
    description = "Nix domain in PythonEDA",
    author = "rydnr",
    author_email = "github@acm-sl.org",
    url = "https://github.com/rydnr/pythoneda-nix-shared",
    download_url = "https://github.com/rydnr/pythoneda-nix-shared/releases",
    keywords = ["eda", "ddd"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    install_requires=[
    ],
    long_description = """\
PythonEDA Nix Shared
--------------------

This package includes a shared kernel for abstractions about Nix.

This is what PythonEDA Nix Shared provides:
- EDANixShared/*: Some error classes.
- EDANixShared/python/nix_python_package: A Python package available in Nix.
- EDANixShared/python/nix_python_package_repo: The repository of Python packages in Nix.
""",
    tests_require=['pytest']
)

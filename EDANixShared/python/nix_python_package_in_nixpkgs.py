from PythonEDA.event import Event
from PythonEDA.value_object import primary_key_attribute

class NixPythonPackageInNixpkgs(Event):
    """
    Represents the event when a Python package is already available in nixpkgs.
    """

    def __init__(
        self,
        pkg: PythonPackage
    ):
        """Creates a new NixPythonPackageInNixpkgs instance"""
        self._python_package = pkg

    @property
    @primary_key_attribute
    def python_package(self):
        return self._python_package

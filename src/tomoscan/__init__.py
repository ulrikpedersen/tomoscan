from importlib.metadata import version

__version__ = version("tomoscan")
del version

__all__ = ["__version__"]

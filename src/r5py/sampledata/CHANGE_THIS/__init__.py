#!/usr/bin/env python3


"""Sample data set for r5py, covering CHANGE_THIS, downloaded upon first access."""


from r5py.util.data_set import DataSet


__all__ = [
    "__version__",
    "example",
]

__version__ = "0.1.0"


BASE_URL = f"https://github.com/r5py/CHANGE_THIS/raw/v{__version__}/data/"

example = DataSet(
    f"{BASE_URL}/example.zip",
    "57d0d5f3359cbd0d42cc7467c51ec9b14e0c9dc1665308246644fbc3bddd9a1f",
)

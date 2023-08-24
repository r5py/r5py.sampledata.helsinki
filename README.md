# TEMPLATE for r5py sample data sets

This is a template repository for creating new r5py sample data sets. R5py
sample data sets are [namespace
packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages)
underneath the namespace `r5py.sampledata`.

To create a new sample data set, 

- create a repository from this template, and adjust `pyproject.toml` (look
  out for ‘CHANGE_THIS’, and also 
- adapt the list of authors accordingly. Then,
- rename the directory `src/r5py/sampledata/CHANGE_THIS` to a *lowercase*
  name reflecting the content of the sample data set (e.g., the name of the
  city it covers). 
- Add the sample files to `data/`,
- and edit `src/r5py/sampledata/NOW_CHANGED_DIRECTORY_NAME/__init__.py`: 
    - change `BASE_URL`, and
    - include one variable per data set that is an
      `r5py.util.data_set.DataSet()` with the source url and the SHA256
      checksum as parameters, and
    - add the data set variable to `__all__`. Then,
    - update the `__version__` string, and
- edit this README to tell about the data set. Also, don’t forget to
- change `CHANGE_THIS` in `tests/test_data_sets.py`.

Once you have added all data sets, add a tag (equal to `f"v{__version__}`) and
push the changes and tags.

For a detailed example, see
[r5py.sampledata.sao_paulo](https://github.com/r5py/r5py.sampledata.sao_paulo).

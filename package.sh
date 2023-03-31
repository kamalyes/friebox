rm -rf build dist friebox.egg-info
python -m pip install --user --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
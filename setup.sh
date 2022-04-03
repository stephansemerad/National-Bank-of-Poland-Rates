# 1. Run the following command
python setup.py sdist bdist_wheel

# 2. install twine
python -m pip install twine

# 3. Upload the package to PyPi
twine upload dist/*
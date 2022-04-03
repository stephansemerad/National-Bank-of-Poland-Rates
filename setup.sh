# 1. Run the following command
python setup.py sdist bdist_wheel

# 2. install twine
python -m pip install twine

# 3. Upload the package to PyPi
twine upload dist/*

# 4. Remove 
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q pln_fx.egg-info

# 5. Update
# Change Version number in setup.py and then run the commands again
python setup.py sdist bdist_wheel
twine upload dist/*
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q pln_fx.egg-info
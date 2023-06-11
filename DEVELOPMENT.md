# Contributing to this library


In order to contribute you need to install a few things


1. First make sure you have python3 installed. You can check by running the following command in your terminal

```
python3 -m pip install --upgrade pip
```

2. Install the build packages
```
python3 -m pip install --upgrade build
```

3. Then run the following command at the root of the project to build the package
```
SLASHML_DIR='.' python3 -m build
```

The `SLASHML_DIR` will pick the root dir and build the package inside the dist folder in the root.


4. Pushing the package to pypi

```
python3 -m pip install --upgrade twine
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

Make sure dist only has the newly build package, otherwise the command will try to deploy all of the packages.

The above command will prompt you for a username and a password. You will need developer access to the pypi repo to be able to push the package. Contact @eff-kay for this.


5. Test the package by 

```
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple slashml
```

This command will pull the latest from test.pypi.org and the extra-index-url will pull the dependencies from pypi.org. This is because the slashml package depends on other packages that are not on test.pypi.org.




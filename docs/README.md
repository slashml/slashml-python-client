Create a new venv, and install the requirements file


Then run the following to compile the docs


```bash
make dirhtml
```

you can verify the updates by running the following command

```bash
python -m http.server --directory _build/dirhtml
```


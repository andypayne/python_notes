

## Requirements

### pipreqs

Use [pipreqs](https://github.com/bndr/pipreqs) for showing top-level dependencies to avoid `requirements.txt` files getting bulky. Basic installation and usage:

```shell
pip install pipreqs

pipreqs --print
```


### pigar

TODO


### black

[black](https://github.com/psf/black) vim integration:

https://black.readthedocs.io/en/stable/integrations/editors.html

The first time you edit a file and run `:Black`, the black plugin will run some setup code. Be sure to deactivate any existing python environments before doing that the first time, assuming you installed the black pip file globally.


### pipenv

[Installing:] https://pipenv.pypa.io/en/latest/install/#installing-pipenv

```
pip install --user pipenv
```

or

```
pip install --user pipx
pipx install pipenv
```


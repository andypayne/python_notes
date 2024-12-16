
## Pyenv

[pyenv](https://github.com/pyenv/pyenv) is a tool for managing multiple versions of Python.

List of commands: [commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

Install on mac with homebrew:
```
brew update
brew install pyenv
```

Install a version with:
```
pyenv install 3.10.4
```

Activate for a local project with:
```
pyenv local 3.10.4
```

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

#### Install

[Installing:] https://pipenv.pypa.io/en/latest/install/#installing-pipenv

```
pip install --user pipenv
```

or

```
pip install --user pipx
pipx install pipenv
```

#### Upgrade

```
pip install --user --upgrade pipenv
```

#### Use

Install a package into a fresh project, and pipenv will automatically create a Pipfile for the project.

```
mkdir myproject
cd myproject
pipenv install <package>
```

Activate with:

```
pipenv shell
```

I use my [renv](https://github.com/andypayne/dotfiles-local/blob/master/aliases.local#L110) alias to activate the environment.

Or run a command with:

```
pipenv run
```

This repo will host book content for CHEM502 Chemical Data, Discovery and Design.

The book uses [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)

The repo will (hopefully) be available on [Binder](https://mybinder.org) - link to follow...


To create a conda environment, use the environment.yml file.

`conda env create --file environment.yml`

The requirements_conda[_mac].txt files might also work to create a conda environment with the same versions as the code was created:

`conda create --name <env> --file requirements_conda[_mac].txt`

but using the yaml file via the earlier command is probably less likely to cause issues.


The book is copyright © 2024-25 Sam Chong and is released under under the CC BY-NC-SA 4.0.
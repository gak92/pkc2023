# Using Conda Environment

## Key reasons why creating conda environments is necessary/useful

- Dependency and version management: Conda environments allow you to isolate different projects that may have conflicting dependencies or require different versions of packages. This avoids dependency clashes.

- Reproducibility: Environments make it easy to exactly replicate the software environment used for a project/analysis. This ensures reproducible results.

- Code sharing: Environments allow sharing code/notebooks with others while bundling all dependencies. Avoid issues caused by missing or wrong package versions.

- Testing different stacks: You can test different package combinations and Python/IPython versions easily using separate environments without interfering with system setup.

- Package conflicts: Some packages conflict in how they use or install dependencies. Environments prevent such issues from arising.

- Clean project separation: Keeping each project activitiesisolated in its own environment prevents namespace pollution and clutter. Easy to switch between projects.

- System stability: Environments avoid the risk of new package versions breaking existing projects or the system Python setup.

- Temporary setups: Useful for experimenting with packages without permanently changing the system configuration. Easy clean up by deleting env.

So in summary, conda environments make dependency and version management clean and reproducible for both development and production environments.

## Using basics conda commands

> check conda environment list: `conda env list`

> check which packages are installed: `conda list`

> check conda version: `conda info`

> update conda: `conda update conda`

> install package in conda: `conda install python`

> update a package: `conda update python`

## Create new conda environment

> create new environment: `conda create -n pandas_env`

> check if new env created:  `codna env list`

## Activate env

> activate  the environment: `conda activate pandas_env`

## Copy of an env
> create copy of an environment: `conda create --clone pandas_env --name pandas_env2`

## Save an env and create from file
> save environment to text file: `conda list --explicit > pandas_env.txt`

> recreate environment from txt file: `conda install --file pandas_env.txt`

## Install packages from the file
> install packages from the file: `conda install --yes --file  requirements.txt`

## Deactivate the env
> deactivate the environment: `deactivate`

> create env and install package: `conda create -n bio_env biopython`

## Search and remove the package and env
> search the package: `conda search python`

> remove environment: `conda remove --name bio_env --all`

> remove package from environment: `conda remove matplotlib`

## Install specific version of package
> install specific version of pacakge in the env: `conda install --channel conda-forge python=3.4`
or
`conda install python=3.4 --channel conda-forge --channel bioconda`

## Rename the env
> rename the environment: create clone and remove the old env


## To check where is python install
> where is python: `where python`

## Conda cheat sheet
- https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf

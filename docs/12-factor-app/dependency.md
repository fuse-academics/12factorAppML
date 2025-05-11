## 2. Dependency Management

>Explicitly declare and isolate dependencies

### Pip & Virtualenv

Python comes pre-installed with PIP (Python Package Installer) for declaration and Virtualenv for Isolation. PIP allows installation of packages from [Python Package Index (PyPI)](https://pypi.org/)

Create a virtual environment to manage dependencies

`python -m venv env`

Activate the Virtual Environmnet

- on Windows: `env\Scripts\activate`
- On macOS/Linux:`source env/bin/activate`

Install Dependencies

- by listing the pacakges: `pip install numpy scipy pandas scikit-learn matplotlib seaborn`
- by using requirement file: `pip install -r requirements.txt`
- from local git repo: `pip install git+file:///path/to/your/package#egg=package-name`
- from remote git repo optionally specifying branch: `pip install git+ssh://git@github.com:Username/Project.git@master`

To work with specific python version you'd have to call pip from the specific python version installed to the system eg:

`python3.12 -m pip install numpy`

### Anaconda/Miniconda

Many developer also prefer to use [Anaconda](https://www.anaconda.com/download/) or minimal version [miniconda](https://docs.anaconda.com/miniconda/) for package and environment management. Ananconda distribution comes with many preinstalled package and many others can be installed from [Anaconda](https://anaconda.org/)
Please follow and install the instructions mentioned in their site. If you installed everything correctly you'll be able to start conda environment by typing `conda init` in the terminal.

Creating a New Environment, with a specific python version

`conda create -n myenv python=3.8`

Activate your environment with: `conda activate myenv`

Deactivate your environment with: `conda deactivate`

Install pacakges into environment, you can also specify channels or install a local file

```bash
conda install numpy pandas matplotlib
conda install -c conda-forge scikit-learn
conda install /path/to/package-file.tar.bz2
```

Managing multiple environments

```bash
conda env list
conda env remove -n myenv
conda update conda
```

Export your environment to YAML file for sharing or create from an existing YAML file

```bash
conda env export > environment.yml
conda env create -f environment.yml
```

### Poetry

[Poetry](https://python-poetry.org/) is a mordern packaging and dependency management tool that aims to simplify the process of managing project dependencies and publishing packages to [PyPI](https://pypi.org/). It uses a single file, pyproject.toml, to manage both project metadata and dependencies, making it easier to maintain and understand the project structure.

Installation: `pip install poetry --user --upgrade --pre`

Creating a new Project

```bash
poetry new poetry-demo-new
poetry new --src poetry-demo-new-src
```

Initializing Existing project

```bash
cd poetry-demo-init
poetry init
```

Poetry either uses your configured virtualenvs or creates its own to always be isolated from your system.

```bash
cd poetry-demo-transition
poetry init
poetry add `cat requirements.txt`
poetry add --dev `cat dev_requirements.txt`
poetry export -f requirements.txt --output requirements.txt
poetry show --tree
```

Run Commands within poetry virtual environment

`poetry run pytest`

Ability to work within an activated virtual env

`poetry shell`

Environment Commands

```bash
poetry env info
poetry env list
poetry env use 3.8
poetry env remove 3.7
```

You need to have specific version of python installed in your system in order for poetry to use it

Other useful commands

```bash
poetry search dynaconf
poetry add dynaconf
poetry add coverage --dev
poetry update
poetry update pytest
poetry remove dynaconf
poetry remove coverage --dev
poetry install
poetry install --no-dev
poetry export --without-hashes -o requirements.txt
poetry export --dev --without-hashes -o dev_requirements.txt
```

Easily build and package your projects with a single command. Supports source distribution and wheels.

`poetry build`

Make your work known by publishing it to PyPI. You can also publish on private repositories.

`poetry publish`

</details>

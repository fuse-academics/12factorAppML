## 3. Configuration Management

> Store config in the environment

An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc). This includes resource handles to the databases or backing services, credentials to external services such as Amazon S3 or API Keys, per-deploy values such as the canonical hostname for the deploy and so on.

### dotenv

[Python-dotenv](https://github.com/theskumar/python-dotenv) reads key-value pairs from a .env file and can set them as environment variables.

Installation: `pip install python-dotenv`

Load environment variables from `.env` file

```python
from dotenv import load_dotenv

load_dotenv()  # load .env file

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
```
`.env` for this project
```bash
#.env
# Add this to the .env file
DATABASE_URL = sqlite:///./data/iris.db
LOG_LEVEL = DEBUG
ENVIRONMENT = development # Staging and Production
MODEL_PATH = ./models/iris_dtree.joblib
PORT = 9000
HOST = 0.0.0.0
```

By default, `load_dotenv` doesn't override existing environment variables and looks for a .env file in same directory as python script or searches for it incrementally higher up.

### Dynaconf

[Dynaconf](https://www.dynaconf.com/) provides a simple way to manage configuration/settings for your application and help in protection of senstive informations (passwords/tokens). It supports multiple settings sources, including environment variables(dotenv support included), TOML, YAML, JSON, INI, and Python files. It also provides a simple way to override settings based on the environment. It provide optional layered system for multi environments [default, development, testing, production] (also called multi profiles). It also provides CLI for common operations such as init, list, write, validate, export.

Installation: `pip install dynaconf`

Initialization:

```bash
mkdir configs
dynaconf init -p configs -f yaml
```

Creates config.py and a config folder with files to hold application settings and sensitive data like passwords and tokens
First of all fix the paths for your settings files in config.py by replacing the following line:
`settings_files=["configs/settings.yaml", "configs/.secrets.yaml"]`

In code

```python
from config import settings
offset = settings.offset  # Use configuration as variables
```

Add the config in settings.yaml file

```YAML
offset:2
```

You can set and unset your configurations using environment variables as well

```bash
export DYNACONF_OFFSET=1
unset DYNACONF_OFFSET
```

In real world, we deal with multiple environment usually dev, stage and prod environment, for which we create layered environment configuration in config.py

```python
settings = Dynaconf(
     envvar_prefix="DYNACONF",
     settings_files=["configs/settings.yaml", "configs/.secrets.yaml"],
     environments=True,
)
```

Create different settings

```YAML
default:
 name: ""
 offset: 1

development:
 name: developer

production:
 offset: 0
 name: admin
```

Dynaconf sets the default environment to development. The subsequent layer inherits the configurations of the upper layers unless replaced.
Thus, we could access the offset value while in development even though we didn’t specify the offset value for it explicitly.

To Switch environment change environment variable, unset it for default

```bash
export ENV_FOR_DYNACONF=production
```

There are two other ways to set the environment using dynaconf

- `settings.from_env("production").name`
- `setenv("production")`
- `settings.name`

Second approach fixes the environment for the entire file but not globally. Although this approach might be convenient it is not recommended.

dynaconf provides plugins for both flask and django

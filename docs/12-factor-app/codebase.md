## 1. Codebase Setup

> One codebase tracked in revision control, many deploys

- Create a single codebase which can be single repo (in a centralized revision control system), or any set of repos who share a root commit (in a decentralized revision control system like Git) i.e. braches/clone/forks from a same root commit.
 - The single codebase will be deployed into a running instance of the app. The codebase remains the same across all deploys, although differen version may be active in each deploy.

### Setting Up Git
[`Download Git for Windows`](https://git-scm.com/downloads/win)
```
sudo apt update

sudo apt install git
```

Setup Git configuration for the system if its your [first time using git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

```bash
git config --global user.name “Aayush Regmi"
git config --global user.email "example@email.com"
```

Setup [Secure Shell Protocol (SSH)  for Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) for secure connection channel

```bash
ssh-keygen -t ed25519 -C "$(git config user.email)" # Create new shh key:

# Copy and add SSH key to SSH and GPG key page in Github
```

Create a local Repository

```bash
ls
git init
git add .
git commit -m “first commit”
```

Create a repository in github and connect local repository to github

```bash
git remote add origin git@github.com-AayushFuse:AayushFuse/abc.git
git push -u origin master
```

Alternatively you can clone a repository to your local machine:

On GitHub.com, navigate to the main page of the repository, Copy the URL for the repository.

```bash
git clone git@github.com:fuse-academics/12factorAppML.git
cd 12factorAppML
```
You can also do this through popular IDE such as VSCode.

### Pre Commit Hooks

[Pre-commit hooks](https://pre-commit.com/) are a set of scripts that are run automatically before you commit your code. They can be used to enforce consistent code style, run tests, and more.

Install pre-commit package: `pip install pre-commit`

Create a `.pre-commit-config.yaml` file in the root of your repository that defines the hooks you want to run. You can generate a basic configuration with `pre-commit sample-config` and modify it.

```YAML
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.11.5
  hooks:
    # Run the linter.
    - id: ruff
      types_or: [ python, pyi ]
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
      types_or: [ python, pyi ]

-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
    -   id: requirements-txt-fixer
    -   id: check-added-large-files
        args:
          - --maxkb=1000
          # - --enforce-all

    -   id: pretty-format-json
        args:
          - --autofix
          - --indent
          - "2"

```

Check [Pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) for some out-of-the-box hooks for pre-commits. You can also create and setup your own hooks.

After configuring your hooks, install them in your repository, and run commands automatically before each commit: `pre-commit install`

You can also run the hooks manually on all files or specific files: `pre-commit run --all-files`

To update hooks to their latest version use: `pre-commit autoupdate`

# Setting up your Python Environment

A well-defined development environment and worflow that can be repeated for every new project helps to ensure efficient, consistent and high quality development. Keep the workflow simple, consistent and reproducible. Make sure to  document everything and incorporate flexible architectures and scalable solutions that can adapt to evolving technologies and industry standards to sustain long-term functionality and relevance.

## Pre-requisites

Before you begin, ensure you have the following installed on your system:

- [Python](https://www.python.org/downloads/), usually pre-installed in most linux system, comes pre-installed with pip
- [Git](https://git-scm.com/downloads)

## Project Structure

This guide will help you set up a Python environment to get started with different types of python projects. The first thing to do is to set up a flexible folder structure that is easy to understand, navigate and manage.

- [Cookie Cutter Project Templates](https://cookiecutter.readthedocs.io/en/stable/) helps in setting up a consistent project structure, which is crucial for maintaining and scaling projects. You can choose a template, familarize with the project structure and components:
    - Installation: `pip install cookiecutter`
- **For Setting up project using Cookie Cutter templates**:
    - Data Science Repository Template
        - Installing the Data Science Template `pip install cookiecutter-data-science`
        - Configuring Project `ccds`
    - Other Available Templates [Cookie Cutter Templates](https://github.com/search?q=cookiecutter&amp%3Btype=Repositories&type=repositories)

    *Fill in necessary project details, configurations to customize the project; add data, scripts and get started developing.*

## Code Editor (IDE) Setup
The next thing that we need is a code editor that is easy to use and has good support for Python. There are many options available, but I recommend using [VS Code](https://code.visualstudio.com/) as it is free, open-source, and has a lot of extensions that can help you with your projects.

Now we need some extensions to get started depending on the programming language and tech stack we are using

**Visual Studio Code Extensions**

I have prepared a file for automating the installation process

- Create a `.sh` File `./install-extensions.sh`

```bash
#!/bin/bash
extensions=(
    "ms-python.python"
    "ms-python.vscode-pylance"
    "ms-toolsai.vscode-jupyter-powertoys "
    "charliermarsh.ruff"
    "ms-python.pylint"
    "george-alisson.html-preview-vscode"
    "ms-toolsai.jupyter"
    "foxundermoon.shell-format"
    "PKief.material-icon-theme"
    "aaron-bond.better-comments"
    "GitHub.vscode-github-actions"
    "GitHub.copilot"
    "GitHub.copilot-chat"
    "GitHub.vscode-pull-request-github"
)

for extension in "${extensions[@]}"; do
    code --install-extension "$extension"
done
```
```
# Let's add execute permissions for the file
chmod +x script.sh

# Now let's execute the script
./install-extensions.sh
```

## Project Management Tools
1. [Jira](https://www.atlassian.com/software/jira)
2. [Odoo](https://www.odoo.com)
3. [Trello](https://trello.com/)
4. [Linear](https://linear.app/)
5. [Todoist](https://todoist.com/)
6. [Clickup Github Project](https://clickup.com/github-project) etc.

Use PM tools to collaborate and handle complexity of projects, tasks, and workflows. This helps in planning, tracking and amangeing software development projects from conception to delivery.

- Setup Kanban board to manage tasks and track progress that usually includes: Backlog, Todo, In Progress, Review, Done.
- Setup Feature Labels to categorize features and track progress: Features, Bug, Improvement, Documentation, Test, etc.
- Integrate with Github to automatically create issues and track progress.
- Integrate with your communication platform Slack, Teams, GoogleChat, etc. to notify team members about new tasks and updates.

### Define a Definition of Done (DoD)

If you're working with a team, it is important to clearly describe each feature and define a Definition of Done (DoD) for each feature. This will help ensure that all team members are working towards the same goal and that the project is completed to a high standard.

**Examples of DoD**

- `Code is committed, peer-reviewed, and merged into the main branch.`
- `All tests (unit and integration) pass in CI/CD pipeline.`
- `API documentation is updated and visible in FastAPI's Swagger UI.`

### Standard Operating Procedure (SOPs)

Whenever you start a project, it is important to create a standard operating procedure (SOP) to ensure that all team members are working in the same way and that the project is completed to a high standard. SOPs define key practices like branching strategies, pull request conventions, and Definition of Done (DoD), helping maintain code quality and team alignment.

## Documentation

Maintain detailed documentation for processes, data sources, and transformations to ensure transparency and reproducibility in data projects. Follow a structured approach to manage documentation to ensure efficient and effective documentation.

- Store it in project repository under a folder called `docs` or `reports. and organize it with subfolders to makes it easy to find and access documentation related to research, sprint release notes (describes features, bug fixes, updates and rationale) and other categories. If you are using GitHub Releases feature it can automatically gnerate release notes stored separately from the repo.
- Use consistent naming convention for files usually written markdown files. Clarity is key so keep it simple, short and concise. AI can write effective documentation but they tend to be a bit verbose.
- Regularly update documentation, Review and edit them to catch errors and inconsistencies.
- Use a documentation tool such as [MkDocs](https://www.mkdocs.org), [Sphinx](https://www.sphinx-doc.org/en/master/) to generate documentation from source code and markdown files. This help to export to PDF or HTML for sharing.

**We will learn how to build and deploy documentation in this session**

## Testing (Pytest, etc.)

For testing we will be setting up

- [pytest](https://docs.pytest.org/en/stable/)

`pip install pytest`

Update `pytest.ini` file
```
[pytest]
python_files = tests/*.py
python_paths = .
asyncio_default_fixture_loop_scope = function

```

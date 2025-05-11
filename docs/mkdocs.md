## Setting up project Documentation
**Commands**

* `pip install mkdocs` - Installing library for Documentation
* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.


**Project layout**

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


**Edit `./mkdocs.yml` file**

    site_name: Title of your Site
    site_description: Description of your site
    nav:
      - Getting Started:
        - Overview: index.md
    theme: readthedocs

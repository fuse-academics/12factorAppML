## 5. Build, Release, Run Managmenet

> Strictly separate build and run stages

According to 12 factor, codebase is transformed into a (non-development) deploy through three stages:

- **The build stage:** Compiles a specified version of code repo into an executable bundle aka build; fetches dependencies, compile binaries and assets; packages the code. Usually triggered by developer
- **The release stage:** Combine the build with environment-specific configuration. The resulting release contains both the build and the config and is ready for immediate execution in the execution environment.
- **The run stage aka runtime:** Execute the app in the execution environment, by launching some set of the app’s processes against a selected release. Runtime execution can be automatically triggered. Therefore, the run stage should be kept to as few moving parts as possible, since problems that prevent an app from running can cause it to break in the middle of the night when no developers are on hand.

**The twelve-factor app uses strict separation between the build, release, and run stages.**

- **For example**, it is impossible to make changes to the code at runtime, since there is no way to propagate those changes back to the build stage.
Every release should always have a unique release ID, such as a timestamp of the release (such as 2011-04-06-20:32:17) or an incrementing number (such as v100).

- Releases cannot be mutated once it is created. Any change must create a new release.

### Docker

### Build: Create a Dockerfile to define the build process:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

Build the Docker image: `docker build -t my-python-app .`

### Release & Run

Set environment variables for configuration:

```bash
DATABASE_URL=mysql://user:password@localhost:3306/mydatabase
SECRET_KEY=mysecretkey
```

Run with the environment variable: `docker run --env-file .env -p 4000:80 my-python-app`

### Github Actions

Create a `new-workflow.yml` file in the `.github/workflows` directory of your repository.
[Github Actions](https://docs.github.com/en/actions) is a CI/CD tool integrated with github that allows automated workflows directly from repository. We can combime multiple action for testing, document hosting (eg. github pages), and package hosting-PyPi.

```YAML
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  release:
    types: [published]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest

  release:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Create Release
        id: create_release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          draft: false
          prerelease: false

      - name: Upload Release Asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }}
          asset_path: ./path/to/your/asset.zip
          asset_name: asset.zip
          asset_content_type: application/zip

  deploy:
    needs: [build, release]
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Deploy to Production
        run: ./deploy.sh
```

[Github Actions for Trunk Based Development](https://blog.jannikwempe.com/github-actions-trunk-based-development)

- Travis CI
- Jenkins

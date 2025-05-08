# Windows Setup
## Short version

On Windows, follow the standard [README.md](https://github.com/gpt-engineer-org/gpt-engineer/blob/main/README.md), but to set API key do one of:
- `set OPENAI_API_KEY=[your api key]` on cmd
- `$env:OPENAI_API_KEY="[your api key]"` on powershell

## Full setup guide

Choose either **stable** or **development**.

For **stable** release:

Run `pip install gpt-engineer` in the command line as an administrator

Or:

  1. Open your web browser and navigate to the Python Package Index (PyPI) website: <https://pypi.org/project/gpt-engineer/>.
  2. On the PyPI page for the gpt-engineer package, locate the "Download files" section. Here you'll find a list of available versions and their corresponding download links.
  3. Identify the version of gpt-engineer you want to install and click on the associated download link. This will download the package file (usually a .tar.gz or .whl file) to your computer.
  4. Once the package file is downloaded, open your Python development environment or IDE.
  5. In your Python development environment, look for an option to install packages or manage dependencies. The exact location and terminology may vary depending on your IDE. For example, in PyCharm, you can go to "File" > "Settings" > "Project: \<project-name>" > "Python Interpreter" to manage packages.
  6. In the package management interface, you should see a list of installed packages. Look for an option to add or install a new package.
  7. Click on the "Add Package" or "Install Package" button.
  8. In the package installation dialog, choose the option to install from a file or from a local source.
  9. Browse and select the downloaded gpt-engineer package file from your computer.

For **development**:

- `git clone git@github.com:gpt-engineer-org/gpt-engineer.git`
- `cd gpt-engineer`
- `poetry install`
- `poetry shell` to activate the virtual environment

### Setup

With an api key from OpenAI:

Run `set OPENAI_API_KEY=[your API key]` in the command line

Or:

  1. In the Start Menu, type to search for "Environment Variables" and click on "Edit the system environment variables".
  2. In the System Properties window, click on the "Environment Variables" button.
  3. In the Environment Variables window, you'll see two sections: User variables and System variables.
  4. To set a user-specific environment variable, select the "New" button under the User variables section.
  5. To set a system-wide environment variable, select the "New" button under the System variables section.
  6. Enter the variable name "OPENAI_API_KEY" in the "Variable name" field.
  7. Enter the variable value (e.g., your API key) in the "Variable value" field.
  8. Click "OK" to save the changes.
  9. Close any open command prompt or application windows and reopen them for the changes to take effect.

### Installing and Using Poetry

If you're working with the development version and need to use Poetry:

1. **Install Poetry** (if you haven't already):
   - Open PowerShell as administrator and run:
     ```
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
     ```
   - Or install with pip:
     ```
     pip install poetry
     ```

2. **Troubleshooting Poetry Command Not Found**:

   If you installed Poetry but get "'poetry' is not recognized as an internal or external command", you need to add Poetry to your PATH:

   - **Option 1: Run with full path** (quick solution):
     ```
     %APPDATA%\Python\Python3XX\Scripts\poetry install
     %APPDATA%\Python\Python3XX\Scripts\poetry shell
     ```
     Replace `3XX` with your Python version (e.g., `310` for Python 3.10, `313` for Python 3.13)

   - **Option 2: Add Poetry to PATH** (permanent solution):
     - Press Win+I to open Settings
     - Search for "Edit environment variables for your account"
     - Under "User variables", find the PATH variable and click Edit
     - Click New and add: `%APPDATA%\Python\Python3XX\Scripts`
     - Click OK, close all command prompts, and open a new one

   - **Option 3: Temporary PATH update** (for current session only):
     ```
     set PATH=%PATH%;%APPDATA%\Python\Python3XX\Scripts
     ```

3. **Run poetry install**:
   - Navigate to your gpt-engineer directory:
     ```
     cd path\to\gpt-engineer
     ```
   - Run the install command:
     ```
     poetry install
     ```

4. **Activate the virtual environment**:
   - After installation, activate the environment:
     ```
     poetry shell
     ```

This will install all dependencies defined in your `pyproject.toml` file and create a virtual environment for your project.

### Run

- Create an empty folder. If inside the repo, you can:
  - Run `xcopy /E projects\example projects\my-new-project` in the command line
  - Or hold CTRL and drag the folder down to create a copy, then rename to fit your project
- Fill in the `prompt` file in your new folder
- `gpt-engineer projects/my-new-project`
  - (Note, `gpt-engineer --help` lets you see all available options. For example `--steps use_feedback` lets you improve/fix code in a project)

By running gpt-engineer you agree to our [ToS](https://github.com/gpt-engineer-org/gpt-engineer/blob/main/TERMS_OF_USE.md).

### Results

- Check the generated files in `projects/my-new-project/workspace`

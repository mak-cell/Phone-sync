# Phone-sync

A brief description of Sync Bot.

## Setting up a Virtual Environment

To isolate Sync Bot's dependencies, you can create and use a Python virtual environment. Here's how:

1. **Create a Virtual Environment:**

   Open your command prompt or terminal and navigate to the project directory. Run the following command to create a virtual environment:

   ```bash
   python -m venv venv_name
   ```

   Replace `venv_name` with your preferred virtual environment name, for example:

   ```bash
   python -m venv myenv
   ```

2. **Activate the Virtual Environment:**

   Depending on your operating system, activate the virtual environment as follows:

   - **Windows:**

     ```bash
     venv_name\Scripts\activate
     ```

   - **macOS and Linux:**

     ```bash
     source venv_name/bin/activate
     ```

   Once activated, your command prompt or terminal will show the virtual environment name.

## Installing Dependencies

You can use a `requirements.txt` file to list Sync Bot's dependencies. To install them in your virtual environment, follow these steps:

1. **Activate the Virtual Environment:**

   Ensure that your virtual environment is activated.

2. **Install Dependencies from `requirements.txt`:**

   Run the following command to install the dependencies specified in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure the `requirements.txt` file is in Sync Bot directory and contains a list of required packages and their versions.

## Running Sync Bot

With your virtual environment activated and dependencies installed, you can run Sync Bot's main script. Here's how:

1. **Activate the Virtual Environment:**

   Ensure that your virtual environment is activated.

2. **Navigate to Sync Bot Directory:**

   Use the command prompt or terminal to navigate to the directory where Sync Bot's `main.py` script is located.

3. **Run Your `main.py` Script:**

   Run your main script using the `python` command:

   ```bash
   python main.py
   ```

   This will execute your script with the isolated dependencies from the virtual environment.

## Deactivating the Virtual Environment

When you're done working on Sync Bot, you can deactivate the virtual environment to return to the system's global Python environment:

```bash
deactivate
```

This will ensure that Sync Bot's dependencies remain isolated.

Remember to activate your virtual environment every time you work on Sync Bot and deactivate it when you're finished to keep Sync Bot dependencies isolated from the system-wide Python installation.

```

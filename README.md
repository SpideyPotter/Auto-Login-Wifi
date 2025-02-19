# Auto-Login-Wifi

A Python project that automates WiFi login by saving user credentials in a `credentials.json` file and logging into the WiFi portal using an HTTP POST request.

## Features

- **Automated login using stored credentials**: Automatically logs into the WiFi portal using saved credentials.
- **Credential storage in `credentials.json`**: User credentials are securely stored in a `credentials.json` file, which is ignored in version control.
- **Standalone executable with PyInstaller**: Create a standalone executable for easy distribution using PyInstaller.

## Developer Instructions

### Prerequisites

- Python 3.x
- PyInstaller

### edit the python file for your own wifi network :

```python
   login_url = "the network login portal url"

   payload = {
       "mode": "191",
      "username": username,  # Use the saved or entered username
      "password": password,  # Use the saved or entered password
      "a": "1739869937827",
      "producttype": "0"
      }
```

### Steps to Build the Executable

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:

   ```bash
   pyinstaller --onefile --icon=app_icon.ico --add-data "credentials.json;." login_script.py

   ```

3. The executable will be located in the `dist` directory.

### Uploading to GitHub Releases

1. Create a new release on your GitHub repository.
2. Upload the executable file from the `dist` directory to the release.

## User Instructions

### Downloading the Executable

1. Go to the [GitHub Releases](https://github.com/<USERNAME>/<REPOSITORY>/releases) page.
2. Download the latest executable for your operating system.

### Running the Executable

1. Run the downloaded executable.
2. Enter your WiFi credentials when prompted for the first time. The credentials will be saved in a `credentials.json` file for future logins.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

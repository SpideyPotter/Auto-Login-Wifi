import sys
import os
import json
import requests

# Path to store the credentials
credentials_file = "credentials.json"

# Function to check if the app is running as a packaged executable
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Function to ask for credentials
def get_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

# Function to save credentials to a file
def save_credentials(username, password):
    credentials = {
        "username": username,
        "password": password
    }
    with open(credentials_file, "w") as file:
        json.dump(credentials, file)

# Function to load credentials from the file
def load_credentials():
    file_path = resource_path(credentials_file)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            credentials = json.load(file)
        return credentials["username"], credentials["password"]
    return None, None

# Check if credentials already exist
username, password = load_credentials()

if not username or not password:
    # Ask for credentials if they don't exist
    print("No credentials found. Please enter your credentials.")
    username, password = get_credentials()
    save_credentials(username, password)
    print("Credentials saved for future use.")

# The login URL and payload
login_url = "https://bmunet.bmu.edu.in:8090/login.xml"

payload = {
    "mode": "191",
    "username": username,  # Use the saved or entered username
    "password": password,  # Use the saved or entered password
    "a": "1739869937827",  
    "producttype": "0"
}

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Referer": "https://bmunet.bmu.edu.in:8090/httpclient.html",
    "Origin": "https://bmunet.bmu.edu.in:8090",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

# Start a session to persist the login
session = requests.Session()

try:
    response = session.post(login_url, data=payload, headers=headers, timeout=10)

    print("Response Code:", response.status_code)
    print("Response Content:", response.text)

    if response.status_code == 200 and "success" in response.text.lower():
        print("✅ WiFi login successful!")
    else:
        print("⚠️ Login may have failed. Check response content.")
except requests.exceptions.RequestException as e:
    print(f"❌ Login request failed: {e}")

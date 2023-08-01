EgyBruter is a powerful and efficient WordPress brute force tool designed to help ethical hackers and security researchers identify and address weak login credentials in WordPress websites. This tool utilizes multithreading to perform concurrent login attempts, making it fast and efficient for testing password combinations.
Features

    Fast and efficient WordPress brute force attacks.
    Multithreading for concurrent login attempts.
    User-friendly and visually appealing interface.
    Thread safety to ensure clean and organized output.
    Target information display, including URL, status code, server, and IP address.
    Check connection to the target before starting the brute force attack.
    Ability to use custom user-agent headers for requests.

Installation

    Clone this repository to your local machine using git clone.
    Navigate to the cloned directory: cd EgyBruter.
    Install the required dependencies: pip install -r requirements.txt.

Usage

    Run the script: python EgyBruter.py.
    Enter the target URL, which should be the WordPress login page.
    Provide the WordPress username for the brute force attack.
    Enter the path to the file containing the list of passwords, with one password per line.
    Specify the number of threads to use during the brute force attack (recommended: 10).
    Sit back and let EgyBruter perform the brute force attack.

Note: Please use this tool responsibly and only on websites where you have proper authorization. Unauthorized use is illegal and unethical.
Example

mathematica

$ python EgyBruter.py
Enter the target URL (WordPress login page): https://example.com/wp-login.php
Enter the username: admin
Enter the path to the file containing passwords (one per line): passwords.txt
Enter the number of threads to use (recommend 10): 10

Disclaimer

This tool is intended for ethical hacking and security research purposes only. The developer and contributors are not responsible for any illegal or malicious use of this tool. Use it responsibly and only on websites where you have proper authorization.
License

EgyBruter is licensed under the MIT License.
Contributions

Contributions to improve and enhance EgyBruter are welcome! Please feel free to open issues, submit pull requests, or suggest new features to make this tool even better.
Credits

EgyBruter is developed and maintained by Your Name.
Acknowledgments

Special thanks to the open-source community for their valuable contributions to the tools and libraries used in this project.

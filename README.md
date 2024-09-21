Python Virus Scanner Tool Using VirusTotal API
This tool scans the files in a specified directory using the VirusTotal API to detect potential vulnerabilities and malware. It automatically checks if a file is vulnerable and prints the result. Optionally, you can delete vulnerable files after detection.

Features
Scans all files in a directory (supports multithreading for faster scanning).
Uses VirusTotal API for file scanning and reporting.
Detects if files are vulnerable (infected with malware).
Can handle large directories and filters files larger than 32MB.
Provides detailed logging for safe and vulnerable files.
Optionally, deletes vulnerable files from the system.
Requirements
Python 3.x
requests library
VirusTotal API key
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/YourUsername/virus-scanner-tool.git
cd virus-scanner-tool
Install dependencies:

bash
Copy code
pip install requests
Get your VirusTotal API Key:

Sign up for a free account at VirusTotal.
Obtain your API key from the user settings.
Set your API key in the script:

Open the file virsh_scanner.py and replace the value of API with your own VirusTotal API key:
python
Copy code
API = "your_virustotal_api_key"
Usage
To scan a specific directory, run the script from the terminal:

bash
Copy code
python virsh_scanner.py
You can modify the directory path to scan any folder on your system. For example:

python
Copy code
scan_system_files("/path/to/your/directory", max_work=8)
If a file is vulnerable (infected), it will be flagged, and you can choose to delete it by uncommenting the os.remove() line in the script:

python
Copy code
# os.remove(file_path)
Example Output
bash
Copy code
This file is vulnerable: /home/user/Documents/malicious_file.exe
The file /home/user/Documents/safe_file.txt is safe
File is too large or does not exist: /home/user/Documents/large_file.iso
Important Notes
This tool only scans files up to 32MB due to VirusTotal API limitations for free users.
You need to provide your own VirusTotal API key in the script to use this tool.
The tool does not automatically delete files unless the os.remove() line is uncommented.
License
This project is licensed under the MIT License - see the LICENSE file for details.


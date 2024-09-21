# Python Virus Scanner Tool Using VirusTotal API

This tool scans the files in a specified directory using the VirusTotal API to detect potential vulnerabilities and malware. It automatically checks if a file is vulnerable and prints the result. Optionally, you can delete vulnerable files after detection.

## Features
- Scans all files in a directory (supports multithreading for faster scanning).
- Uses VirusTotal API for file scanning and reporting.
- Detects if files are vulnerable (infected with malware).
- Can handle large directories and filters files larger than 32MB.
- Provides detailed logging for safe and vulnerable files.
- Optionally, deletes vulnerable files from the system.

## Requirements
- Python 3.x
- `requests` library
- VirusTotal API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/virus-scanner-tool.git
   cd virus-scanner-tool

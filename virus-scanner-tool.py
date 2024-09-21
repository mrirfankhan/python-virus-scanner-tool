import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

API = "<your virush total api>"

def scan_file(file_path):
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    try:
        with open(file_path, "rb") as file:
            files = {'file': (file_path, file)}
            params = {'apikey': API}
            response = requests.post(url, files=files, params=params)
            if response.status_code != 200:
                print(f"Error scanning file {file_path}: {response.status_code}")
                return {}
            return response.json()
    except Exception as e:
        print(f"Error opening file {file_path}: {e}")
        return {}

def get_report(resource):
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    params = {'apikey': API, 'resource': resource}
    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching report for resource {resource}: {response.status_code}")
            return {}
        return response.json()
    except Exception as e:
        print(f"Error fetching report: {e}")
        return {}

def verify_delete(file_path):
    scan_file1 = scan_file(file_path)
    if not scan_file1 or "scan_id" not in scan_file1:
        print(f"Error scanning {file_path}, no scan_id returned")
        return

    scan_id = scan_file1.get("scan_id")
    time.sleep(15)  # Wait for the report to be generated
    report1 = get_report(scan_id)
    
    if not report1:
        print(f"Error retrieving report for {file_path}")
        return
    
    if report1.get('positives', 0) > 0:
        print(f"This file is vulnerable: {file_path}")
        # Uncomment the next line to delete the file
        # os.remove(file_path)
    else:
        print(f"The file {file_path} is safe")

def scan_system_files(root_dir, max_work):
    files_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):  # Check if file exists
                if os.path.getsize(file_path) <= 32 * 1024 * 1024:  # Check file size
                    files_list.append(file_path)
                else:
                    print(f"File {file_path} is too large to scan.")
            else:
                print(f"File not found: {file_path}")

    with ThreadPoolExecutor(max_workers=max_work) as executor:
        futures = [executor.submit(verify_delete, file_path) for file_path in files_list]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                print(f"Error occurred during file scanning: {exc}")

if __name__ == "__main__":
    scan_system_files("/home/irfan/Documents/", max_work=8)

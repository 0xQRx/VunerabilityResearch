# Membership Management System in PHP - Unrestricted File Upload to RCE (Settings Logo)

### CVE Assigned:
**[CVE-2024-25869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25869)** [mitre.org](https://www.cve.org/CVERecord?id=CVE-2024-25869) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2024-25869)

### Date:

> 9 Feb 2024

### Author Email:

> yevhenii.butenko@outlook.com

### Vendor Homepage:

> https://codeastro.com/

### Software Link:

> [Membership Management System in PHP](https://codeastro.com/membership-management-system-in-php-with-source-code/)

### Version:

> v 1.0

### Unrestricted File Upload to RCE:

> The "Unrestricted File Upload to Remote Code Execution (RCE)" vulnerability is a critical security flaw where attackers can upload malicious files to a web server. This vulnerability arises from the lack of proper restrictions on the types and contents of the files that can be uploaded. Once uploaded, these files can be executed on the server, allowing attackers to run arbitrary code and potentially gain full control over the server. This vulnerability poses a severe risk, as it can lead to system compromise, data breaches, and further network exploitation.

### Affected Components:

> settings.php

### Description:

> The presence of this vulnerability enables an unauthenticated attacker to upload .php files to the web server and execute code under the privileges of the user running the application.

## Proof of Concept:

### Manual Exploitation

![Upload shell.php via admin settings](https://github.com/0xQRx/VulnerabilityResearch/blob/master/2024/img/membership_management_unrestricted_fileupload.png?raw=true)

![Remote Code Execution](https://github.com/0xQRx/VulnerabilityResearch/blob/master/2024/img/membership_management_unrestricted_fileupload_exec.png?raw=true)

### Automated Exploitation

The python script PoC of exploit can be found [here](https://github.com/0xQRx/VulnerabilityResearch/blob/master/2024/PoC/MembershipManagementSystem/authenticated_file_upload_rce.py).

![Remote Code Execution](https://github.com/0xQRx/VulnerabilityResearch/blob/master/2024/PoC/MembershipManagementSystem/img/membership_management_unrestricted_fileupload_script_exec.png?raw=true)

## Recommendations

To mitigate this vulnerability, it's essential to validate and sanitize all file uploads, restrict file types, and ensure that uploaded files are not executable on the server.

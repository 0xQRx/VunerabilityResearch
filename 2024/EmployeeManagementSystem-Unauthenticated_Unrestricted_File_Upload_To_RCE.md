# Employee Management System - Unauthenticated Unrestricted File Upload To RCE

### Vendor Homepage:

> https://www.sourcecodester.com

### Software Link:

> [Employee Management System](https://www.sourcecodester.com/php/16999/employee-management-system.html)

### Version:

> v 1.0

### Unauthenticated Unrestricted File Upload to RCE:

> The "Unauthenticated Unrestricted File Upload to Remote Code Execution (RCE)" vulnerability is a critical security flaw where attackers can upload malicious files to a web server without needing to authenticate. This vulnerability arises from the lack of proper restrictions on the types and contents of the files that can be uploaded. Once uploaded, these files can be executed on the server, allowing attackers to run arbitrary code and potentially gain full control over the server. This vulnerability poses a severe risk, as it can lead to system compromise, data breaches, and further network exploitation.

### Affected Components:

> /employee_akpoly/Admin/edit-photo.php

### Description:

> The presence of this vulnerability enables an unauthenticated attacker to upload .php files to the web server and execute code under the privileges of the user running the application.

## Proof of Concept:

The python script PoC of exploit can be found [here](https://github.com/0xQRx/VunerabilityResearch/blob/master/2024/PoC/EmployeeManagementSystem/unauthenticated_file_upload_rce.py).

![Remote Code Execution](https://github.com/0xQRx/VunerabilityResearch/blob/master/2024/PoC/EmployeeManagementSystem/img/unauthenticated_file_ulpoad_rce.png?raw=true)

## Recommendations

To mitigate this vulnerability, it's essential to implement strong authentication, validate and sanitize all file uploads, restrict file types, and ensure that uploaded files are not executable on the server.

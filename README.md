# sploitGET
This is a simple wrapper script for https://sploitus.com.

## Usage

```bash
python3 sploitGET.py --help                         
usage: sploitGET.py [-h] -q QUERY [-t {exploits,tools}]
                    [-s {default,date,score}]

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        search query
  -t {exploits,tools}, --type {exploits,tools}
                        Search for either public exploits or tools
  -s {default,date,score}, --sort {default,date,score}
                        Sort the results by chosen option
```


### Example
A basic search query may look like this:

```bash
python3 sploitGET.py -q "Linux Kernel 3.13" -t exploits -s default

 #####                                #####  ####### ####### 
#     # #####  #       ####  # ##### #     # #          #    
#       #    # #      #    # #   #   #       #          #    
 #####  #    # #      #    # #   #   #  #### #####      #    
      # #####  #      #    # #   #   #     # #          #    
#     # #      #      #    # #   #   #     # #          #    
 #####  #      ######  ####  #   #    #####  #######    #    
                                                             

[+] Found 12 results!

+-----------------------------------------------+------------------------------------------------------------------------------+------------+-------------+-------+
|                     Title                     |                                     URL                                      |    Date    |  Published  | Score |
+-----------------------------------------------+------------------------------------------------------------------------------+------------+-------------+-------+
|     Linux Nested NMIs Privilege Escalation    | https://packetstormsecurity.com/files/download/132994/linuxnmis-escalate.txt | 2015-08-07 | packetstorm |  7.2  |
| Linux espfix64 - Privilege Escalation Nested  |                  https://www.exploit-db.com/download/37722/                  | 2015-08-05 |  exploitdb  |  7.2  |
| Linux x86_64 NMI Privilege Escalation Due to  |                       https://0day.today/exploit/23971                       | 2015-08-05 |     zdt     |  7.2  |
|  Linux Kernel splice System Call - Local DoS  |                  https://www.exploit-db.com/download/36743/                  | 2015-04-13 |  exploitdb  |  7.2  |
| Linux Kernel <= 3.13 - Local Privilege Escala |                   https://www.seebug.org/vuldb/ssvid-87007                   | 2014-07-01 |    seebug   |  6.2  |
| Linux Kernel <= 3.13 - Local Privilege Escala |                       https://0day.today/exploit/22363                       | 2014-06-22 |     zdt     |  6.2  |
| Linux Kernel <= 3.13 - Local Privilege Escala |                  https://www.exploit-db.com/download/33824/                  | 2014-06-21 |  exploitdb  |  6.2  |
|        Linux Kernel inet_frag_intern()        |                   https://www.seebug.org/vuldb/ssvid-62030                   | 2014-04-02 |    seebug   |  9.3  |
|     Linux Kernel 'arch_dup_task_struct()'     |                   https://www.seebug.org/vuldb/ssvid-61996                   | 2014-03-31 |    seebug   |  9.3  |
|     Linux Kernel ath9k ath_tx_aggr_sleep()    |                   https://www.seebug.org/vuldb/ssvid-61997                   | 2014-03-31 |    seebug   |  9.3  |
+-----------------------------------------------+------------------------------------------------------------------------------+------------+-------------+-------+
```

```bash
python3 sploitGET.py -q "gobuster" -t tools
 #####                                #####  ####### ####### 
#     # #####  #       ####  # ##### #     # #          #    
#       #    # #      #    # #   #   #       #          #    
 #####  #    # #      #    # #   #   #  #### #####      #    
      # #####  #      #    # #   #   #     # #          #    
#     # #      #      #    # #   #   #     # #          #    
 #####  #      ######  ####  #   #    #####  #######    #    
                                                             

[+] Found 5 results!

+-----------------------------------------------+----------------------------------------+------------------------------------------------------------------------------+
|                     Title                     |                  URL                   |                                     Blog                                     |
+-----------------------------------------------+----------------------------------------+------------------------------------------------------------------------------+
| Celerystalk - An Asynchronous Enumeration and | https://github.com/sethsec/celerystalk |  http://www.kitploit.com/2018/12/celerystalk-asynchronous-enumeration.html   |
| Kali Linux 2018.4 Release - Penetration Testi |    https://www.kali.org/downloads/     |  http://www.kitploit.com/2018/10/kali-linux-20184-release-penetration.html   |
| Gobuster - Directory/File & DNS Busting Tool  |     https://github.com/OJ/gobuster     | http://www.kitploit.com/2018/02/gobuster-directoryfile-dns-busting-tool.html |
| Vanquish - Kali Linux based Enumeration Orche |   https://github.com/frizb/Vanquish    |  http://www.kitploit.com/2017/10/vanquish-kali-linux-based-enumeration.html  |
| Reconnoitre - A Security Tool For Multithread | https://github.com/codingo/Reconnoitre |      http://www.kitploit.com/2017/05/reconnoitre-security-tool-for.html      |
+-----------------------------------------------+----------------------------------------+------------------------------------------------------------------------------+
```

## Known Issues

* The current table does no automatic line wrapping
* The used curl command does not load **all** results if there are > 10
  * Sploitus loads these results dynamically when scrolling
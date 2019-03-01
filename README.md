# sploitGET
This is a simple wrapper script for https://sploitus.com that fetches either tools or exploit from their API for a specified search query.

The resulting download URLs in the table are shortened via https://is.gd/ and https://git.io for github repos.
By doing so and doing an automatic line break at a length of 30/50 characters the output of search queries nicely fits
on one half of a 1080p screen with a terminal font size of ~13pts.

Feel free to edit the script or suggest changes.

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
-> % python3 sploitGET.py -q "Linux Kernel 3.13" -s score
 #####                                #####  ####### ####### 
#     # #####  #       ####  # ##### #     # #          #    
#       #    # #      #    # #   #   #       #          #    
 #####  #    # #      #    # #   #   #  #### #####      #    
      # #####  #      #    # #   #   #     # #          #    
#     # #      #      #    # #   #   #     # #          #    
 #####  #      ######  ####  #   #    #####  #######    #    
                                                             
────────────────────────────────────────────────────────────
[+] Found 12 results!

+--------------------------------+----------------------+------------+-------------+-------+
|             Title              |         URL          |    Date    |  Published  | Score |
+--------------------------------+----------------------+------------+-------------+-------+
|       Linux Kernel DCCP        | https://is.gd/ReNKyx | 2014-03-19 |    seebug   |  10.0 |
|          Linux Kernel          | https://is.gd/a2gmK7 | 2014-04-02 |    seebug   |  9.3  |
|       inet_frag_intern()       |                      |            |             |       |
|  Linux Nested NMIs Privilege   | https://is.gd/FHb9XU | 2015-08-07 | packetstorm |  7.2  |
|           Escalation           |                      |            |             |       |
|   Linux espfix64 - Privilege   | https://is.gd/niEvef | 2015-08-05 |  exploitdb  |  7.2  |
|     Escalation Nested NMIs     |                      |            |             |       |
|          Interrupting          |                      |            |             |       |
|   Linux x86_64 NMI Privilege   | https://is.gd/QfLB6t | 2015-08-05 |     zdt     |  7.2  |
| Escalation Due to Nested NMIs  |                      |            |             |       |
|     Interrupting espfix64      |                      |            |             |       |
|   Linux Kernel splice System   | https://is.gd/xzz9Vc | 2015-04-13 |  exploitdb  |  7.2  |
|        Call - Local DoS        |                      |            |             |       |
|  Linux Kernel <= 3.13 - Local  | https://is.gd/453sk4 | 2014-07-01 |    seebug   |  6.2  |
| Privilege Escalation PoC (gid) |                      |            |             |       |
|  Linux Kernel <= 3.13 - Local  | https://is.gd/XCmSa1 | 2014-06-22 |     zdt     |  6.2  |
| Privilege Escalation PoC (gid) |                      |            |             |       |
|  Linux Kernel <= 3.13 - Local  | https://is.gd/M260Y7 | 2014-06-21 |  exploitdb  |  6.2  |
|  Privilege Escalation PoC gid  |                      |            |             |       |
|       Linux Kernel IPv6        | https://is.gd/pq8VZm | 2014-03-11 |    seebug   |  6.1  |
+--------------------------------+----------------------+------------+-------------+-------+

```

```bash
-> % python3 sploitGET.py -q "gobuster" -t tools

 #####                                #####  ####### ####### 
#     # #####  #       ####  # ##### #     # #          #    
#       #    # #      #    # #   #   #       #          #    
 #####  #    # #      #    # #   #   #  #### #####      #    
      # #####  #      #    # #   #   #     # #          #    
#     # #      #      #    # #   #   #     # #          #    
 #####  #      ######  ####  #   #    #####  #######    #    
                                                             
────────────────────────────────────────────────────────────
[+] Found 5 results!

+-------------------------------------------------+----------------------+--------------+
|                      Title                      |         URL          |   Website    |
+-------------------------------------------------+----------------------+--------------+
|  Celerystalk - An Asynchronous Enumeration and  | https://git.io/fhACJ |  github.com  |
|              Vulnerability Scanner              |                      |              |
| Kali Linux 2018.4 Release - Penetration Testing | https://is.gd/ruZP0m | www.kali.org |
|      and Ethical Hacking Linux Distribution     |                      |              |
|   Gobuster - Directory/File & DNS Busting Tool  | https://git.io/fhAcd |  github.com  |
|                  Written In Go                  |                      |              |
|     Vanquish - Kali Linux based Enumeration     | https://git.io/fhACU |  github.com  |
|                   Orchestrator                  |                      |              |
| Reconnoitre - A Security Tool For Multithreaded | https://git.io/fhACT |  github.com  |
|  Information Gathering And Service Enumeration  |                      |              |
+-------------------------------------------------+----------------------+--------------+

```

## Known Issues

* The used curl command does not load **all** results if there are > 10
  * Sploitus loads these results dynamically when scrolling

#!/usr/bin/python
#author - ethical securities
#date - 25 June 2019
#name of the file - nmap_scan.py

#purpose - using python to run nmap scans

import nmap #in order to use python to write your own nmap scan codes, import nmap module

results = nmap.PortScanner()  #call PortScanner() method of nmap module for scanning purpose

print results.scan('192.168.70.129', '1-65535') #specify the target IP and port range; also print scan parameters

print ('*'*80) #separator

print results.command_line() #print the command line arguments of nmap command

print ('*'*80) #separator

print results['192.168.70.129'].all_protocols() #check what protocols were scanned on the target

print ('*'*80) #separator

print results['192.168.70.129'].state()         #check the state of the target machine - up or down

print ('*'*80) #separator

print results['192.168.70.129']['tcp'].keys()   #check the ports discovered

print ('*'*80) #separator

print results['192.168.70.129']['tcp'][22]      #check the state of the port

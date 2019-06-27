#!/usr/bin/python

#author - ethical securities
#date - 25 June 2019
#name of the file - read_messages.py

#purpose - using python to search for specific log entries - keywords, time stamps etc.

fdesc = open("/var/log/messages", "r") # This will open /var/log/messages in the linux PC
for line in fdesc:
	if "Jun 25 23:06:10" in line: #This  will search for logs with time stamp 'June 25 23:06:10'
		print line
fdesc.close()

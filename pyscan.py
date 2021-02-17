#!/usr/bin/env python3


##########################################################################
# Imports
import xml.etree.ElementTree as ET
import subprocess
import os
import random
import socket
import time

#<?xml version="1.0" encoding="UTF-8"?>
#<note>
#  <to>Tove</to>
#  <from>Jani</from>
#  <heading>Reminder</heading>
#  <body>Don't forget me this weekend!</body>
#</note>
#

##########################################################################
# Python to bash commands

def py_to_bash_without_os_sys(bashCommand):
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	return output

def py_to_bash(bashCommand):
	os.system(bashCommand)

def clears():
	py_to_bash("clear")

##########################################################################
# Update dependencies

def update_install_nmap():
	print("Do you want to make an update before dependencies installation? [y]es or [n]o")
	switch1 = True
	while (switch1):
		answer = input()
		if answer == "y":
			switch1 = False
			clears()
			py_to_bash("apt-get update && apt-get install nmap")
			py_to_bash("pip install elementpath && pip3 install elementpath")
		elif answer == "n":
			switch1 = False
			clears()
			py_to_bash("apt-get install nmap")
			py_to_bash("pip install elementpath && pip3 install elementpath")
		else :
			print("Invalid input")
	print("Clearing in 10s...")
	time.sleep(10)
	clears()
	radomize_menu()
	main_menu()


##########################################################################
# Scan types

def nmap_basic_scan():
	hostname = socket.gethostname()
	local_ip = socket.gethostbyname(hostname)
	py_to_bash(f"nmap -sC -sV {set_output_xml(True)} {local_ip}")

def nmap_basic_scan_man():
	ipAdress = input("Enter your local IP Adress: ")
	py_to_bash(f"nmap -sC -sV {set_output_xml(True)} {ipAdress}")

def nmap_vuln_scan():
	hostname = socket.gethostname()
	local_ip = socket.gethostbyname(hostname)
	py_to_bash(f"nmap -sC -sV --script=vuln -p- {set_output_xml(True)} {local_ip}")

def nmap_vuln_scan_man():
	ipAdress = input("Enter your local IP Adress: ")
	py_to_bash(f"nmap -sC -sV --script=vuln -p- {set_output_xml(True)} {ipAdress}")

##########################################################################
# Settings

def set_output_xml(saveFile):
	if(saveFile == True):
		passLocation = "-oX output.xml"
	else:
		passLocation = ""
	return passLocation


def set_root(xmlFileName):
	myTree = ET.parse(xmlFileName)
	getRoot = myTree.getroot()
	return getRoot

##########################################################################
# Xml Parsing 

def print_tags_and_attrib(root):
	for child in root:
		print(f"Tag = {child.tag}", f"\nAttrib =  {child.text}")

##########################################################################
#Menus

def main_menu_theme_1():
	print("d8888b. db    db .d8888.  .o88b.  .d8b.  d8b   db ")
	print("88  `8D `8b  d8' 88'  YP d8P  Y8 d8' `8b 888o  88 ")
	print("88oodD'  `8bd8'  `8bo.   8P      88ooo88 88V8o 88 ")
	print("88~~~      88      `Y8b. 8b      88~~~88 88 V8o88 ")
	print("88         88    db   8D Y8b  d8 88   88 88  V888 ")
	print("88         YP    `8888Y'  `Y88P' YP   YP VP   V8P ")
	print("                                                  ")
	print("                                           kyriefs")
	print("                                                  ")
	print("   _Options/")
	print("   __1. Install dependencies")
	print("   __2. Default Scan")
	print("   __3. Default Scan (Manualy)")
	print("   __4. Flaws Scan")
	print("   __5. Flaws Scan (Manualy)")
	print("   __6. Exit")
	print("   __7. Menu")

def main_menu_theme_2():

	print(" 888888ba           .d88888b                             ")
	print(" 88    `8b          88.    ""'                           ")
	print("a88aaaa8P' dP    dP `Y88888b. .d8888b. .d8888b. 88d888b. ")
	print(" 88        88    88       `8b 88'  `"" 88'  `88 88'  `88 ")
	print(" 88        88.  .88 d8'   .8P 88.  ... 88.  .88 88    88 ")
	print(" dP        `8888P88  Y88888P  `88888P' `88888P8 dP    dP ")
	print("oooooooooooo~~~~.88~ooooooooooooooooooooooooooooooooooooo")
	print("            d8888P                                       ")
	print("                                               kyriefs   ")
	print("                                                         ")
	print("   _Options/")
	print("   __1. Install dependencies")
	print("   __2. Default Scan")
	print("   __3. Default Scan (Manualy)")
	print("   __4. Flaws Scan")
	print("   __5. Flaws Scan (Manualy)")
	print("   __6. Exit")
	print("   __7. Menu")

def main_menu_theme_3():

	print(" .oPYo.        .oPYo.                     ")
	print(" 8    8        8                          ")
	print("o8YooP' o    o `Yooo. .oPYo. .oPYo. odYo. ")
	print(" 8      8    8     `8 8    ' .oooo8 8' `8 ")
	print(" 8      8    8      8 8    . 8    8 8   8 ")
	print(" 8      `YooP8 `YooP' `YooP' `YooP8 8   8 ")
	print(":..::::::....8 :.....::.....::.....:..::..")
	print("::::::::::ooP'.:::::::::::::::::::::::::::")
	print("::::::::::...:::::::::::::::::::::::::::::")
	print(":::::::::::::::::::::::::::::::  kyriefs :")
	print("::::::::::::::::::::::::::::::::::::::::::")
	print("::   Options   :::::::::::::::::::::::::::")
	print("::::: 1. Install dependencies ::::::::::::")
	print(":::::     (First time use)   :::::::::::::")
	print("::::::::::::::::::::::::::::::::::::::::::")
	print("::::: 2. Default Scan ::::::::::::::::::::")
	print("::::: 3. Default Scan (Manualy) ::::::::::")
	print("::::: 4. Flaws Scan ::::::::::::::::::::::")
	print("::::: 5. Flaws Scan (Manualy) ::::::::::::")
	print("::::: 6. Exit ::::::::::::::::::::::::::::")
	print("::::: 7. Menu ::::::::::::::::::::::::::::")

def radomize_menu():
	kickIt = random.randrange(1,4)
	if(kickIt == 1):
		main_menu_theme_1()
	elif(kickIt == 2):
		main_menu_theme_2()
	elif(kickIt== 3):
		main_menu_theme_3()

def main_menu():

	repeat = True
	while repeat:
		switch = input()
		if switch == '2':
			repeat = False
			clears()
			nmap_basic_scan()
		elif switch == '3':
			repeat = False
			clears()
			nmap_basic_scan_man()
		elif switch == '4':
			repeat = False
			clears()
			nmap_vuln_scan()
		elif switch == '5':
			repeat = False
			clears()
			nmap_vuln_scan_man()
		elif switch == '6':
			clears()
			exit()
		elif switch == '7':
			clears()
			radomize_menu()
			repeat == True
		elif switch == '1':
			repeat = False
			update_install_nmap()
		else :
			print("Invalid input")

	return switch

##########################################################################
# Main function

def main():
	#root = set_root('testfile.xml')
	#print("File name = " + root.tag)
	#print_tags_and_attrib(root)
	set_output_xml(True)
	radomize_menu()
	print("! Be sure to run the script in SUDO mode !")
	print("   Coming Soon:")
	print("  Highlight of possible threats and flaws")
	main_menu()
	#print("Testing bash")
	#py_to_bash("ls")

if __name__ == '__main__':
	main()
##########################################################################

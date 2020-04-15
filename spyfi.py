#!/usr/bin/env
#Author: Ansh - mrdebator
import os

print('''

╭━━━╮╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┳╮╱╭┫╰━━┳╮
╰━━╮┃╭╮┃┃╱┃┃╭━━╋┫
┃╰━╯┃╰╯┃╰━╯┃┃╱╱┃┃
╰━━━┫╭━┻━╮╭┻╯╱╱╰╯
╱╱╱╱┃┃╱╭━╯┃
╱╱╱╱╰╯╱╰━━╯
''')

print('Python Script to automate network monitoring and estimate geographic location of Access Points.')
os.system('sudo airmon-ng')

interfaceName = input('Choose which interface to commence monitor mode: ')

#print('Some processes must be terminated for monitor mode: ')
checkProcessesStream = os.popen('sudo airmon-ng check')
checkProcesses = checkProcessesStream.read()

if(checkProcesses):
	print('Some processes must be terminated for monitor mode: ')
	print(checkProcesses)

print('Running `check kill`...')
os.system('sudo airmon-ng check kill')

#start monitor mode on selected interface

monitorModeCommand = "sudo airmon-ng start " + interfaceName
os.system(monitorModeCommand)

print('Beginning monitor mode...')
os.system('sudo airodump-ng '+interfaceName)




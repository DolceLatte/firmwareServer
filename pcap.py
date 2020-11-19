import os
import argparse
import datetime

print("Please input seconds!")
time=input()

now = datetime.datetime.now()
now = str(now)
print(now)
table = str.maketrans(' .:-', '____' )
now = now.translate(table)
now = now + ' .pcap'
print(now)

tempt='tcpdump -G ' + str(time) + " -W 1 -w " + now
print(tempt)
os.system(tempt)
os.system('scp ' + now + ' cho2@168.188.129.208:Desktop')

if __name__ == "__main__" :

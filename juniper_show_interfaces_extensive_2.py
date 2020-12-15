import textfsm
from pprint import pprint

with open('juniper_show_interfaces_extensive.textfsm') as tfh:
    template=textfsm.TextFSM(tfh)
with open('juniper_show_interfaces_extensive.txt','r') as f:
    for line in f.readlines():
        interface_textfsm=template.ParseText(line,eof=False)

print(interface_textfsm) 
for result in interface_textfsm:
	print(result) 
	

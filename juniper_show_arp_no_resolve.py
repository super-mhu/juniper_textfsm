import textfsm
from pprint import pprint

with open('juniper_show_arp_no_resolve.txt') as rfh:
	raw_output = rfh.read()

print("\n******raw output******\n") 
print(raw_output) 

with open('juniper_show_arp_no_resolve.textfsm') as tfh:
	template=textfsm.TextFSM(tfh)

print("\n******textfsm template******\n") 
print(template) 
print(template.header) 

fsm_results=template.ParseText(raw_output) 
#print(fsm_results)

print("\n******textfsm output******\n") 
for result in fsm_results:
	print(result) 

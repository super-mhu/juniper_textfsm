##0. import modules 
import textfsm
from pprint import pprint

##1. get raw output 
with open('juniper_show_lldp_neighbors.txt') as rfh:
	raw_output = rfh.read()

print("\n******raw output******\n") 
print(raw_output) 

##2. call pre defined textfsm template  
with open('juniper_show_lldp_neighbors.textfsm') as tfh:
	template=textfsm.TextFSM(tfh)

print("\n******textfsm template******\n") 
print(template) 
print(template.header) 

##3. convert raw output into a list 
fsm_results=template.ParseText(raw_output) 

for result in fsm_results:
	print(result) 


##4. Combine variable and output list into a dictionary 

result_dict = {}

for result in fsm_results:
	for i in range(len(template.header)):
		result_dict[template.header[i]] = result[i]
	print(result_dict) 

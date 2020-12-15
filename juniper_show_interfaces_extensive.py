import textfsm
from pprint import pprint

##1. get raw output 
with open('juniper_show_interfaces_extensive.txt') as rfh:
	raw_output = rfh.read()

##2. print raw output 
print("\n******raw output******\n") 
#print(raw_output) 

##3. call pre defined textfsm file 
with open('juniper_show_interfaces_extensive.textfsm') as tfh:
	template=textfsm.TextFSM(tfh)

print("\n******textfsm template******\n") 
print(template) 
print(template.header) 

##4. convert raw output 
fsm_results=template.ParseText(raw_output) 

##5. print parsed output in the format of lists 
print("\n******textfsm output******\n") 
for result in fsm_results:
	print(result) 

##6. from the above output, find out the interfaces with highest input/output traffic rate 
high_input = 0
high_output = 0

for result in fsm_results:
	if (result[5]).isdigit() and (result[6]).isdigit(): 
		if int(result[5]) >= high_input:
			high_input=int(result[5]) 
			high_input_interface=result[0]
		if int(result[6]) >= high_output:
			high_output=int(result[6]) 
			high_output_interface=result[0]

print("\n******find interfaces with highest inptu/output rate******\n") 

print(f"Interface {high_input_interface} has highest input rate: {high_input}")
print(f"Interface {high_output_interface} has highest input rate: {high_output}") 

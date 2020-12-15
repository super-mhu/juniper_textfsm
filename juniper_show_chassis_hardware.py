##0. import modules 
import textfsm
from pprint import pprint

##1. get raw output 
with open('juniper_show_chassis_hardware_0.txt') as rfh:
	raw_output = rfh.read()

print("\n******raw output******\n") 
print(raw_output) 

##2. call pre defined textfsm template  
with open('juniper_show_chassis_hardware.textfsm') as tfh:
	template=textfsm.TextFSM(tfh)

print("\n******textfsm template******\n") 
print(template) 
print(template.header) 

##3. convert raw output into a list 
fsm_results=template.ParseText(raw_output) 

for result in fsm_results:
	print(result) 


##4. Get all MPC related info 

print("*"*100)
mpc_list = []

for result in fsm_results:
	if "MPC" in result[5]:
		mpc_list.append(result[5])
		print(result)

print(mpc_list) 

##5. Find out 3 most occurrance type of MPCs  

from collections import Counter 
print(Counter(mpc_list))
print(Counter(mpc_list).most_common(3))

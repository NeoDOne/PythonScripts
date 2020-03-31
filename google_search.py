#Written by:
#Rahul Das, CTO
#Ethical Securities
#Date: 30 March 2020

#Exception handling in python
try:
    from googlesearch import search
except ImportError:
    print("The module 'google' was not founf in your computer. Use 'pip3 install google' to install.")
query = input("What do you want to ask google?   ############## Type here: ")
for return_hits in search(
                query,
                start = 0,
                stop = None,
                ):
    print(return_hits)

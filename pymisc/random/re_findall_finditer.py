'''
re.findall() will find all occurrences of the pattern in the text and return them as separate entities, without considering any overlap in characters or positions.
aka if my text is "aaaaa" and I was looking for "aa" then it will generate aa,aa not aa aa aa aa .. basically it doesnt consider indexes that have been matched already. 

re.finditer() is same as re.findall but instead of putting all matches in memory, it yields them out one by one.

Lookbehind: Doesnt consume indexes for actual match, done with (?<=YOURPRECONDITIONBEFOREMATCH)MYMATCH where "YOURPRECONDITIONBEFOREMATCH" needs to happen before actual match
Lookafter:  done with MYMATCH(?=YOURPRECONDITIONAFTERMATCH) where "YOURPRECONDITIONAFTERMATCH" needs to happen after the actual match
'''
import re

print (*re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aAeEiIoOuU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",input()),sep='\n')

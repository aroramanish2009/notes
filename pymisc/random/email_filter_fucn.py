'''

A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters. 
>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
Now, you only require those elements that are greater than but less than .
>> l = list(filter(lambda x: x > 10 and x < 80, l))

'''


import re

def fun(s):
    # return True if s is a valid email, else return False
    regex = re.compile(r'([A-Za-z0-9-_]+)+@{1}[A-Za-z0-9]+(\.[A-Z|a-z]{,3}$)+')
    if re.match(regex,s):
        return (True)
    else:
        return (False)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

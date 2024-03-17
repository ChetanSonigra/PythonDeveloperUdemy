pattern = r'\d\d\d-\d\d\d-\d\d\d\d'  
# or pattern = r'\d{3}-\d{3}-\d{4}'
#r represents that this is a re
# special characters: 

# \d indicates numeric digit  , \D not a digit
# \w alphanumeric value     ,  \W not a alphanumeric value
# \s white space            ,  \S not a space

# Quantifiers: 
"""
    +    1 or more times , d+
   {n}   repeated n times , d{3}
   {n,m} repeated from n to m times , d{3,5}
   {n,}  repeated min n times , d{3,}
   *     0 or more times , \s*
   ?     once or zero times , dog?
"""

import re

text = 'If you need help, call 888-444-3333 anytime for online help'

pattern1 = 'pencil'
pattern2 = 'help'
search = re.search(pattern1, text); print(search) #search gives first occurence.
search = re.search(pattern2, text); print(search)
print(search.span(), search.start(), search.end())
search = re.findall(pattern2, text); print(search) # findall gives list of all findings
print(re.finditer(pattern2, text))                 # finditer gives iterator object consisting of all findings.
for finding in re.finditer(pattern2, text):
    print(finding.span())
    

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
search = re.search(pattern,text)
print(search.group(), search.group(2))

passwd = input("Password: ")
pattern = r'\D{1}\w{7}'
res = re.search(pattern, passwd)
print(res)

text = 'Saturday 5 and sunday 4 is closed.'
search = re.search(r'saturday|sunday', text); print(search)
search = re.search(r'saturday|monday', text); print(search)
search = re.search(r'lose', text); print(search)
search = re.search(r'.lose', text); print(search)
search = re.search(r'...lose', text); print(search)
search = re.search(r'^\D', text); print(search)
search = re.search(r'^\d', text); print(search)
search = re.search(r'\D$', text); print(search)
search = re.search(r'\d$', text); print(search)
search = re.findall(r'[^\d]', text); print(search)
search = re.findall(r'[^\s]+', text); print(search)
print(''.join(search))

import re

def check_email(email):
    pattern = r'\w+@\w+\.com'
    if re.search(pattern, email):
        print("Ok")
    else:
        print("The email address is incorrect")

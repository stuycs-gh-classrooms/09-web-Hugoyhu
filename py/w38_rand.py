#!/usr/bin/python3
print('Content-type: text/html\n')

from random import random

print('hello, ', random())

from datetime import date, datetime

print (
f'''

<head><title>random w38</title></head>
<body style="background-color:pink;">
    <p>
        Hello! This is a random number: {random()}
        <br>
        Today, it is {datetime.now().strftime("%A, %B %d. It is %I:%M %p.")}
    </p>
</body>





'''
)
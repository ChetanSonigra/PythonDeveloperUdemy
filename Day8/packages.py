# till now whatever we used, we already had installed when we installed python
# These are called standard or built-in libraries.
# PyPi = 3rd party python packages.
# pip install to get packages from PyPi repository.
# search in google for any task you want to do.
# ex: 'Python packages for console text color. -- pip install colored
from colored import fg,bg,attr
color = fg(1) + bg(15)
print(color + 'Hello World' + attr(0))

# Python packages for excel: many packages. pip install openpyxl
from openpyxl import * 